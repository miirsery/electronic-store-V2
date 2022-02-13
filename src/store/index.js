import { createStore } from "vuex";
import cart from "@/store/cart";
import categories from "@/store/categories";
import products from "@/store/products";
import fullCategories from "@/store/fullCategories";
export default createStore({
  modules: {
    cart,
    categories,
    products,
    fullCategories
  },
  strict: process.env.NODE_ENV !== "production"
});