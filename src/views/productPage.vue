<template>
  <div>
    <a @click="$router.go(-1)" class="ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900">Вернуться
      назад</a>
    <hr>
    <div class="content">
      <div v-for="item in products" :key="item.title">
        <div v-if="item.url.slice(1) === id" class="product">
          <div class="product__hero">
            <div class="product__img-block mr-10">
              <div class="product__img">
                <img :src="item.imgUrl" :alt="item.title">
              </div>
              <div class="product__img-bottom">
                <div class="product__img-bottom-item">
                  <img :src="item.imgUrl" :alt="item.title">
                </div>
                <div class="product__img-bottom-item">
                  <img :src="item.imgUrl" :alt="item.title">
                </div>
                <div class="product__img-bottom-item">
                  <img :src="item.imgUrl" :alt="item.title">
                </div>
                <div class="product__img-bottom-item">
                  <img :src="item.imgUrl" :alt="item.title">
                </div>
                <div class="product__img-bottom-item">
                  <img :src="item.imgUrl" :alt="item.title">
                </div>
              </div>
            </div>
            <div class="product__info">
              <h2 class="product__title mt-2 text-2xl leading-8 tracking-tight text-gray-900 sm:text-2xl">
                {{ item.title }}</h2>
              <div class="price mt-4">
                <p class="price__bonus ">+270</p>
                <p class="price__count md:text-2xl">26 990</p>
              </div>
              <button
                class="flex items-center justify-center px-6 py-5 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-2 md:text-lg md:px-5">
                В корзину
              </button>
              <div class="delivery">
                <p><a href="/" class="text-indigo-600">Доставка </a>будет в такие-то дни</p>
                <p class="text-sm max-w-2xl">Можно забрать самому. Но тут всякие очереди, сам понимаешь, что будешь
                  дольше. Ну и нам денюшка капнет. Закажи лучше, плз))0)</p>
              </div>
            </div>
          </div>
          <div class="characteristics">
            <nav class="mt-4">
              <ul>
                <li class="ml-2">
                  <a href="/" class="opacity-70 hover:opacity-100">О товаре</a>
                </li>
                <li class="ml-2">
                  <a href="/" class="opacity-70 hover:opacity-100">Характеристики</a>
                </li>
                <li class="ml-2">
                  <a href="/" class="opacity-70 hover:opacity-100">Аксессуары</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("products", { productProxy: "item" }),
    ...mapGetters("products", { products: "all" }),
    id() {
      return this.$route.params.id;
    }

  }
};
</script>

<style scoped lang="sass">
.product
  &__hero
    display: flex

  &__img
    max-width: 300px

    img
      width: 100%
      object-fit: cover

    &-bottom
      display: flex
      justify-content: space-between
      width: 100%

      &-item
        width: 50px
        height: 55px

.characteristics
  nav
    ul
      display: flex
</style>