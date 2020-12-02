import { createApp } from "vue";
//import Vue from 'vue'
import App from './App.vue'
import axios from 'axios' //追記
import VueAxios from 'vue-axios' //追記
import VueCookies from 'vue-cookies'
import DiscordOauth2 from 'discord-oauth2'
import VueRouter from 'vue-router';

const app = createApp(App)

app.use(VueAxios, axios, VueCookies, DiscordOauth2, VueRouter) //追記

app.mount("#app");


  
  

