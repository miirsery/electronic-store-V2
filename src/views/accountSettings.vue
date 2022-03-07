<template>
  <div class="settings">
    <h2 class="settings__title">Настройки пользователя</h2>
    <hr />
    <div class="settings__content flex">
      <ul class="settings__categories w-1/6">
        <li>
          <a href="#general">General</a>
        </li>
        <li>
          <a href="#motification">Notification</a>
        </li>
        <li>
          <a href="#accout">Accout</a>
        </li>
      </ul>
      <div class="settings__fields w-2/3">
        <form action="https://jsonplaceholder.typicode.com/users">
          <div class="settings__wrapper flex justify-between">
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
              <div class="general__img">
                <img src="../assets/avatar2.jpg" alt="avatar" />
                <button
                  @click="toggleModal"
                  class="general__img-button cursor-pointer"
                  type="button"
                >
                  <svg
                    class="h-8 w-8 text-black"
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
                  Edit
                </button>
                <avatar-change
                  :show-modal="showModal"
                  @close="toggleModal"
                />
              </div>
            </div>
          </div>
          <button
            type="button"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-6"
          >
            Update profile
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AvatarChange from "@/components/ProfileSettings/AvatarChange.vue";

export default defineComponent({
  name: "accountSettings",
  components: {
    AvatarChange
  },
  data() {
    return {
      showModal: false
    };
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    }
  }
});
</script>

<style scoped lang="sass">



.settings
  &__input
    margin-bottom: 2rem

.general
  &__img
    width: 200px
    height: 200px
    position: relative

    &-button
      position: absolute
      left: 10px
      bottom: 0

    img
      object-fit: cover
      height: 100%
      width: 100%
      border-radius: 50%
</style>
