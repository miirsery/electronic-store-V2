<template>
  <div>
    <h2 class="title mb-8">{{ category.title }}</h2>
    <a
      @click="$router.go(-1)"
      class="ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900"
    >Вернуться назад</a>
    <hr />
    <div class="container flex w-full">
      <div class="content w-2/3">
        <div
          class="content__product mb-4 shadow p-4"
          v-for="product in products"
          :key="product.title"
        >
          <product-slider :product="product" />
          <div class="content__product-info">
            <h2 class="product__title">{{ product.title }}</h2>
            <hr />
            <div class="product-info">
              <div v-for="(value, index) in product.specifications" :key="index">
                <div v-for="spec in value" :key="spec" class="product-info__item">
                  {{ spec }}
                </div>
              </div>
            </div>
            <router-link :to="`/product${product.url}`" class="catalog__link">Подробнее</router-link>
          </div>
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
          <div class="flex w-full justify-between">
            <input class="w-1/3 mr-1" type="text" value="1500" />
            <input class="w-1/3" type="text" value="1000" />
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
    <hr />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import ProductSlider from "@/components/ProductSlider";

export default {
  components: {
    ProductSlider
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
    }
  }
};
</script>

<style scoped lang="sass">
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
