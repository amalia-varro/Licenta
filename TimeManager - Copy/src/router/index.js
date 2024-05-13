/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
// import { createRouter, createWebHistory } from 'vue-router/auto'
// import { setupLayouts } from 'virtual:generated-layouts'
//
// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   extendRoutes: setupLayouts,
// })

import {createRouter, createWebHistory} from 'vue-router'
import DefaultLayout from "@/layouts/default.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/HomePage.vue')
        },
      ]
    },
    {
      path: "/login",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/LoginPage.vue')
        },
      ]
    },
    {
      path: "/register",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/RegisterPage.vue')
        },
      ]
    },
    {
      path: "/attendance",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/AttendanceHistory.vue')
        },
      ]
    }
  ]
})

export default router
