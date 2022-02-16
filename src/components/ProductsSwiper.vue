<template>
  <div class="offers ">
    <h2 class="title mb-6">{{ title }}</h2>
    <div class="content">
      <swiper
        :modules="modules"
        :space-between="20"
        :slides-per-view="8"
        navigation
        @swiper="onSwiper"
        @slideChange="onSlideChange"
      >
        <swiper-slide v-for="product in products" :key="product.id">
          <img :src="product.imgUrl" :alt="product.title" />
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation } from "swiper";

import "swiper/swiper.scss";
import "swiper/components/navigation/navigation.scss";
import { mapGetters } from "vuex";

export default {
  props: {
    title: String
  },
  components: {
    Swiper,
    SwiperSlide
  },
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log("slide change");
    };
    return {
      onSwiper,
      onSlideChange,
      modules: [Navigation]
    };
  },
  computed: {
    ...mapGetters("products", { products: "all" })
  }
};
</script>

<style scoped lang="sass">
.offers
  box-shadow: 0 10px 13px rgba(0, 0, 0, 0.3)
  border-radius: 10px
  padding: 15px
  width: 100%
  margin-top: 2rem

.title
  font-size: 36px

</style>
