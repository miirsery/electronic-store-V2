<template>
  <div class="offers">
    <div class="content">
      <swiper
        :modules="modules"
        :space-between="50"
        :slides-per-view="1"
        navigation
        :pagination="{ clickable: true }"
        :scrollbar="{ draggable: true }"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
      >
        <swiper-slide v-for="item in items" :key="item.id">
          <img :src="item.src" :alt="item.title" />
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Navigation, Scrollbar, Pagination } from "swiper";

import "swiper/swiper.scss";
import "swiper/components/navigation/navigation.scss";
import "swiper/components/scrollbar/scrollbar.scss";
import "swiper/components/pagination/pagination.scss";

export default {
  components: {
    Swiper,
    SwiperSlide,
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
      modules: [Navigation, Scrollbar, Pagination],
    };
  },
  data() {
    return {
      items: [
        {
          id: 1,
          src: require("../assets/hero-carousel/1.jpg"),
        },
        {
          id: 2,
          src: require("../assets/hero-carousel/2.jpg"),
        },
        {
          id: 3,
          src: require("../assets/hero-carousel/3.jpg"),
        },
        {
          id: 4,
          src: require("../assets/hero-carousel/4.jpg"),
        },
      ],
    };
  },
};
</script>

<style scoped lang="sass">

.offers
  width: 80%
</style>
