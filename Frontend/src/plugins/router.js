import { createRouter, createWebHistory } from 'vue-router'

const routes = [
        {path: '', name: 'Home', component: () => import('@/views/Home.vue')},
        {path: '/login', name: 'Login', component: () => import('@/views/Login.vue')},
        {path: '/register', name: 'Register', component: () => import('@/views/Register.vue')},
        {path: '/profile', name: 'Profile', component: () => import('@/views/Profile.vue')},
        {path: '/bids', name: 'Bids', component: () => import('@/views/Bids.vue')},
        {path: '/add', name: 'Add', component: () => import('@/views/AddItem.vue')},
    ]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router
