
<template>
  <ul>
    <li><router-link :to="{name:'Home'}">Home</router-link></li>
    <li><router-link :to="{name:'About'}">About</router-link></li>
    <li><router-link :to="{name:'Login'}">Login/Register</router-link></li>
    <li><router-link :to="{name:'Profile'}">Profile</router-link></li>
    <li><router-link :to="{name:'Bids'}">Bids</router-link></li>
  </ul>
  <router-view />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>


