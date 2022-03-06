<template>
  <Header />
  <main class="main container">
    <Offers />
    <Loader v-if="showLoading" />
    <router-view />
    <router-view name="catalogItem" />
    <router-view name="productId" />
  </main>
  <my-footer />
</template>

<script>
import Header from "@/components/Header";
import Offers from "@/components/Offers";
import Loader from "@/components/Loader";
import MyFooter from "@/components/MyFooter";
import { mapMutations, mapState } from "vuex";
import { LOADING_SPINNER_SHOW_MUTATIONS } from "@/store/constants";

export default {
  components: {
    Header,
    Offers,
    Loader,
    MyFooter
  },

  created() {
    this.$store.commit(`${LOADING_SPINNER_SHOW_MUTATIONS}`, true);
    setTimeout(() => {
      this.$store.commit(`${LOADING_SPINNER_SHOW_MUTATIONS}`, false);
    }, 500);
    let userData = JSON.parse(localStorage.getItem("user")) ;
    if (userData !== null) {
      console.log(userData);
      this.$store.dispatch("user/setUser", userData);
      this.$store.dispatch("user/IS_AUTH", true);
    }
  },
  computed: {
    ...mapMutations([
      `${LOADING_SPINNER_SHOW_MUTATIONS}`
    ]),
    ...mapState([
      "showLoading"
    ])
  }
};
</script>

<style lang="sass" scoped>
.wrapper
  display: flex
  min-height: 100vh
  flex-direction: column
</style>