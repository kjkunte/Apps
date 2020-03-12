<template>
    <div>
      <pie-chart :data="[['Nokia',50],['Samsung',150]]">  </pie-chart>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="scss" scoped>
.pie-chart {
    width: 300px;
    height: 300px; 
    border-radius: 50%;
    border: 2px solid #fefefe;
    background : conic-gradient(
        #fefefe 0 30%
        #00fe00 0 70%
        #0000fe 0 100%
    );
}
</style>