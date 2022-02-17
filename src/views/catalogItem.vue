<template>
  <div>
    <h2 class="title mb-8">{{ category.title }} </h2>
    <hr>
    <div class="container flex w-full">
      <div class="content">
        <div class="content__product mb-4 shadow" v-for="product in products" :key="product.title">
          <div class="content__product-img">
            <img v-lazy="{src: product.imgUrl, loading: 'Loading...', error: 'Error load'}" :alt="product.title">
          </div>
          <div class="content__product-info">
            <h2>{{ product.title }}</h2>
            <hr>
            <p>{{ product.description }}</p>
            <router-link :to="`/product${product.url}`">Watch</router-link>
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
              <label class="ml-2" for="availability-pickup">Доступен самовывоз</label>
            </div>
            <div>
              <input id="availability-fast-pickup" type="checkbox" />
              <label class="ml-2" for="availability-fast-pickup">Забрать через 15 минут</label>
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
                <input id="promo-any" type="radio" checked name="promo">
                <label for="promo-any">Любой</label>
              </div>
              <div>
                <input id="promo-five" type="radio" checked name="promo">
                <label for="promo-five">5% и больше</label>
              </div>
              <div>
                <input id="promo-ten" type="radio" checked name="promo">
                <label for="promo-ten">10% и больше</label>
              </div>
            </div>
          </div>
        </form>
      </aside>
    </div>
    <hr>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("categories", { categoryProxy: "item", productProxy: "item" }),
    ...mapGetters("products", { products: "all" }),
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
</style>