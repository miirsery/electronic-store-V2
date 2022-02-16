<template>
  <div class="hero flex mt-2 w-full">
    <AsideCategories class="mr-8"></AsideCategories>
    <Hero></Hero>
  </div>
  <products-swiper title="Успейте купить"/>
  <products-swiper title="Акция месяца"/>
</template>

<script>
import AsideCategories from "@/components/AsideCategories";
import Hero from "@/components/Hero";
import ProductsSwiper from "@/components/ProductsSwiper";

export default {
  components: {
    AsideCategories,
    Hero,
    ProductsSwiper
  }
};
</script>

<style scoped>

</style>