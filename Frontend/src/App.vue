
<template>
  <div id="wrapper">
    <nav class="navbar fixed-top navbar-dark bg-dark">
  <div class="container-fluid">
    <h3>Group 51</h3>
      <ul class="nav">
    <li class="nav-item">
      <a class="nav-link active"><router-link :to="{name:'Home'}">Home</router-link></a>
    </li>
    <li class="nav-item">
      <a class="nav-link" ><router-link :to="{name:'Login'}"> Login/Register </router-link></a>
    </li>
    <li class="nav-item">
      <a class="nav-link"><router-link :to="{name:'Profile'}"> Profile </router-link></a>
    </li>
    <li class="nav-item">
      <a class="nav-link"><router-link :to="{name:'Bids'}"> Bids </router-link></a>
    </li>
    <li class="nav-item">
      <a class="nav-link"><router-link :to="{name:'Add'}"> Add Item </router-link></a>
    </li>
  </ul>
  </div>
</nav>

  <section class="section">
    <router-view/>
  </section>

  <Footer/>
  
  </div>
</template>


<script>
import { RouterView, RouterLink } from 'vue-router'
import Footer from '@/components/footer.vue'

export default {
  name: 'App',
  components: {
    Footer
  }
}
</script>

<style scoped>
h3{
  color: aliceblue;
}
</style>


