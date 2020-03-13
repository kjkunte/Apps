<template>
  <div>
    <pie-chart :data="severity"></pie-chart>
    <triggerApi @buttonClicked="severityFor = $event"> </triggerApi>
  </div>
</template>

<script>
import axios from 'axios'
import Dropdown from './Dropdown';
export default {
 components: {
    'triggerApi':Dropdown
  },
 data() {
   return {
     severityFor :'',
     severity : [
      //  ['1']
     ]
   } 
 },
 mounted() {
   this.getSeverity1(this.severityFor)
   this.getSeverity()
 },

 methods: {
  //  getSeverity1(abc) {
  //    console.log(this.severityFor)
  //    const path = `http://localhost:5000/api/severity/${abc}`
  //   //  What is axios | What is its node equivalent
  //    axios({method: 'GET', url: path}).then(
  //      result => {
  //        this.severity = result.data.severity;
  //        console.log(this.severity);
  //      },
  //      error => {
  //        console.error(error)
  //      }
  //    )
  //  },
   getSeverity() {
     const path = `http://localhost:5000/api/severity/`
     axios({method: 'GET', url: path}).then(
       result => {
         this.severity = result.data.severity;
         console.log(this.severity);
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
