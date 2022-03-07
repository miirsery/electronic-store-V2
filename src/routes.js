import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    meta: {
      breadCrumb: "home"
    },
    component: () => import("@/views/home")
  },
  {
    path: "/cart",
    name: "cart",
    meta: {
      breadCrumb: "cart"
    },
    component: () => import("@/views/cartPage")
  },
  {
    path: "/about",
    name: "about",
    meta: {
      breadCrumb: "about"
    },
    component: () => import("@/views/aboutPage")
  },
  {
    path: "/faq",
    name: "faq",
    meta: {
      breadCrumb: "faq"
    },
    component: () => import("@/views/faqPage")
  },
  {
    path: "/catalog",
    name: "catalog",
    meta: {
      breadCrumb: "catalog"
    },
    components: {
      default: () => import("@/views/fullCategories"),
      catalogItem: () => import("@/views/catalogItem")
    }
  },
  {
    path: "/catalog/:id",
    name: "catalogItem",
    meta: {
      breadCrumb: "catalog/:id"
    },
    components: {
      default: import("@/views/catalogItem"),
      catalog: () => import("@/views/fullCategories")
    }
  },
  {
    path: "/product/:id",
    name: "productId",
    meta: {
      breadCrumb: "product/:id"
    },
    component: () => import("@/views/productPage")
  },
  {
    path: "/order",
    name: "order",
    meta: {
      breadCrumb: "order"
    },
    component: () => import("@/views/orderPage")
  },
  {
    path: "/account/settings",
    name: "accountSettings",
    meta: {
      breadCrumb: "accountSettings"
    },
    component: () => import("@/views/accountSettings")
  },
  {
    path: "/password-recovery",
    name: "passwordRecovery",
    meta: {
      breadCrumb: "passwordRecovery"
    },
    component: () => import("@/views/passwordRecovery")
  },
  {
    path: "/:PathMatch(.*)*",
    name: "errorPage",
    meta: {
      breadCrumb: "errorPage"
    },
    component: () => import("@/views/ePage")
  }
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;
