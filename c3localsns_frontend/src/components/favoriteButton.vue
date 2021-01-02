<template>
  <div>
    <i v-if="!this.isMeFavorited" class="mdi mdi-heart-outline" @click="favorite() " aria-hidden="true"></i>
    <i v-if="this.isMeFavorited" class="mdi mdi-heart" @click="favorite() " aria-hidden="true"></i>
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
        'http://localhost:8000/api/v1/posts/favorites/',
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
  },
  computed: {
    isMeFavorited() {
      if(this.post.favorites !== [] && this.post.favorites.length > 0) return true
      else return false
    }
  }
}
</script>