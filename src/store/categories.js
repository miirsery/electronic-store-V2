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
      title: "Телефоны и гаджеты",
      imgUrl: require("../assets/phone.svg"),
      url: "/catalog/phones",
      subcategories: [
        {
          title: "Смартфоны, мобильные телефоны",
          items: [
            {
              title: "Смартфоны",
            },
            {
              title: "Новинки",
            },
            {
              title: "Кнопочные телефоны",
            },
            {
              title: "Аксессуары для телефонов",
            },
            {
              title: "Домашние телефоны",
            },
            {
              title: "Радиостанции",
            },
          ],
        },
        {
          title: "Планшеты",
          items: [
            {
              title: "Apple iPad",
            },
            {
              title: "Планшеты Sasung",
            },
            {
              title: "Планшеты Huiwei",
            },
            {
              title: "Планшеты на Anduxa",
            },
            {
              title: "Аксессуары для планшетов",
            },
          ],
        },
      ],
    },
    {
      id: "laptops",
      title: "Ноутбуки и компьютеры",
      imgUrl: require("../assets/laptop.svg"),
      url: "/catalog/laptops",
    },
    {
      id: "photo-and-video",
      title: "Фото и видео",
      imgUrl: require("../assets/camera.svg"),
      url: "/catalog/photo-and-video",
    },
    {
      id: "products-for-auto",
      title: "Товары для авто",
      imgUrl: require("../assets/car.svg"),
      url: "/catalog/products-for-auto",
    },
    {
      id: "products-for-home",
      title: "Техника для дома",
      imgUrl: require("../assets/home.svg"),
      url: "/catalog/products-for-home",
    },
  ];
}
