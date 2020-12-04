<template>
  <div class="hello">
      <p>コールバック</p>
  </div>
  
</template>

<script>
export default({
  name: 'discordCallBack',
  data() {
    return {

    };
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
                      console.log(this.results)
                      window.$cookies.set('c3localsns-app-auth', response.data.access_token, 600);
                      window.$cookies.set('c3localsns-app-auth-refresh', response.data.refresh_token, 600);
                      this.$router.push('/')
                      
                  })
                
            })
        }
    }

    
})
</script>