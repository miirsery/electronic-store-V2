export default {
  namespaced: true,
  state: {
    items: tmpCategories(),
  },
  getters: {
    all: (state) => state.items,
    itemsMap(state) {
      const map = {};
      state.items.forEach((pr, index) => {
        map[pr.id.toString()] = index;
      });
      return map;
    },
    item: (state, getters) => (id) => state.items[getters.itemsMap[id]],
  },
  mutations: {},
  actions: {},
};

function tmpCategories() {
  return [
    {
      id: "phones",
      title: "Телефоны",
      url: "/catalog/phones",
    },
    {
      id: "laptops",
      title: "Ноутбуки и компьютеры",
      url: "/catalog/laptops",
    },
    {
      id: "photo-and-video",
      title: "Фото и видео",
      url: "/catalog/photo-and-video",
    },
    {
      id: "products-for-auto",
      title: "Товары для авто",
      url: "/catalog/products-for-auto",
    },
    {
      id: "products-for-home",
      title: "Техника для дома",
      url: "/catalog/products-for-home",
    },
    {
      id: "products-for-home",
      title: "Техника для дома",
      url: "/catalog/products-for-home",
    },
    {
      id: "products-for-home",
      title: "Техника для дома",
      url: "/catalog/products-for-home",
    },
  ];
}
