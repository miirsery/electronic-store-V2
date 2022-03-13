<template>
  <div class="image-cropper">
    <div class="img__wrapper">
      <img
        class="img__avatar--new"
        ref="image"
        :src="src"
        alt="img__avatar--new"
      />
      <button
        @click="onSubmit"
        type="button"
        class="block img__save bg-blue-400 text-white pt-2 pb-2 pl-3 pr-3"
      >
        Save
      </button>
    </div>
  </div>
</template>

<script>
import Cropper from "cropperjs";

export default {
  name: "ImageCropper",
  props: {
    src: String
  },
  data() {
    return {
      cropper: {},
      destination: {},
      image: {},
      newDestination: {},
      currentFile: null
    };
  },
  watch: {
    destination(val, newVal) {
      this.newDestination = newVal;
    }
  },
  mounted() {
    console.log("MOUNTED");
    if (this.image)
      setTimeout(() => {
        this.changeAvatar();
      }, 100);
  },
  methods: {
    changeAvatar() {
      console.log("CHANGE");
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
    onSubmit() {
      setTimeout(() => {
        this.currentFile = this.isUser.user.selectedFile;
        console.log(this.currentFile);
        const token = localStorage.getItem("tokenData");
        const formData = new FormData();

        const data = {
          avatar: this.currentFile,
          token: token
        };
        for (let dataKey in data) {
          if (dataKey === "avatar") {
            formData.append(
              "avatar",
              this.currentFile,
              this.currentFile.name
            );
          } else formData.append(dataKey, data[dataKey]);
        }
        this.$api.user.uploadPhoto(formData).then((res) => console.log(res));
        this.$store.dispatch("user/setAvatarFile", this.destination);
        this.$store.commit("user/TOGGLE_CROP", false);
      }, 500);
    }
  },
  computed: {
    isUser() {
      return this.$store.state.user;
    }
  }
};
</script>
<style>
.image-cropper .cropper-view-box {
  box-shadow: 0 0 0 1px #39f;
  border-radius: 50%;
  outline: 0;
}
</style>
<style scoped lang="sass">
.image-cropper
  z-index: 120

.img
  &__destination
    width: 200px
    height: 200px

  &__save
    text-align: center

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
