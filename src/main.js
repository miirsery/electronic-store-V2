import { createApp } from "vue";
import routes from "@/routes";
import App from "./App.vue";
import loader from "vue-ui-preloader";
import "@/assets/tailwind.css";
import "@/assets/sass/global.sass";
import store from "./store/index";

const app = createApp(App);
app.use(loader);
app.use(store);
app.use(routes);
app.mount("#app");
