<template>
  <div>
    <img :src="iconUrl">
    <h3>{{ authorName }}</h3>
    <p>{{ text }}</p>
  </div>
</template>
<script>
export default {
  props: {
    iconUrl: String,
    authorName: String,
    text: String
  }
}
</script>
<style scoped>
img {
  width: 3rem;
}
</style>