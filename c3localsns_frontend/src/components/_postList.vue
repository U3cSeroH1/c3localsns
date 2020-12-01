<template>
  <div class="hello">
    <li v-for="Post in Posts" :key="Post" style="display:block">
      <div >
        <div style="display:block">{{Post.author}}</div>
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
})
</script>