export default {
  namespaced: true,
  state: {},
  getters: {
    all: state => state.items,
    itemsMap(state) {
      let map = {};
      state.items.forEach((pr, index) => {
        map[pr.id.toString()] = index;
      });
      return map;
    },
    item: (state, getters) => id => state.items[getters.itemsMap[id]]
  },
  mutations: {},
  actions: {}
};

