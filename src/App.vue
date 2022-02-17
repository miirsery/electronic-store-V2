<template>
  <div class="wrapper">
    <Header />
    <main class="main container">
      <Offers />
      <Loader v-if="showLoading" />
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
import { mapState } from "vuex";

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
  // created() {
  //   this.loading = true;
  //   setTimeout(() => {
  //     this.loading = false;
  //   }, 2000);
  // },
  computed: {
    ...mapState({
      showLoading: (state) => state.showLoading,
    })
  }
};
</script>

<style lang="sass" scoped>
.wrapper
  display: flex
  min-height: 100vh
  flex-direction: column
</style>
