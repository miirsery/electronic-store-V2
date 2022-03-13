export default {
  namespaced: true,
  state: {
    user: {
      id: "",
      username: "",
      avatar: require("../assets/avatar.png"),
      avatarFile: null,
      selectedFile: null
    },
    isAuth: false,
    isCrop: false
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
    SET_AVATAR_FILE(state, payload) {
      state.user.avatarFile = payload;
    },
    SET_IMAGE_FILE(state, payload) {
      state.user.selectedFile = payload
    },
    TOGGLE_CROP(state, payload) {
      state.isCrop = payload;
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
    setAvatarFile({ commit }, payload) {
      commit("SET_AVATAR_FILE", payload);
    }
  }
};
