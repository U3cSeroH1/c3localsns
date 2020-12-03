<template>
  <img alt="Vue logo" src="../assets/logo.png">
  <postCreate></postCreate>
  <postList></postList>
  <register></register>
</template>

<script>
import postCreate from '../components/_postCreate.vue'
import postList from '../components/_postList.vue'
import register from '../components/_register.vue'
export default {
  name: 'Home',
  components: {
    postCreate,
    postList,
    register
  }
}
</script>
