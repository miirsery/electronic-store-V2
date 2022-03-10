<template>
  <div class="image-cropper">
    <div class="img__wrapper" v-show="isCrop">
      <!--      <img class="img__avatar&#45;&#45;new" ref="image" :src="src" alt="image" />-->

      <!--      <img class="img__avatar&#45;&#45;old" ref="image" :src="src" alt="image" v-if="url === null" />-->
      <img class="img__avatar--new" ref="image" :src="url" alt="img__avatar--new" />
      <button
        @click="onUpload"
        type="button" class="block img__save bg-blue-400 text-white pt-2 pb-2 pl-3 pr-3">
        Save
      </button>
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
    isCrop: Boolean,
    url: String
  },
  mounted() {
    this.image = this.$refs.image;
    console.log(this.image);
    this.cropper = new Cropper(this.image, {
      zoomable: false,
      scalable: false,
      aspectRatio: 1,
      crop: () => {
        const canvas = this.cropper.getCroppedCanvas();
        this.destination = canvas.toDataURL("image/png");
      }
    });
    this.newUrl = localStorage.getItem("url");
  },
  data() {
    return {
      cropper: {},
      destination: {},
      image: {},
      newImage: {},
      selectedFile: null,
      newFile: null,
      newUrl: null
    };
  },
  methods: {
    onUpload() {
      this.selectedFile = this.getAvatar;
      this.newUrl = localStorage.getItem("url");

      const formData = new FormData();
      const token = localStorage.getItem("tokenData");

      this.$api.user.uploadPhoto(formData)
        .then(res => console.log(res));

      this.$emit("crop");
      let myBlob = this.dataURItoBlob(this.destination);
      let name = this.selectedFile.name;
      // For send
      this.newFile = new File([myBlob], name);
      const data = {
        avatar: this.selectedFile,
        token: token
      };
      for (let dataKey in data) {
        if (dataKey === "avatar") {
          formData.append("avatar", this.selectedFile, this.selectedFile.name);
        } else formData.append(dataKey, data[dataKey]);
      }
    },
    dataURItoBlob(dataURI) {
      // convert base64/URLEncoded data component to raw binary data held in a string
      let byteString;
      if (dataURI.split(",")[0].indexOf("base64") >= 0)
        byteString = atob(dataURI.split(",")[1]);
      else
        byteString = unescape(dataURI.split(",")[1]);

      // separate out the mime component
      let mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0];

      // write the bytes of the string to a typed array
      let ia = new Uint8Array(byteString.length);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }

      return new Blob([ia], { type: mimeString });
    }
  },

  computed: {
    changeCropState() {
      return !this.isCrop;
    },
    isUser() {
      return this.$store.state.user;
    },
    getAvatar() {
      return this.$store.state.user.selectedFile;
    },
    getNewAvatar() {
      return this.$store.state.user.url;
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