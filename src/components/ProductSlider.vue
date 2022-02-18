<template>
  <div
    v-for="(item, index) in products"
    :key="index"
    class="product-slider-wrapper"
  >
    <article class="product">
      <div class="product__image">
        <div class="product__switch image-switch">
          <div
            class="image-switch__item"
            v-for="(img, i_index) in item.smallImages"
            :key="i_index"
          >
            <div class="image-switch__img">
              <img :src="img.img" :alt="item.title">
            </div>
          </div>
        </div>
      </div>
      <ul class="product__image-pagination image-pagination" aria-hidden="true">
        <li class="image-pagination__item"></li>
      </ul>
    </article>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  methods: {
    pagination() {
      console.log(this.products);
    }
  },
  computed: {
    ...mapGetters("products", { productProxy: "item", products: "all" })
  }
};
</script>

<style scoped lang="sass">
.product
  width: 100%
  height: 100%
  position: relative

  &__image
    position: relative
    display: block
    height: 220px
    overflow: hidden

.image-switch
  position: absolute
  left: 0
  top: 0
  z-index: 20
  width: 100%
  height: 100%
  display: flex

  &__item
    flex-grow: 1
    cursor: pointer
    text-align: center

  &__img
    position: absolute
    left: 50%
    top: 0
    z-index: 2
    width: 100%
    height: 100%
    transform: translateX(-50%)
    pointer-events: none
    background-color: #fff
    align-items: center
    opacity: 0

    img
      display: block
      max-width: 100%
      height: 100%
      object-fit: cover
      margin: 0 auto

  &__item:first-child
    .image-switch__img
      opacity: 1
      z-index: -1

  &__item:hover
    .image-switch__img
      opacity: 1
      z-index: -1

.image-pagination
  position: absolute
  z-index: 30
  left: 0
  bottom: 0
  width: 100%
  display: flex
  justify-content: center

  &__item
    display: block
    width: 4px
    height: 4px
    border-radius: 100%
    margin: 0 3px
    background-color: #fff

.product-slider-wrapper
  width: 285px
  padding: 15px
  background-color: #fff

.product-slider-wrapper:not(:first-child)
  display: none
</style>