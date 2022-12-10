import { createRouter, createWebHistory } from 'vue-router'

const routes = [
        {path: '', name: 'Home', component: () => import('@/views/Home.vue')},
        {path: '/about', name: 'About', component: () => import('@/views/About.vue')},
        {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},
        {path: '/register', name: 'Register', component: () => import('@/views/Register.vue')},
        {path: '/profile', name: 'Profile', component: () => import('@/views/Profile.vue')},
        {path: '/bids', name: 'Bids', component: () => import('@/views/Bids.vue')},
    ]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router