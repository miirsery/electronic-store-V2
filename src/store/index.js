import { createStore } from "vuex";
import cart from "@/store/cart";
import categories from "@/store/categories";
import products from "@/store/products";
import fullCategories from "@/store/fullCategories";
import { LOADING_SPINNER_SHOW_MUTATIONS } from "@/store/constants";

export default createStore({
  modules: {
    cart,
    categories,
    products,
    fullCategories
  },
  state() {
    return {
      showLoading: false,
    };
  },

  mutations: {
    [LOADING_SPINNER_SHOW_MUTATIONS](state, payload) {
      state.showLoading = payload;
    },
  },
  strict: process.env.NODE_ENV !== "production"
});