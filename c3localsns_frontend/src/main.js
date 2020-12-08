import { createApp } from "vue";
//import Vue from 'vue'
import App from './App.vue'
import VueCookies from 'vue-cookies'
import DiscordOauth2 from 'discord-oauth2'
import * as VueRouter from 'vue-router';
import router from './router'

const app = createApp(App)

app.use(router, VueRouter, VueCookies, DiscordOauth2) //追記

app.mount("#app");
