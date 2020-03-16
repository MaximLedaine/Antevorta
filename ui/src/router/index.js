import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/dashboard.vue'
import NotFound from '../views/notFound'
import types from '../store/types'

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
    path: '/query',
    name: 'query',
    meta: {
      name: 'Query',
      calls: [],
      requiresAuth: true
    },
    component: () => import(/* webpackChunkName: "vehicleChild" */ '../views/queryView')
  },
  {
    path: '/stocks',
    name: 'stocks',
    meta: {
      name: 'Stocks',
      calls: [],
      requiresAuth: true
    },
    component: () => import(/* webpackChunkName: "vehicleChild" */ '../views/stocksView')
  },
  {
    path: '/stocks/:symbol',
    name: 'stock',
    meta: {
      name: 'Stock',
      calls: [types.db.actions.getStats, types.db.actions.getCompany, types.db.actions.getStatistics],
      requiresAuth: true
    },
    component: () => import(/* webpackChunkName: "vehicleChild" */ '../views/stocksView/children/stocksChild')
  },
  {
    path: '/analysis',
    name: 'analysis',
    meta: {
      name: 'Analysis',
      calls: [],
      requiresAuth: true
    },
    component: () => import(/* webpackChunkName: "vehicleChild" */ '../views/analysisView')
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
