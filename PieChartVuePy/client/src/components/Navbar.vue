<template>
  <nav>
    <div class="menu-item"><a href="#">Home</a></div>
    <div class="menu-item"><a href="#">About</a></div>
    <Dropdown title="Severity" :items="severityTypes" />
    <div class="menu-item"><a href="#">Contact</a></div>
  </nav>
</template>

<script>
import Dropdown from './Dropdown';
export default {
  name: 'navbar',
  components: {
    Dropdown
  },
  data () {
    return {
      severityTypes: [
        {
          id: 1,  
          title: 'All',
          link: '#'
        },
        {
          id: 2,  
          title: 'Week',
          link:'#'
        },
        {
          id: 3,
          title: 'Month',
          link: '#'
        }
      ]
    }
  }
}
</script>

<style>
nav {
  display: flex;
  align-items: center;
  justify-content: center;
}
nav .menu-item {
  color: #FFF;
  padding: 10px 20px;
  position: relative;
  text-align: center;
  border-bottom: 3px solid transparent;
  display: flex;
  transition: 0.4s;
}
nav .menu-item.active,
nav .menu-item:hover {
  background-color: #444;
  border-bottom-color: #FF5858;
}
nav .menu-item a {
  color: inherit;
  text-decoration: none;
}
</style>