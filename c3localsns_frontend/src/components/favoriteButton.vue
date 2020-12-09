<template>
  <div>
    <button @click="favorite()">♡{{ post.favorites.length }}</button>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  props: {
    post: {}
  },
  methods: {
    favorite() {
      axios.post(
        'http://localhost:8000/api/v1/postManager/favorites',
        {
          user: this.post.author.id,
          post: this.post.id
        },
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')
          }
        }
      )
    }
  }
}
</script>