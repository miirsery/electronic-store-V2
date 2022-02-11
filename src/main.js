import { createApp } from "vue";
import routes from "@/routes";
import App from "./App.vue";
import "@/assets/tailwind.css";
import "@/assets/sass/global.sass";
import store from "./store/index";

const app = createApp(App);
app.use(store);
app.use(routes);
app.mount("#app");
