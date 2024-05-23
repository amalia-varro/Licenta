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
    },
    {
      path: "/teleworking",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/TeleworkingRequest.vue')
        },
      ]
    },
    {
      path: "/vacation",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/VacationRequest.vue')
        },
      ]
    },
    {
      path: "/teamtimesheet",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/TeamTimesheet.vue')
        },
      ]
    },
    {
      path: "/teamteleworking",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/TeamTeleworking.vue')
        },
      ]
    },
    {
      path: "/teamvacation",
      component: DefaultLayout,
      children: [
        {
          path: '',
          component: () => import('@/pages/TeamVacation.vue')
        },
      ]
    }
  ]
})

export default router
