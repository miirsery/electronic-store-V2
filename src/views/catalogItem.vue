<template>
  <div>
    <h2 class="title mb-8">{{ category.title }} </h2>
    <hr>
    <div class="container">
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
    </div>
    <hr>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("categories", { categoryProxy: "item" }),
    ...mapGetters("products", { productProxy: "item" }),
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
</style>