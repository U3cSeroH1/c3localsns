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
        })
        .then(response => {
          //console.log(response.data.username)
          this.axios
            .post('http://127.0.0.1:8000/api/v1/postManager/posts/create/', { text : this.text , author : response.data.pk },{
              headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
            })
            .then(response => {this.results = response.data})
        })
    }
  },
})
</script>