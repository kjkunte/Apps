<template>
  <div id="app">
    <header>
    <Navbar/>
    </header>
    <dashboard/>
    <router-view/>
  </div>
</template>

<script>
import dashboard from './components/dashboard.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    dashboard,
    Navbar
  }
}
</script>

<style>
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
body {
font-family: 'montserrat', sans-serif;
}

header {
  width:100vw;
  background-color: #222;
  padding: 15px
}
</style>
