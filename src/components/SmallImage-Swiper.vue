<template>
  <div v-if="item.url.slice(1) === id" class="product">
    <swiper
      :slides-per-view="4"
      :space-between="10"

    >
      <swiper-slide
        class="item cursor-pointer"
        v-for="image in item.smallImages"
        :key="image.id"
      >
        <img :src="image.img" :alt="item.title" />
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper.scss";
import { mapGetters } from "vuex";

export default {
  props: {
    item: Object
  },
  components: {
    Swiper,
    SwiperSlide
  },
  computed: {
    ...mapGetters("products", { products: "all" }),
    id() {
      return this.$route.params.id;
    }
  }
};
</script>

<style scoped lang="sass">
.item
  max-width: 40px
  height: 45px

  img
    height: 100%
    object-fit: cover

.content
  max-width: 100%
</style>
