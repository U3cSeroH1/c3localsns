<template>
  <div>
    <div class="field">
      <label class="label">Text</label>
      <div class="control">
        <textarea class="textarea" v-model="text" placeholder="Text"></textarea>
      </div>
    </div>
    <div class="field">
      <div class="control">
        <button class="button is-primary" @click="postStatus(text)">Post</button>
      </div>
    </div>
  </div>
</template>

<script>
import  { mapActions } from 'vuex'
export default({
  name: 'postCreate',
  data() {
    return {
      text: "",
    };
  },
  methods:{
    ...mapActions([
      'postStatus'
    ])
  },
})
</script>