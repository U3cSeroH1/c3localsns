<template>
  <div class="hello">
      <p>コールバック</p>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex';
export default({
  name: 'discordCallBack',
  data() {
    return {
      oauthClientId: "783546093198639146",
      oauthClientSecret: "Q8nFq7vYWVMRwu5kWO2rDAnb82hwSG1p",
      oauthRedirectUri: "http://localhost:8080/callback"
    };
  },
  methods: {
    ...mapActions([
      'updateToken',
      'updateLoginUser'
    ])
  },
  mounted() {
    //vue-router使える人いたらここそれ専用に書き換えといて

    const urlParams = new URLSearchParams(window.location.search)
    //document.getElementById("urlparam").innerHTML = url;

    const code = urlParams.get("code");
    console.log("Code: ", code)

    if(!window.$cookies.isKey('c3localsns-app-auth') && code){
      const DiscordOauth2 = require("discord-oauth2");
        const oauth = new DiscordOauth2();
          oauth.tokenRequest({
            clientId: this.oauthClientId,
            clientSecret: this.oauthClientSecret,
            code: code,
            scope: "identify guilds",
            grantType: "authorization_code",
            redirectUri: this.oauthRedirectUri,
          }).then(discordAccessInfo=>{
            axios.post('http://127.0.0.1:8000/api/v1/oauthLoginManager/discord/token', {
                access_token: discordAccessInfo.access_token,
                code: ""
              },{
                headers: { "Content-Type": "application/json"},
              }).then(response => {   
                this.results = response.data
                console.log(this.results)
                this.updateToken(response.data.access_token)
                this.updateLoginUser(this.results.user)
                window.$cookies.set('c3localsns-app-auth', response.data.access_token, 600);
                window.$cookies.set('c3localsns-app-auth-refresh', response.data.refresh_token, 600);
                this.$router.push('/')
              })
        })
        }
    }

    
})
</script>