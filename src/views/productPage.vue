<template>
  <div>
    <div class="product-breadcrumbs">
      <router-link :to="{ name: 'home' }">Home</router-link>
      /
      <router-link to="/catalog/phones">каталог</router-link>
    </div>
    <a
      @click="$router.go(-1)"
      class="ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900"
    >
      Вернуться назад
    </a>
    <hr />
    <div class="content">
      <div v-for="item in products" :key="item.title">
        <div v-if="item.url.slice(1) === id" class="product">
          <div class="product__hero flex">
            <div class="product__img-block mr-10 max-w-sm">
              <div class="product__img">
                <img :src="item.imgUrl" :alt="item.title" />
              </div>
              <div class="product__img-bottom flex justify-between w-full">
                <small-image-swiper :item="item" />
              </div>
            </div>
            <div class="product__info">
              <h2
                class="product__title mt-2 text-2xl leading-8 tracking-tight text-gray-900 sm:text-2xl"
              >
                {{ item.title }}
              </h2>
              <div class="price mt-4">
                <p class="price__bonus text-gray-400 font-light mb-4">
                  +270 бонусов
                </p>
                <p class="price__count md:text-3xl mb-6">{{ item.price }} ₽</p>
              </div>
              <button
                v-if="inCart(item.id)"
                @click="removeFromCart(item.id)"
                class="mb-8 items-center justify-center px-6 py-5 border border-transparent text-base font-medium rounded-md text-white bg-indigo-400 hover:bg-indigo-700 md:py-2 md:text-lg md:px-5"
              >
                Убрать из корзины
              </button>
              <button
                v-else
                @click="addToCart(item.id)"
                class="mb-8 flex items-center justify-center px-6 py-5 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-2 md:text-lg md:px-5"
              >
                В корзину
              </button>
              <div class="delivery">
                <p>
                  <a href="/" class="text-indigo-600">Доставка </a>будет в
                  такие-то дни
                </p>
                <p class="text-sm max-w-2xl mt-4">
                  Можно забрать самому. Но тут всякие очереди, сам понимаешь,
                  что будешь дольше. Ну и нам денюшка капнет. Закажи лучше,
                  плз))0)
                </p>
              </div>
            </div>
          </div>
          <div class="characteristics">
            <div class="characteristics__tabs">
              <nav class="mt-4 mb-8 mt-8">
                <ul class="flex flex-wrap -mb-px">
                  <li class="mr-2" role="presentation">
                    <button
                      class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300"
                      type="button"
                      @click="toggleTabs(1)"
                      :class="{
                        'text-gray-400': openTab !== 1,
                        'text-gray-600': openTab === 1,
                      }"
                    >
                      О товаре
                    </button>
                  </li>
                  <li class="mr-2" role="presentation">
                    <button
                      class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300 active"
                      type="button"
                      @click="toggleTabs(2)"
                      :class="{
                        'text-gray-400': openTab !== 1,
                        'text-gray-600': openTab === 1,
                      }"
                    >
                      Характеристики
                    </button>
                  </li>
                  <li class="mr-2" role="presentation">
                    <button
                      class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300"
                      type="button"
                      @click="toggleTabs(3)"
                      :class="{
                        'text-gray-400': openTab !== 1,
                        'text-gray-600': openTab === 1,
                      }"
                    >
                      Аксессуары
                    </button>
                  </li>
                  <li role="presentation">
                    <button
                      class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300"
                      type="button"
                      @click="toggleTabs(4)"
                      :class="{
                        'text-gray-400': openTab !== 1,
                        'text-gray-600': openTab === 1,
                      }"
                    >
                      Услуги
                    </button>
                  </li>
                </ul>
              </nav>
            </div>
            <div class="characteristics__content">
              <div
                class="about-product bg-gray-100"
                :class="{ hidden: openTab !== 1, block: openTab === 1 }"
              >
                <div class="characteristics__content-main flex">
                  <div class="characteristics__content-title mr-16">
                    <p class="sm:text-2xl">Основное</p>
                    <a href="/">Все характеристики</a>
                  </div>
                  <div class="about-product-title mr-10">
                    <p>Операционная система</p>
                    <p>Дисплей</p>
                    <p>Разрешение дисплея</p>
                  </div>
                  <div class="about-product-value">
                    <p>Android 11</p>
                    <p>6.67", IPS</p>
                    <p>2400x1080</p>
                  </div>
                </div>
                <div class="characteristics__content-description"></div>
                <div class="characteristics__content-reviews"></div>
              </div>
              <div
                class="characteristics"
                :class="{ hidden: openTab !== 2, block: openTab === 2 }"
              >
                <div class="characteristics__item mb-8">
                  <h2 class="characteristics__title mb-4">
                    Общие характеристики
                  </h2>
                  <div class="characteristics__item-w flex">
                    <div class="characteristics__item-title mr-10">
                      <p>Класс</p>
                      <p>Тип корпуса</p>
                      <p>Технология GSM 850</p>
                      <p>Технология GSM 900/1800</p>
                      <p>Технология GSM 1900</p>
                      <p>Технология 3G</p>
                      <p>Технология 4G (LTE)</p>
                    </div>
                    <div class="characteristics__item-value">
                      <p>смартфон</p>
                      <p>моноблок</p>
                      <p>есть</p>
                      <p>есть</p>
                      <p>есть</p>
                      <p>есть</p>
                      <p>есть</p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="accessories"
                :class="{ hidden: openTab !== 3, block: openTab === 3 }"
              >
                accessories
              </div>
              <div class="characteristics__content-description"></div>
              <div class="characteristics__content-reviews"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import SmallImageSwiper from "@/components/SmallImage-Swiper";

export default {
  name: "buttons",
  components: { SmallImageSwiper },
  data() {
    return {
      openTab: 1
    };
  },
  methods: {
    toggleTabs(tabNumber) {
      this.openTab = tabNumber;
    },
    ...mapActions("cart", { addToCart: "add", removeFromCart: "remove" })
  },
  computed: {
    ...mapGetters("products", { products: "all" }),
    ...mapGetters("cart", { inCart: "has" }),
    id() {
      return this.$route.params.id;
    },
    showCart() {
      return this.items;
    }
  }
};
</script>

<style scoped lang="sass">
.product
  &__img
    max-width: 300px

    img
      width: 100%
      object-fit: cover

    &-bottom
      &-item
        width: 50px
        height: 55px

.button
  margin-bottom: 2rem

.price
  &__bonus
    font-size: 14px
</style>
