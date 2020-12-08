<template>
  <div>
    <register></register>
    <postCreate></postCreate>
    <postList></postList>
  </div>
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
  },
  data() {
    return {
      isLogin: false
    }
  },
  created() {
    this.isLogin = this.checkLogin()
  },
  methods: {
    checkLogin() {
      return window.$cookies.get("c3localsns-app-auth")
    }
  }
}
</script>
