<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <postCreate></postCreate>
  <postList></postList>
  <register></register>

</template>

<script>


import postList from './components/_postList.vue'
import postCreate from './components/_postCreate.vue'
import register from './components/_register.vue'


export default {
  name: 'App',
  components: {
    postList,
    postCreate,
    register,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
