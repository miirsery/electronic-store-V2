<template>
  <div>
    <h2 class="title mb-8">{{ category.title }}</h2>
    <a
      @click="$router.go(-1)"
      class="ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900"
    >Вернуться назад</a
    >
    <hr />

    <div class="container flex w-full">
      <div class="content w-2/3">
        <div
          class="content__product mb-4 shadow p-4"
          v-for="product in filteredProducts"
          :key="product.title"
        >
          <product-slider :product="product" />
          <product-info :product="product" />
        </div>
      </div>
      <aside class="filters pt-2 pl-4 pr-4">
        <form>
          <div class="filters__top flex justify-between">
            <h2 class="filters__title font-bold text-2xl">Фильтры</h2>
            <button class="filters__clear">Отчистить</button>
          </div>
          <div>
            <input type="text" placeholder="Поиск по фильтрам..." />
          </div>
          <div class="w-full">
            <div class="values flex">
              <input class="w-1/3 mr-1" type="text" :value="minPrice" />
              <input class="w-1/3" type="text" :value="maxPrice" />
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
            <div class="range-values">
              <p>Min: {{ minPrice }}</p>
              <p>Max: {{ maxPrice }}</p>
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
  <hr />
</template>

<script>
import { mapGetters } from "vuex";
import ProductSlider from "@/components/ProductSlider";
import ProductInfo from "@/components/ProductInfo";

export default {
  components: {
    ProductSlider,
    ProductInfo
  },

  data() {
    return {
      minPrice: 0,
      maxPrice: 3000000,
      sortedProducts: []
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
      this.sortedProducts = this.sortedProducts.filter(item => item.price >= vm.minPrice && item.price <= vm.maxPrice);
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
      else return null;
    }
  },
  mounted() {
    this.sortByCategories();
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

    &::-webkit-slider-thumb
      z-index: 2
      position: relative
      top: 2px
      margin-top: -7px

.title
  font-size: 28px
  font-weight: bold

.catalog
  &__link
    font-size: 18px
    background-color: #50a0cd
    color: #ffffff
    margin-top: 1rem
    display: block
    max-width: 35%
    text-align: center
    padding: 0.5rem 0
    text-transform: uppercase
    transition: all 0.3s
    border-radius: 5px

    &:hover
      background-color: #4687af

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

.product
  &__title
    font-size: 1.5rem
    font-weight: bold
    padding: 0.5em 0

  &-info
    &__item
      margin-bottom: 0.5rem

      &:first-child
        margin-top: 0.5rem

</style>
