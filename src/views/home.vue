<template>
  <div class="hero flex mt-2 w-full">
    <AsideCategories class="mr-8"></AsideCategories>
    <Hero></Hero>
  </div>
</template>

<script>
import AsideCategories from "@/components/AsideCategories";
import Hero from "@/components/Hero";

export default {
  components: {
    AsideCategories,
    Hero
  }
};
</script>

<style scoped>

</style>