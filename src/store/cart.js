export default {
  namespaced: true,
  state: {
    items: []
  },
  getters: {
    length: (state) => state.items.length,
    has: (state) => (id) => state.items.some((pr) => pr.id === id),
    productsDetailed(state, getters, rootState, rootGetters) {
      return state.items.map((pr) => {
        let info = rootGetters["products/item"](pr.id);
        return { ...pr, ...info };
      });
    },
    total: (state, getters) =>
      getters.productsDetailed.reduce((t, pr) => t + pr.price * pr.cnt, 0)
  },
  mutations: {
    add(state, id) {
      state.items.push({ id, cnt: 1 });
    },
    remove(state, id) {
      state.items = state.items.filter((pr) => pr.id !== id);
    },
    setCnt(state, { id, cnt }) {
      let i = state.items.findIndex((pr) => pr.id === id);
      state.items[i].cnt = Math.max(1, cnt)
    }
  },
  actions: {
    add(store, id) {
      if (!store.getters.has(id)) store.commit("add", id);
    },
    remove(store, id) {
      if (store.getters.has(id)) store.commit("remove", id);
    },
    setCnt(store, payload) {
      if (store.getters.has(payload.id)) store.commit("setCnt", payload);
    }
  }
};
