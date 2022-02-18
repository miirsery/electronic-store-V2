export default {
  namespaced: true,
  state: {
    items: tmpProducts()
  },
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

function tmpProducts() {
  return [
    {
      id: 1,
      title: "IPhone XYN 10",
      price: 19999,
      imgUrl: require("../assets/products/1.jpg"),
      url: "/iphone-xyn-10-rand001",
      description: "Этот телефон такой-то такой. Мне очень нравится данная модель. Настоятельно не рекомендую к покупке.",
      smallImages: [
        {
          id: 1,
          img: require("../assets/products/carousel/1.jpg")
        },
        {
          id: 2,
          img: require("../assets/products/carousel/2.jpg")
        },
        {
          id: 3,
          img: require("../assets/products/carousel/3.jpg")
        },
        {
          id: 4,
          img: require("../assets/products/carousel/4.jpg")
        },
        {
          id: 5,
          img: require("../assets/products/carousel/5.jpg")
        },
        {
          id: 6,
          img: require("../assets/products/carousel/6.jpg")
        }
      ],
      specifications: [
        {
          os: "Операционная система Android 21",
          display: "Дисплей 6.17\", IPS",
          resolution: "1400x1080",
          processor: "Qualcomm Snapdragon 860, 2960МГц, 0-ми ядерный",
          ram: "Объем оперативной памяти 18 ГБ",
          rom: "Объем встроенной памяти 2526 ГБ"
        }
      ]
    },
    {
      id: 2,
      title: "Redmi XZ 1011",
      price: 39999,
      imgUrl: require("../assets/products/2.jpg"),
      url: "/redmi-xz-1001-rand002",
      description: "Этот телефон такой-то такой. Мне очень нравится данная модель. Настоятельно не рекомендую к покупке.",
      specifications: [
        {
          os: "Операционная система Android 11",
          display: "Дисплей 6.67\", IPS",
          resolution: "2400x1080",
          processor: "Qualcomm Snapdragon 860, 2960МГц, 8-ми ядерный",
          ram: "Объем оперативной памяти 8 ГБ",
          rom: "Объем встроенной памяти 256 ГБ"
        }
      ]
    },
    {
      id: 3,
      title: "Redmi XZY 11",
      price: 92999,
      imgUrl: require("../assets/products/3.jpg"),
      url: "/redmi-xzy-11-rand003",
      description: "Этот телефон такой-то такой. Мне очень нравится данная модель. Настоятельно не рекомендую к покупке."
    },
    {
      id: 4,
      title: "IPhone Kakoi-to 11",
      price: 9399,
      imgUrl: require("../assets/products/4.jpg"),
      url: "/iphone-kakoi-to-11-rand004",
      description: "Этот телефон такой-то такой. Мне очень нравится данная модель. Настоятельно не рекомендую к покупке."
    },
    {
      id: 5,
      title: "IPhone Kakoi-to 12",
      price: 29999,
      imgUrl: require("../assets/products/5.jpg"),
      url: "/iphone-kakoi-to-12-rand005",
      description: "Этот телефон такой-то такой. Мне очень нравится данная модель. Настоятельно не рекомендую к покупке."
    }
  ];
}