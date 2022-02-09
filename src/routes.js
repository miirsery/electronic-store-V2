import { createRouter, createWebHashHistory } from "vue-router";
import FullCategoriesPage from "@/views/fullCategories";
const routerHistory = createWebHashHistory();
const routes = createRouter({
  history: routerHistory,
  routes: [
    {
      path: "/",
      name: "home"
    },
    {
      path: "/categories",
      name: "categories",
      component: FullCategoriesPage
    },

  ]

});
export default routes;