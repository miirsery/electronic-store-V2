import { createRouter, createWebHistory } from "vue-router";
import FullCategoriesPage from "@/views/fullCategories";
import CatalogItemPage from "@/views/catalogItem";
import HomePage from "@/views/home";
import CartPage from "@/views/cartPage";

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
    path: "/:PathMatch(.*)*",
    name: "error"
  }
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;
