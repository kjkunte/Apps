<template>
  <div class="hello">
   </div>
</template>

<script>
import axios from 'axios'
export default {
 
 data() {
   return {
     severity : []
   } 
 },
 mounted() {
   this.getSeverity()
 },

 methods: {
   getSeverity() {
     const path = 'http://localhost:5000/api/severity';
    //  What is axios | What is its node equivalent
     axios({method: 'GET', url: path}).then(
       result => {
         console.log(result.data)
         this.severity = result.data
       },
       error => {
         console.error(error)
       }
     )
   }
 }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
