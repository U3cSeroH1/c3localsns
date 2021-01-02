<template>
  <div id="app" class="has-background-light">
    <navbar />
    <router-view/>
  </div>
</template>
<script>
import Navbar from '@/components/Navbar' 
import { mapActions } from 'vuex'
export default {
  components: {
    Navbar
  },
  methods: {
    ...mapActions([
      'updateLoginUser',
      'updateExtraData',
      'startWebSocket'
    ])
  },
  created() {
    this.updateLoginUser(null)
    this.startWebSocket(null)
    //this.updateExtraData()
  }
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
