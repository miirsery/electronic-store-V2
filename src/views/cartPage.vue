<template>
  <div>
    <h1 class="mb-4">Cart <span>1 товар</span></h1>
    <div class="cart__wrapper flex justify-between">
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
            <p class="cart__title">{{ product.title }}</p>
            <button @click="remove(product.id)">Удалить товар</button>
          </div>
          <div class="cart__count">
            <button @click="setCnt({ id: product.id, cnt: product.cnt - 1})">
              -
            </button>
            1
            <button @click="setCnt({ id: product.id, cnt: product.cnt + 1})">
              +
            </button>
          </div>
          <div class="cart__price-and-availability">
            <p class="cart__price">{{ product.price }}</p>
            <p class="cart__availability">В наличии: в 1 магазине</p>
          </div>
        </div>
      </div>
      <div class="cart__make-an-order w-1/4">
        <div class="cart__total">{{ cartCnt }} товар на {{ cartTotal }}</div>
        <p class="cart__availability">В наличии: в 1 магазине</p>
        <button
          class="flex items-center justify-center px-6 py-5 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-2 md:text-lg md:px-5"
        >
          Оформить заказ
        </button>
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
      cartCnt: "length"
    })
  },
  methods: {
    ...mapActions("cart", ["setCnt", "remove"])
  }
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
</style>
