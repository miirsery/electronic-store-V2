import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Layout',
    component: () => import('@/layout/Layout.vue'),
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/pages/Home.vue'),
      },
      {
        path: '/cart',
        name: 'CartPage',
        component: () => import('@/pages/CartPage.vue'),
      },
      {
        path: '/profile',
        name: 'ProfilePage',
        component: () => import('@/pages/ProfilePage.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
