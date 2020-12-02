<template>
  <div class="hello">
    <button onclick="location.href='https://discord.com/api/oauth2/authorize?client_id=781573068560662539&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fcallback&response_type=code&scope=identify'">ぢｓこｒｄろぐいんぽ！！！！！！</button>
    <br><br><br>

    <span>情報かけ:</span>
        <input v-model="username" placeholder="user">
        <input v-model="password" placeholder="password">
    <br>    
    <button v-on:click="login">ただのろぐいんぽ！！！！！！</button>
    <button v-on:click="logout">でてけぇ！！！！！！！！！！！！！！！！！</button>
  </div>
  
</template>

<script>
export default({
  name: 'postList',
  data() {
    return {
      username:"",
      password:""
    };
  },
  methods: {
    login: function(){
      this.axios
        .post('http://127.0.0.1:8000/dj-rest-auth/login/', { username : this.username , password : this.password })
        .then(response => 
        {   
            this.results = response.data
            window.$cookies.set('c3localsns-app-auth', response.data.access_token, 600);
            window.$cookies.set('c3localsns-app-auth-refresh', response.data.refresh_token, 600);
            window.location.reload();
        })
    },
    discordlogin: function(){
      
    },
    logout: function(){
      this.axios
        .post('http://127.0.0.1:8000/dj-rest-auth/logout/', {
          headers: { "Content-Type": "application/json"},
        })
        .then(response => 
        {   
            this.results = response.data
            window.$cookies.remove('c3localsns-app-auth');
            window.$cookies.remove('c3localsns-app-auth-refresh');
            window.location.reload();
        })
    }    
  },
  mounted() {
    //vue-router使える人いたらここそれ専用に書き換えといて

    var url = location.search;
    //document.getElementById("urlparam").innerHTML = url;

    const code = url.substr(6);
    console.log(url);

    if(!window.$cookies.isKey('c3localsns-app-auth') && code){
      const DiscordOauth2 = require("discord-oauth2");
            const oauth = new DiscordOauth2();



            oauth
              .tokenRequest({
                clientId: "781573068560662539",
                clientSecret: "OiSPDK6CChZwne3fRDsBb-80tVQCCUyX",
            
                code: code,
                scope: "identify guilds",
                grantType: "authorization_code",
                
                redirectUri: "http://127.0.0.1:8080/callback",
            })
              .then(discordAccesInfo=>{
                console.log(discordAccesInfo);
                this.axios
                  .post('http://127.0.0.1:8000/api/v1/oauthLoginManager/discord/token', {access_token: discordAccesInfo.access_token,
                    code: ""},{
                    headers: { "Content-Type": "application/json"},
                  })
                  .then(response => 
                  {   
                      this.results = response.data
                      window.$cookies.set('c3localsns-app-auth', response.data.access_token, 600);
                      window.$cookies.set('c3localsns-app-auth-refresh', response.data.refresh_token, 600);
                      window.location.reload();
                  })
                
            })
        }
    }

    
})
</script>