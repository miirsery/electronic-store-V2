<template>
  <div>
    <div class="content__product-info" v-if="displayType === 'detailed' ">
      <h2 class="product__title">{{ product.title }}</h2>
      <hr />
      <div class="product-info">
        <div v-for="(value, index) in product.specifications" :key="index">
          <div v-for="spec in value" :key="spec" class="product-info__item">
            {{ spec }}
          </div>
        </div>
      </div>
      <router-link :to="`/product${product.url}`" class="product__link">Подробнее</router-link>
    </div>
    <router-link :to="`/product${product.url}`" class="content__product-info-short" v-if="displayType === 'shorted'">
      <h2 class="product-short__title">{{ product.title }}</h2>
      <hr>
      <p class="product-short__price flex justify-between">
        {{ product.price }}
        <button type="button">Add to cart</button>
      </p>
    </router-link>
  </div>
</template>
<script>
export default {
  props: {
    product: Object,
    displayType: String
  }
};
</script>

<style scoped lang="sass">
.product
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

  &__title
    font-size: 1.5rem
    font-weight: bold
    padding: 0.5em 0

  &-info
    &__item
      margin-bottom: 0.5rem

      &:first-child
        margin-top: 0.5rem

      &:last-child
        font-size: 1.1rem
        font-weight: bold
        position: relative

        &::before
          content: 'Цена'
          left: 0
          top: 0
          margin-right: 0.5rem
</style>