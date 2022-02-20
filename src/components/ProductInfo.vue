<template>
  <div>
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
</template>
<script>
export default {
  props: {
    product: Object
  }
};
</script>

<style scoped>

</style>