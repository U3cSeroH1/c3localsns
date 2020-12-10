<template>
  <div class="columns">
    <div class="column"></div>
    <div class="column is-four-fifths">
      <post :post="post" v-for="post in posts" :key="post" style="display:block" />
    </div>
    <div class="column"></div>
  </div>
</template>

<script>
import axios from 'axios'
import Post from './post'
export default({
  name: 'postList',
  components: {
    Post
  },
  data() {
    return {
      posts: []
    };
  },
  mounted() {
      axios.get("http://127.0.0.1:8000/api/v1/postManager/posts/list/", {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},
      })
      .then(response => (this.posts = response.data));
  }

  //https://cdn.discordapp.com/avatars/139707810152710144/f218070c0036af478d6baba14a3d3864
  //https://cdn.discordapp.com/avatars/ユーザID/アバターID
})
</script>