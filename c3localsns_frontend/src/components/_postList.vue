<template>
  <div class="hello">
    <li v-for="Post in Posts" :key="Post" style="display:block">
      <div >
        <img :src="Post.authoravatar">
        <div style="display:block">{{Post.authorname}}</div>
        <div>{{Post.text}}</div>
      </div>
      
    </li>
    
  </div>
</template>

<script>
export default({
  name: 'postList',
  data() {
    return {
      Posts: []
    };
  },
  mounted() {
    this.axios
      .get("http://127.0.0.1:8000/api/v1/postManager/posts/list/", {
        headers: { "Content-Type": "application/json" , "Authorization": "Bearer " + window.$cookies.get('c3localsns-app-auth')},

      })
      .then(response => (this.Posts = response.data));
  }

  //https://cdn.discordapp.com/avatars/139707810152710144/f218070c0036af478d6baba14a3d3864
  //https://cdn.discordapp.com/avatars/ユーザID/アバターID
})
</script>