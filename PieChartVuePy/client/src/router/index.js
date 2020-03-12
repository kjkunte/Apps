import Vue from 'vue'
import Router from 'vue-router'
import dashboard from '@/components/dashboard.vue'
// import piechart from '@/components/piechart.vue'

const routerOptions = [
    {path: '/', component: dashboard},
    // {path: 'piechart', component: piechart},
]
// The .map will call a predefined callback function on the array and return an array of results
// Here the array is RouterOptions
// const routes = routerOptions.map(route => {
//     return{
//         ...route,
//         component: () =>
//     import(`@/components/${route.component}.vue`)
//     }
// })



Vue.use(Router)

export default new Router
({
    routerOptions,
    mode:'history'
})
    