import { createStore } from "vuex";
import cart from "@/store/cart";
import categories from "@/store/categories";
export default createStore({
  modules: {
    cart,
    categories
  },
  strict: process.env.NODE_ENV !== "production"
});