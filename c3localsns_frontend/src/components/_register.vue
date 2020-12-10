<template>
  <div class="navbar-item">
    <div class="buttons">
      <button class="button is-primary" v-if="!isLogin" @click="redirectDiscordLogin()">Login</button>
      <button class="button" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default({
  name: 'postList',
  data() {
    return {
      username:"",
      password:"",
      isLogin: false,
      callbackUrl: "https://discord.com/api/oauth2/authorize?client_id=783546093198639146&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Fcallback&response_type=code&scope=guilds%20identify%20email%20guilds.join"
    };
  },
  created() {
    this.isLogin = this.checkLogin()
  },
  methods: {
    redirectDiscordLogin() {
      location.href = this.callbackUrl
    },
    checkLogin() {
      return window.$cookies.get("c3localsns-app-auth")
    },
    login: function(){
      axios
        .post('http://127.0.0.1:8000/dj-rest-auth/login/', { username : this.username , password : this.password })
        .then(response => {   
            this.results = response.data
            window.$cookies.set('c3localsns-app-auth', response.data.access_token, 6000);
            window.$cookies.set('c3localsns-app-auth-refresh', response.data.refresh_token, 6000);
            window.location.reload();
        })
    },
    discordlogin: function(){
      
    },
    logout: function(){
      axios
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
      
})
</script>