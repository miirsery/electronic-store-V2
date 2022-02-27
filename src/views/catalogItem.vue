<template>
  <div>
    <h2 class="title mb-6 mt-6">
      {{ category.title }} <span>{{ filteredProducts.length }}</span>
    </h2>
    <div class="top w-2/3 flex justify-between">
      <a
        @click="$router.go(-1)"
        class="block ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900"
      >Вернуться назад</a
      >
      <div class="sort flex justify-between w-1/6 mr-6">
        <button type="button" @click="toggleDisplayType('detailed')">
          Подробный
        </button>
        <button
          type="button"
          @click="toggleDisplayType('shorted')"
          class="ml-2"
        >
          Краткий
        </button>
      </div>
    </div>
    <hr />
    <form class="filters__top flex">
      <div>по популярности</div>
      <div>по рейтингу</div>
      <div>по отзывам</div>
      <div>по обзорам</div>
      <div>по названию</div>
    </form>
    <div class="container flex w-full">
      <div class="content w-2/3" :class="parentClassObject">
        <div
          class="content__product mb-4 shadow p-4"
          v-for="product in filteredProducts"
          :key="product.title"
          :class="childClassObject"
        >
          <product-slider :product="product" :display-type="displayType" />
          <product-info :product="product" :display-type="displayType" />
        </div>
      </div>
      <aside class="filters pt-2 pl-4 pr-4">
        <!--        <filters />-->
        <form>
          <div class="filters__top flex justify-between">
            <h2 class="filters__title font-bold text-2xl">Фильтры</h2>
            <button class="filters__clear" type="button" @click="clearFilters">
              Отчистить
            </button>
          </div>
          <div>
            <input
              class="filters__input"
              type="text"
              placeholder="Поиск по фильтрам..."
            />
          </div>
          <div class="w-full">
            <div class="values flex justify-between">
              <input
                class="filters__input w-1/3 mr-1"
                type="text"
                :value="minPrice"
              />
              <input
                class="filters__input w-1/3"
                type="text"
                :value="maxPrice"
              />
            </div>
            <div class="range-slider w-full">
              <input
                type="range"
                min="0"
                max="300000"
                step="1000"
                v-model.number="minPrice"
                @change="setChangeSlider"
              />
              <input
                type="range"
                min="0"
                max="300000"
                step="1000"
                v-model.number="maxPrice"
                @change="setChangeSlider"
              />
            </div>
          </div>
          <div class="mb-4">
            <p class="filter__title mb-2">Наличие товара</p>
            <div>
              <input id="availability-pickup" type="checkbox" checked />
              <label class="ml-2" for="availability-pickup"
              >Доступен самовывоз</label
              >
            </div>
            <div>
              <input id="availability-fast-pickup" type="checkbox" />
              <label class="ml-2" for="availability-fast-pickup"
              >Забрать через 15 минут</label
              >
            </div>
          </div>
          <div class="mb-4">
            <p class="filter__title mb-2">Статус товара</p>
            <div>
              <input id="status-installments" type="checkbox" checked />
              <label for="status-installments">Доступно в рассрочку</label>
            </div>
            <div class="mb-4">
              <input id="status-promo" type="checkbox" checked />
              <label for="status-promo">Товары по акции</label>
            </div>
            <div class="mb-4">
              <p class="filter__title mb-2">Товары со скидкой</p>
              <div>
                <input id="promo-any" type="radio" checked name="promo" />
                <label for="promo-any">Любой</label>
              </div>
              <div>
                <input id="promo-five" type="radio" checked name="promo" />
                <label for="promo-five">5% и больше</label>
              </div>
              <div>
                <input id="promo-ten" type="radio" checked name="promo" />
                <label for="promo-ten">10% и больше</label>
              </div>
            </div>
          </div>
        </form>
      </aside>
    </div>
  </div>
  <el-pagination background layout="prev, pager, next" :total="pages * 10" />
  <hr />
</template>

<script>
import { mapGetters } from "vuex";
import ProductSlider from "@/components/ProductSlider";
import ProductInfo from "@/components/ProductInfo";
// import Filters from "@/components/Filters";

export default {
  components: {
    ProductSlider,
    ProductInfo
    // Filters

  },
  data() {
    return {
      minPrice: 0,
      maxPrice: 3000000,
      sortedProducts: [],
      displayType: "detailed",
      shorted: false,
      pages: 1,
      productsPerView: 8
    };
  },
  methods: {
    setChangeSlider() {
      if (this.minPrice > this.maxPrice) {
        let tmp = this.maxPrice;
        this.maxPrice = this.minPrice;
        this.minPrice = tmp;
      }
      this.sortByCategories();
    },
    sortByCategories() {
      let vm = this;
      this.sortedProducts = [...this.products];
      this.sortedProducts = this.sortedProducts.filter(
        (item) => item.price >= vm.minPrice && item.price <= vm.maxPrice
      );
    },
    clearFilters() {
      this.sortedProducts = this.products;
      this.maxPrice = 3000000;
      this.minPrice = 0;
    },
    toggleDisplayType(name) {
      this.displayType = name;
      this.shorted = this.displayType === "shorted";
    },
    totalPages() {
      this.pages = Math.floor(
        this.sortedProducts.length / this.productsPerView + 1
      );
    }
  },
  computed: {
    ...mapGetters("categories", {
      categoryProxy: "item",
      productProxy: "item"
    }),
    ...mapGetters("products", {
      products: "all"
    }),
    id() {
      return this.$route.params.id;
    },
    category() {
      return this.categoryProxy(this.id);
    },
    filteredProducts() {
      if (this.sortedProducts.length) return this.sortedProducts;
      else return this.sortedProducts;
    },
    parentClassObject() {
      return {
        "flex flex-wrap": this.shorted
      };
    },
    childClassObject() {
      return {
        "flex-col": this.shorted
      };
    }

  },
  mounted() {
    this.sortByCategories();
    this.totalPages()
  }

};
</script>

<style scoped lang="sass">

.range-slider
  margin: auto 16px
  text-align: center
  position: relative

  input[type=range]
    position: absolute
    left: 0
    bottom: 0
    width: 90%

    &::-webkit-slider-thumb
      z-index: 2
      position: relative
      top: 2px
      margin-top: -7px

.title
  font-size: 28px
  font-weight: bold


.content
  &__product
    display: flex

    &-img
      max-width: 160px
      height: 260px
      background-color: #f3f3f3

      img
        width: 100%
        height: 100%
        object-fit: cover

.filters
  width: 300px
  background-color: #eaeaea

  &__input
    margin-bottom: 1rem
    border: 0
    background: none

  &__top
    margin: 1rem 0

    div
      font-size: 0.8rem
      margin-right: 1rem
      cursor: pointer
      color: rgba(0, 0, 0, 0.7)
      font-weight: bold

      &:hover
        color: #000
</style>
