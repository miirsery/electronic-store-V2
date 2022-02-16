<template>
  <div class="container wrapper">
    <Header></Header>
    <main class="main">
      <Offers></Offers>
      <Loader v-show="loading" />
      <router-view />
      <router-view name="catalogItem" />
      <router-view name="productId" />
    </main>
    <my-footer />
  </div>
</template>

<script>
import Header from "@/components/Header";
import Offers from "@/components/Offers";
import Loader from "@/components/Loader";
import MyFooter from "@/components/MyFooter";

export default {
  components: {
    Header,
    Offers,
    Loader,
    MyFooter
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

<style lang="sass" scoped>
.wrapper
  display: flex
  min-height: 100vh
  flex-direction: column
</style>
