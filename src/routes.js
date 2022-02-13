import { createRouter, createWebHistory } from "vue-router";

import FullCategoriesPage from "@/views/fullCategories";
import CatalogItemPage from "@/views/catalogItem";
import HomePage from "@/views/home";
import CartPage from "@/views/cartPage";
import productPage from "@/views/productPage";
import ErrorPage from '@/views/ePage'
const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage
  },
  {
    path: "/cart",
    name: "cart",
    component: CartPage
  },
  {
    path: "/catalog",
    name: "catalog",
    components: {
      default: FullCategoriesPage,
      catalogItem: CatalogItemPage
    }
  },
  {
    path: "/catalog/:id",
    name: "catalogItem",
    components: {
      default: CatalogItemPage,
      catalog: FullCategoriesPage
    }
  },
  {
    path: "/product/:id",
    name: "productId",
    component: productPage
  },
  {
    path: "/:PathMatch(.*)*",
    name: "errorPage",
    component: ErrorPage
  }
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;
