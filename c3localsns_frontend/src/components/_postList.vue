<template>
  <div class="columns">
    <div class="column"></div>
    <div class="column is-four-fifths" ref="postList">
      <post :post="post" v-for="post in getList" :key="post" style="display:block" />
    </div>
    <div class="column"></div>
  </div>
</template>

<script>
import Post from './post'
import { mapActions, mapGetters } from 'vuex'

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
  methods: {
    ...mapActions([
      'updateStatusList'
    ]),
    addUpdateListListener() {
      window.addEventListener('scroll', this.updateListListenerHandler)
    },
    updateListListenerHandler() {
      if(window.scrollY + window.innerHeight > this.$refs.postList.clientHeight) this.updateList()
    },
    updateList() {
      window.removeEventListener('scroll', this.updateListListenerHandler)
      this.updateStatusList()
    }
  },
  computed: {
    ...mapGetters([
      'getList'
    ])
  },
  mounted() {
    this.addUpdateListListener()
    this.updateList()
  },

  //https://cdn.discordapp.com/avatars/139707810152710144/f218070c0036af478d6baba14a3d3864
  //https://cdn.discordapp.com/avatars/ユーザID/アバターID
})
</script>