<template>
  <div>
    <div v-if="products.length === 0" class="empty-cart">
      <div class="empty-cart__wrapper">
        <h2 class="empty-cart__title mb-4 font-bold">В корзине нет товаров</h2>
        <div class="search mb-4">
          Воспользуйтесь
          <span class="underline text-blue-400">
            <span class="cursor-pointer">поиском</span>
          </span>
        </div>
        <div>
          Или же
          <span>
            <router-link to="/catalog" class="underline text-blue-400">
              вернитесь к категориям
            </router-link>
          </span>
        </div>
      </div>
    </div>
    <div v-else class="cart__wrapper flex justify-between">
      <div class="cart__content w-2/3">
        <div
          v-for="product in products"
          :key="product.id"
          class="cart-item flex justify-between mb-4 border-gray-100 shadow p-5 rounded-2xl"
        >
          <div class="cart__img mr-4">
            <img :src="product.imgUrl" :alt="product.title" />
          </div>
          <div class="cart__title-block">
            <p class="cart__title mb-4">{{ product.title }}</p>
            <button @click="remove(product.id)">Удалить товар</button>
          </div>
          <div class="cart__count flex items-center">
            <button
              class="mr-4"
              @click="setCnt({ id: product.id, cnt: product.cnt - 1 })"
            >
              -
            </button>
            {{ product.cnt }}
            <button
              class="ml-4"
              @click="setCnt({ id: product.id, cnt: product.cnt + 1 })"
            >
              +
            </button>
          </div>
          <div class="cart__price-and-availability">
            <p class="cart__price">{{ product.price * product.cnt }} ₽</p>
            <p class="cart__availability">В наличии: в 1 магазине</p>
          </div>
        </div>
      </div>
      <div class="cart__make-an-order w-1/4">
        <div class="cart__total">{{ cartCnt }} товар на {{ cartTotal }}</div>
        <p class="cart__availability">В наличии: в 1 магазине</p>
        <router-link
          class="order-btn block font-bold uppercase text-white bg-indigo-400 ml-auto mr-auto mt-4 pt-1 pb-1 pl-2 pr-2"
          to="/order"
        >
          Оформить заказ
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters("cart", {
      products: "productsDetailed",
      cartTotal: "total",
      cartCnt: "length",
    }),
  },
  methods: {
    ...mapActions("cart", ["setCnt", "remove"]),
  },
};
</script>

<style scoped lang="sass">
.cart
  &__img
    width: 120px
    height: 85px

    img
      height: 100%
      object-fit: cover

.order-btn
  max-width: 60%
  text-align: center

.empty-cart
  position: absolute
  left: 50%
  top: 50%
  transform: translate(-50%, -50%)

  &__title
    font-size: 1.5rem

  &__wrapper
    text-align: center
</style>
