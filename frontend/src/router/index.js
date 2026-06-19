import { createRouter, createWebHistory } from 'vue-router'
import { routes } from './routes'
import { isAuthenticated } from '@/composable/useAuth'

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  if (to.name !== 'login' && !isAuthenticated()) {
    return { name: 'login' }
  }
})

export default router
