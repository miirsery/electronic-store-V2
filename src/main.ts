import { createApp } from "vue";
import routes from "@/routes";
import ElementPlus from "element-plus";
import VueLazyLoad from "vue3-lazyload";
import api from "@/api/index";
import store from "./store/index";
import loadPlugin from "@/plugins/load";

import "element-plus/dist/index.css";
import "@/assets/tailwind.css";
import "@/assets/sass/main.sass";

import App from "./App.vue";

const app = createApp(App);
app.use(store);
app.use(ElementPlus);
app.use(VueLazyLoad, {
  loading: "@/assets/loading.png"
});
app.config.globalProperties.$api = api;
app.config.globalProperties.$load = loadPlugin;
app.use(routes);
app.mount("#app");
