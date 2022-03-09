<template>
  <div class="image-cropper">
    <div class="img__wrapper" v-show="isCrop">
      <img ref="image" :src="src" alt="image" />
    </div>
    <div class="img__destination">
      <img :src="destination" alt="" />
    </div>
  </div>
</template>

<script>
import Cropper from "cropperjs";

export default {
  name: "ImageCropper",
  props: {
    src: String,
    isCrop: Boolean
  },
  data() {
    return {
      cropper: {},
      destination: {},
      image: {},
    };
  },
  mounted() {
    this.image = this.$refs.image;
    this.cropper = new Cropper(this.image, {
      zoomable: false,
      scalable: false,
      aspectRatio: 1,
      crop: () => {
        const canvas = this.cropper.getCroppedCanvas();
        this.destination = canvas.toDataURL("image/png");
      }
    });
  },
  computed: {
    changeCropState() {
      return !this.isCrop;
    }
  }
};
</script>

<style scoped lang="sass">
.image-cropper
  z-index: 100

.img
  &__destination
    width: 200px
    height: 200px

    img
      height: 100%
      width: 100%
      object-fit: cover
      border-radius: 50%

  &__wrapper
    width: 450px
    height: 450px
    position: fixed
    z-index: 999
    top: 50%
    right: 0
    bottom: 0
    left: 50%
    transform: translate(-50%, -50%)
    img
      width: 100%
      height: 100%
      object-fit: cover
</style>