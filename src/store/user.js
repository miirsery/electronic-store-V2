export default {
  namespaced: true,
  state: {
    user: null,
    isAuth: false,
  },
  getters: {
    getUser(state) {
      return state.user;
    }
  },
  mutations: {
    SET_USER(state, payload) {
      state.user = payload;
    },
    DELETE_USER(state) {
      state.user = null;
    },
    IS_AUTH(state, payload) {
      state.isAuth = payload;
    }
  },
  actions: {
    setUser({ commit }, payload) {
      commit("SET_USER", payload);
    },
    deleteUser({ commit }) {
      commit("DELETE_USER");
    },
    IS_AUTH({ commit }, payload) {
      commit("IS_AUTH", payload);
    }
  }
};
