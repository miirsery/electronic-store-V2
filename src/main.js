import { createApp } from "vue";
import routes from "@/routes";
import App from "./App.vue";
import VueLazyLoad from "vue3-lazyload";
// import ApiPlugin from "@/plugins/api";
import "@/assets/tailwind.css";
import "@/assets/sass/main.sass";
import store from "./store/index";

const app = createApp(App);
app.use(store);
app.use(VueLazyLoad, {
  loading: "@/assets/loading.png"
});
// app.use(ApiPlugin)
app.use(routes);
app.mount("#app");
