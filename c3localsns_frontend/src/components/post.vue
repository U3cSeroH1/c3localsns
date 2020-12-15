<template>
  <div class="box">
    <article class="media">
      <div class="media-left">
        <figure class="image is-64x64">
          <img class="is-rounded" :src="getAvatarUrl(post.author.extra_data.id, post.author.extra_data.avatar)">
        </figure>
      </div>
      <div class="media-content">
        <div class="content">
          <p>
            <strong>{{ post.author.first_name }}</strong>
            <br />
            {{ post.text }}
          </p>
        </div>
        <nav class="level is-mobile">
        <div class="level-left">
          <a class="level-item" aria-label="reply">
            <span class="icon is-small">
              <favorite-button :post="post"></favorite-button>
            </span>
          </a>
        </div>
      </nav>
      </div>
    </article>
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
  },
  created() {
    console.log(this.post)
  },
  methods: {
    getAvatarUrl(userId, avatarId) {
      return `https://cdn.discordapp.com/avatars/${userId}/${avatarId}.png?size=256`
    }
  }
}
</script>
FavoriteButton
<style scoped>
img {

}
.box {
  margin: 3rem 0;
}
</style>