<template>
  <div class="container">

    <my-loader v-show="loading"></my-loader>
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
import MyLoader from "@/components/UI/MyLoader";

export default {
  components: {
    Header,
    Offers,
    MyLoader
  },
  data() {
    return {
      loading: true
    };
  },
  created() {
    this.loading = true;
    setTimeout(() => {
      this.loading = false;
    }, 2000);
  }
};
</script>

<style lang="sass">

</style>
