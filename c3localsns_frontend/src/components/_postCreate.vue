<template>
  <div class="hello">
    <span>Multiline text is:</span>
    <p style="white-space: pre-line;">{{ text }}</p>
    <p style="white-space: pre-line;">{{ author }}</p>
    <br>
    <textarea v-model="text" placeholder="add multiple lines"></textarea>
    <textarea v-model="author" placeholder="add multiple lines"></textarea>
    <button v-on:click="postText">あほ</button>
  </div>
</template>

<script>
export default({
  name: 'postCreate',
  data() {
    return {
      text: "",
      author:""
    };
  },
  methods:{
    postText: function(){
      
      this.axios
        .post('http://127.0.0.1:8000/api/v1/postManager/posts/create/', { text : this.text , author : parseInt(this.author) },{
          headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
        })
        .then(response => {this.results = response.data})
    }
  },
})
</script>