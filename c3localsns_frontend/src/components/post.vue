<template>
  <div>
    <img :src="post.authoravatar">
    <h3>{{ post.author.username }}</h3>
    <p>{{ post.text }}</p>
    <favorite-button :post="post"></favorite-button>
  </div>
</template>
<script>
import FavoriteButton from './favoriteButton.vue'
export default {
  components: {
    FavoriteButton
  },
  props: {
    post: {}
  }
}
</script>
FavoriteButton
<style scoped>
img {
  width: 3rem;
}
</style>