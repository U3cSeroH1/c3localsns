<template>
  <nav class="navbar is-link">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <div>CCCOSNS</div>
      </a>
    </div>
    <div class="navbar-end">
      <register />
    </div>
  </nav>
</template>
<script>
import register from './_register'
export default {
  components: {
    register
  }
}
</script>