import { createRouter, createWebHistory } from "vue-router";
import FullCategoriesPage from "@/views/fullCategories";
import CatalogItemPage from "@/views/catalogItem";

const routes = [
  {
    path: "/",
    name: "home",
  },
  {
    path: "/catalog",
    name: "catalog",
    components: {
      default: FullCategoriesPage,
      catalogItem: CatalogItemPage,
    },
  },

  {
    // path: '/:PathMatch(.*)*',
    path: "/catalog/:id",
    name: "catalogItem",
    components: {
      default: CatalogItemPage,
      catalog: FullCategoriesPage,
    },
  },
  {
    // path: '/:PathMatch(.*)*',
    path: "/product/:id",
    name: "product",
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router;
