import { createRouter, createWebHistory } from 'vue-router'
import Register from '../components/Register.vue'
import Index from '../views/Index.vue'
import MovieDetails from '../components/MovieDetails.vue'


const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../components/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },

  {
    path: '/movies/:id',
    name: 'movie',
    component: MovieDetails,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})



export default router
