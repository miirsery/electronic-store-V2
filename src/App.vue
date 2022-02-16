<template>
  <div class="container">
    <Header></Header>
    <Offers></Offers>
    <Loader v-show="loading"/>
    <router-view/>
    <router-view name="catalogItem" />
    <router-view name="productId" />

  </div>
</template>

<script>
import Header from "@/components/Header";
import Offers from "@/components/Offers";
import Loader from "@/components/Loader";

export default {
  components: {
    Header,
    Offers,
    Loader
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
