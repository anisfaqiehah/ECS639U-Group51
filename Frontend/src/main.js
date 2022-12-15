import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './plugins/router'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

createApp(App).use(router).mount('#app')
