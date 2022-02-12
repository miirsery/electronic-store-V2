import { createStore } from "vuex";
import cart from "@/store/cart";
import categories from "@/store/categories";
import products from "@/store/products";
export default createStore({
  modules: {
    cart,
    categories,
    products
  },
  strict: process.env.NODE_ENV !== "production"
});