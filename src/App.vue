<template>
  <div class="container">
    <Header></Header>
    <Offers></Offers>

    <router-view />

    <router-view name="catalogItem" />

    <router-view name="productId" />
  </div>
</template>

<script>
import Header from "@/components/Header";
import Offers from "@/components/Offers";

export default {
  components: {
    Header,
    Offers
  }
};
</script>

<style lang="sass">

</style>
