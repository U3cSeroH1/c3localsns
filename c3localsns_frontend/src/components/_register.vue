<template>
  <div class="hello">
    <button onclick="location.href='http://127.0.0.1:8000/accounts/discord/login'">ぢｓこｒｄろぐいんぽ！！！！！！</button>

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
  }
})
</script>