<template>
  <transition name="menu">
    <div class="menu__wrapper" v-if="showModal">
      <div class="menu__w cursor-pointer" @click="$emit('close'), onUpload()"></div>
      <div class="menu__content absolute left-0">
        <form class="menu__content-item menu__content-item-upload">
          <label class="file">
            <input
              @click="$emit('crop')"
              @change="onFileSelected"
              type="file"
              id="file"
              aria-label="File browser"
            />
            <span class="block file-custom">Upload file...</span>
          </label>
        </form>
        <form class="menu__content-item">
          <button class="block" type="button">
            Remove photo
          </button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "AvatarChange",
  props: {
    showModal: Boolean
  },
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    onUpload() {
      const formData = new FormData();
      const token = localStorage.getItem("tokenData");
      const data = {
        avatar: this.selectedFile,
        token: token,
      };
      for (let dataKey in data) {
        if (dataKey === "avatar"){

          // Append all data

          // for (let previewKey in data[dataKey]) {
          //   // formData.append(`avatar[${previewKey}]`, data[dataKey][previewKey])
          //
          // }

          // Append all data binary
          formData.append("avatar", this.selectedFile, this.selectedFile.name);
        }
        else formData.append(dataKey, data[dataKey])
      }
      this.$api.user.uploadPhoto(formData)
        .then(res => console.log(res));
    }
  }
};
</script>

<style scoped lang="sass">
.menu
  &__wrapper
    position: absolute
    left: 0
    bottom: 0

  &__content
    bottom: -4.5rem
    width: 150px
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33)
    z-index: 120

    &-item
      padding: 8px 12px

      &:hover
        background-color: #dbdbdb

  &__w
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    z-index: 100
    display: block
    cursor: default
    content: ""
    background: transparent

.file
  position: relative
  cursor: pointer

  input
    opacity: 0
    margin: 0

  &-custom
    position: absolute
    top: 0
    right: 0
    left: 0
    z-index: 5
    width: 126px
    color: #000
    background-color: transparent
    border-radius: 0.25rem
    user-select: none

</style>