import { createRouter, createWebHashHistory } from "vue-router";
import FullCategoriesPage from "@/views/fullCategories";
import CatalogItemPage from "@/views/catalogItem";

const routerHistory = createWebHashHistory();
const routes = createRouter({
  history: routerHistory,
  routes: [
    {
      path: "/",
      name: "home"
    },
    {
      path: "/catalog",
      name: "catalog",
      components: {
        default: CatalogItemPage,
        catalogItem: FullCategoriesPage
      }
    },

    {
      // path: '/:PathMatch(.*)*',
      path: "/catalog/:catalogAlias",
      name: "catalogItem",
      components: {
        default: FullCategoriesPage,
        catalog: CatalogItemPage
      }
    },
    {
      // path: '/:PathMatch(.*)*',
      path: "/product/:productAlias",
      name: "product"
    }
  ]

});
export default routes;