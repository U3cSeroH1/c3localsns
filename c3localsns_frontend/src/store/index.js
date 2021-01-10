import { createStore } from 'vuex'
import axios from 'axios'

const baseUrl = "http://127.0.0.1:8000/api/v1"
export default createStore({
  state: {
    user: {},
    extraData: {},
    token: "",
    list: [],
    offset: 0,
    limit: 10,
    hasLogin: false
  },
  mutations: {
    updateToken(state, token) {
      state.token = token
    },
    updateLoginUser(state, user) {
      console.log(user)
      state.hasLogin = true
      state.user = user
    },
    updateExtraData(state, extraData) {
      state.extraData = extraData
    },
    updateList(state, list) {
      state.list = list
    },
    updateLatestPost(state, post) {
      console.log('あほ')
      state.list.splice(0, 0, post)
    },
    updateNextList(state, list) {
      state.list = state.list.concat(list)
    },
    updateOffset(state, count) {
      state.offset += count
    }
  },
  actions: {
    updateToken({ commit }, token) {
      commit('updateToken', token)
    },
    async updateLoginUser({ commit }, user) {
      if(user !== null) {
        commit('updateLoginUser', user)
      } else {
        console.log('fetch User')
        try {
          const res = await axios('http://localhost:8000/dj-rest-auth/user/', {
            headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
          })
          const user = await res.data
          commit('updateLoginUser', user)
        } catch (err) {
          console.log("Login Timeouted", err)
          return err
        }
      }
      const res = await axios.get(baseUrl + '/oauthLoginManager/discord/extradata', {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      console.log(res.data.extra_data)
      commit('updateExtraData', res.data.extra_data)
    },
    // fetchStatusList
    async updateStatusList({ commit }) {
      const res = await axios.get(baseUrl + "/posts/" + `?limit=${this.state.limit}&offset=${this.state.offset}`, {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      console.log(res.data.count)
      commit('updateNextList', res.data.results)
      commit('updateOffset', res.data.count)
    },

    async postStatus({ commit, getters, dispatch }, text) {
      console.log("postStatus")
      console.log(getters.getUser)
      await axios.post(baseUrl + '/postManager/posts', {
        text: text,
        author_id: getters.getUser.pk
      }, {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      await dispatch('updateStatusList')
      commit('updateOffset', 1)
    },

    async startWebSocket({ commit }, text) {
      console.log("otimpo")
      //console.log(getters.getUser)

      console.log(text)

      // WebSocket 接続を作成
      const socket = new WebSocket('ws://localhost:5000');

      // 接続が開いたときのイベント
      socket.addEventListener('open', function (event) {
        socket.send('Hello Server!');
        console.log('Message to server ', event.data);
      });

      // メッセージの待ち受け
      socket.addEventListener('message', async function (event) {

        const data = JSON.parse(event.data)


        switch(data.channel) {
          case "POST": {
            console.log("ばかPOST")
            console.log(data)
            const res = await axios.get(baseUrl + "/posts/" + data.id + "/", {
              headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
            })

            
            commit('updateLatestPost', res.data)
            break            
          }


          case "FAVORITE": {
            console.log("あほFAVORITE")
            break
          }


          default: {
            //console.log("うんちぶりぶりだいばくはつVER2")
            //console.log(data)
          }
        }
      });
    }
  },
  getters: {
    hasLogin(state) {
      if(state.user !== {}) return true
      else false
    },
    getUser(state) {
      return state.user
    },
    getList(state) {
      return state.list
    }
  },
  modules: {
  }
})
