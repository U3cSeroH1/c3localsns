import { createApp } from "vue";
//import Vue from 'vue'
import App from './App.vue'
import axios from 'axios' //追記
import VueAxios from 'vue-axios' //追記
import VueCookies from 'vue-cookies'


const app = createApp(App)

app.use(VueAxios, axios, VueCookies) //追記

app.mount("#app");


  
  

