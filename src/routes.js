import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/home")
  },
  {
    path: "/cart",
    name: "cart",
    component: () => import("@/views/cartPage")
  },
  {
    path: "/catalog",
    name: "catalog",
    components: {
      default: () => import("@/views/fullCategories"),
      catalogItem: () => import("@/views/catalogItem")
    }
  },
  {
    path: "/catalog/:id",
    name: "catalogItem",
    components: {
      default: import("@/views/catalogItem"),
      catalog: () => import("@/views/fullCategories")
    }
  },
  {
    path: "/product/:id",
    name: "productId",
    component: () => import("@/views/productPage")
  },
  {
    path: "/order",
    name: "order",
    component: () => import("@/views/orderPage")
  },
  {
    path: "/:PathMatch(.*)*",
    name: "errorPage",
    component: () => import("@/views/ePage")
  }
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;
