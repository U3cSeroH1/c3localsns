<template>
  <div class="hello">
    <button v-if="!isLogin" onclick="location.href='https://discord.com/api/oauth2/authorize?client_id=781573068560662539&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fcallback&response_type=code&scope=identify%20guilds'">Discord Login</button>
    <button v-on:click="logout">Logout</button>
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
      isLogin: false
    };
  },
  created() {
    this.isLogin = this.checkLogin()
  },
  methods: {
    checkLogin() {
      return window.$cookies.get("c3localsns-app-auth")
    },
    login: function(){
      axios
        .post('http://127.0.0.1:8000/dj-rest-auth/login/', { username : this.username , password : this.password })
        .then(response => 
        {   
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