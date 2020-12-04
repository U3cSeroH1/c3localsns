<template>
  <div class="hello">
    <span>Multiline text is:</span>
    <p style="white-space: pre-line;">{{ text }}</p>

    <textarea v-model="text" placeholder="add multiple lines"></textarea>
    <button v-on:click="postText">あほ</button>
  </div>
</template>

<script>
export default({
  name: 'postCreate',
  data() {
    return {
      text: "",
      author: null,
    };
  },
  methods:{
    postText: function(){

      this.axios
        .get('http://127.0.0.1:8000/dj-rest-auth/user/', 
            {headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
            //ここで使ってる奴のid見る
        })
        .then(response => {
          
          const author = response.data.pk
          console.log(response.data)

          this.axios
            .get('http://127.0.0.1:8000/api/v1/oauthLoginManager/discord/extradata/?f=' + response.data.pk, 
                {headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
                //ここで使ってる奴のid見る
            })
            .then(response => {
              
              const jsondata = response.data[0].extra_data.replace( /'/g, '"' )
              
              //var jsonStr = '{"name":"山田太郎","age":{"age":"111", "aho":"うんち"},"gender":"M"}';
              //console.log(JSON.parse(jsonStr))
              const jsondata2 = jsondata.replace( /True/g, '"True"' )
              const jsondata3 = jsondata2.replace( /False/g, '"False"' )
              const jsondata4 = jsondata3.replace( /None/g, '"None"' )
              //console.log(jsondata3)
              console.log(jsondata4)
              const jsondata5 = JSON.parse(jsondata4)
              console.log(jsondata5)



              const authorname = jsondata5.username

              var authoravatar = null
              if(jsondata5.avatar == "None"){
                authoravatar = "/defaultavatar.png"
              }
              else{
                authoravatar = "https://cdn.discordapp.com/avatars/" + jsondata5.id + "/" + jsondata5.avatar
              }
              
              //console.log(response.data.username)
              this.axios
                .post('http://127.0.0.1:8000/api/v1/postManager/posts/create/', { text : this.text ,authorname:authorname, authoravatar:authoravatar, author : author },{
                  headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
                })
                .then(response => {this.results = response.data})
              })





            })






    }
  },
})
</script>