import api from "@/components/api/index";

export default {
  install(Vue) {
    Vue.prototype.$api = api;
  }
};

