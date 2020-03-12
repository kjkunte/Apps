<template>
  <div id="app">
    <!-- <dashboard/>
    <piechart/> -->
    <router-view/>
  </div>
</template>

<script>
import dashboard from './components/dashboard.vue'
import piechart from './components/piechart.vue'

export default {
  name: 'App',
  components: {
    dashboard,
    piechart
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
