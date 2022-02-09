<template>
  <div class="container">
    <Header></Header>
    <Offers></Offers>
    <div class="hero flex mt-2">
      <AsideCategories class="mr-8"></AsideCategories>
      <Hero></Hero>
    </div>
    <router-view />
  </div>
</template>

<script>
import Header from "@/components/Header";
import AsideCategories from "@/components/AsideCategories";
import Hero from "@/components/Hero";
import Offers from "@/components/Offers";

export default {
  components: {
    Header,
    AsideCategories,
    Hero,
    Offers
  }
};
</script>

<style lang="sass">

</style>
