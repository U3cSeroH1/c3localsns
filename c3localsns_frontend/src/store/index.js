import { createStore } from 'vuex'
import axios from 'axios'

const baseUrl = "http://127.0.0.1:8000/api/v1"
export default createStore({
  state: {
    user: {},
    extraData: {},
    token: "",
    list: [],
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
      console.log(res.extra_data)
      commit('updateExtraData', res.extra_data)
    },
    // fetchStatusList
    async updateStatusList({ commit }) {
      const res = await axios.get(baseUrl + "/postManager/posts", {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      commit('updateList', res.data)
    },

    async postStatus({ getters, dispatch }, text) {
      console.log("postStatus")
      console.log(getters.getUser)
      await axios.post(baseUrl + '/postManager/posts', {
        text: text,
        author_id: getters.getUser.pk
      }, {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      await dispatch('updateStatusList')
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
