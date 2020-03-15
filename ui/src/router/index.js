import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/dashboard.vue'
import NotFound from '../views/notFound'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'dashboard',
    meta: {
      name: 'Dashboard',
      calls: [],
      requiresAuth: true
    },
    component: Dashboard
    
  },
  {
    path: "**",
    component: NotFound,
    meta: {
      noAppBar: true
    }
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.onReady(() => {
  router.beforeEach((to, from, next) => {
    next()
  })
})

export default router
