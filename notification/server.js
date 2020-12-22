const redis = require('redis')
const process = require('process')
const WebSocketServer = require('websocket').server
const http = require('http')
const { connection } = require('websocket')

let server = http.createServer((req, res) => {
    console.log("Received request", req.url)
    res.writeHead(404)
    res.end()
})

let ws = new WebSocketServer({
    httpServer: server,
    autoAcceptConnections: false
})

const originIsAllowed = (origin) => {
    return true
}

let connections = []

ws.on('request', (req) => {
    if(!originIsAllowed(req.origin)) {
        req.reject()
        console.log('Connection rejected from', req.origin)
        return ;
    }
    connections.push(req.accept(null))
    console.log('Connection accepted', connection.length, 'th.')
})

const redisOptions = {
    host: process.env.REDIS_HOST || 'redis',
    port: process.env.REDIS_PORT || 6379,
}

if(process.env.REDIS_URL !== undefined) {
    redisOptions = process.env.REDIS_URL
}

const r = redis.createClient(redisOptions);

r.subscribe('FAVORITE')
r.subscribe('POST')

console.log('start redis subscribing')
r.on('message', (channel, message) => {
    console.log(channel, message)
    connections.forEach((con) => {
        con.send(JSON.stringify({
            channel,
            id: parseInt(message)
        }))
    })
})

server.listen(5000, () => {
    console.log('Start WebSocket server listen...')
})