export default {
  namespaced: true,
  state: {
    user: {
      id: "",
      username: "",
      avatar: require("../assets/avatar.png")
    },
    isAuth: false
  },
  mutations: {
    SET_USER(state, payload) {
      state.user = payload;
    },
    DELETE_USER(state) {
      state.user = {};
    },
    IS_AUTH(state, payload) {
      state.isAuth = payload;
    },
    CHANGE_AVATAR(state, payload) {
      state.user.avatar = payload;
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
    },
    changeAvatar({ commit }, payload) {
      commit("CHANGE_AVATAR", payload);
    }
  }
};
