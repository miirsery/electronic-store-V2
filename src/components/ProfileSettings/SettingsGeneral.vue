<template>
  <div class="general flex w-full justify-between">
    <div class="general__fields">
      <label for="settingsName">Name</label>
      <input
        class="settings__input"
        id="settingsName"
        type="text"
        placeholder="Name"
      />
      <label for="settingsSurname">Surname</label>
      <input
        class="settings__input"
        id="settingsSurname"
        type="text"
        placeholder="Surname"
      />
      <div class="settings__update-password">
        <p class="mt-2 mb-2 font-bold">Update password</p>
        <label for="settingsOldPassword">Old password</label>
        <input
          id="settingsOldPassword"
          type="text"
          class="settings__input"
          placeholder="Old password"
        />
        <label for="settingsConfirmPassword">New password</label>
        <input
          id="settingsConfirmPassword"
          type="text"
          class="settings__input"
          placeholder="Confirm password"
        />
      </div>
    </div>
    <div class="general__img" >
      <!--      <img :src="isUser.user.avatar" alt="avatar" />-->
      <image-cropper
        :is-crop="isCrop"
        :src="isUser.user.avatar" />
      <button
        @click="toggleModal"
        class="general__img-button cursor-pointer"
        type="button"
      >
        <svg
          class="h-5 w-5 text-black"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path
            d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"
          />
        </svg>
        <span>Edit</span>
      </button>
      <avatar-change
        @crop="onCropSize"
        :show-modal="showModal"
        @close="toggleModal"
      />
    </div>
  </div>
</template>

<script>
import AvatarChange from "@/components/ProfileSettings/AvatarChange";
import ImageCropper from "@/components/ImageCropper";

export default {
  components: {
    AvatarChange,
    ImageCropper
  },
  data() {
    return {
      showModal: false,
      isCrop: false
    };
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
    onCropSize() {
      this.isCrop = !this.isCrop;
    }
  },
  computed: {
    isUser() {
      return this.$store.state.user;
    }

  }
};
</script>

<style scoped lang="sass">
.general
  &__img
    position: relative

    &-button
      position: absolute
      left: 0
      bottom: 22px
      background-color: #fff
      padding: 2px 8px
      display: flex
      border-radius: 10px
      border: 1px solid rgba(0, 0, 0, 0.5)
      align-items: center
      z-index: 120

      span
        display: block

    img
      object-fit: cover
      height: 100%
      width: 100%
      border-radius: 50%
</style>