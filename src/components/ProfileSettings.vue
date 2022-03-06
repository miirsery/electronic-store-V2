<template>
  <div class="profile-settings-mask__wrapper">
    <transition name="profile-settings">
      <div class="profile-settings-mask" v-if="showModal">
        <div class="profile-settings-wrapper" @click="$emit('close')">
          <div class="container container__wrapper">
            <div class="profile-settings-w" @click.stop>
              <h2>Здравствуйте, {{ isUser.user.username }}</h2>
              <router-link
                :to="{ name: 'accountSettings' }"
                class="mb-2 mt-4 block"
              >
                Настройки
              </router-link>
              <router-link to="/" class="mb-2 block"> Сообщения</router-link>
              <button type="button" class="cursor-pointer" @click="logout">
                Выход
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      defaultAvatar: require("../assets/avatar.png")
    };
  },
  props: {
    showModal: Boolean
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$store.dispatch("user/deleteUser");
      this.$store.dispatch("user/IS_AUTH", false);
      this.$store.dispatch("user/changeAvatar", this.defaultAvatar);
      this.$router.push({ name: "home" });
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
.container__wrapper
  position: relative

.profile-settings
  &-mask
    position: fixed
    z-index: 9998
    top: 0
    left: 0
    width: 100%
    height: 100%
    display: table
    transition: opacity 0.1s ease

  &-wrapper
    display: flex
    justify-content: flex-end
    margin-top: 4rem
    width: 100%
    height: 100%

  &-w
    height: 300px
    width: 200px
    position: absolute
    right: 0
    z-index: 10
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33)
    padding: 15px
    transition: all 0.1s ease
    background-color: #fff
    border-radius: 5px

.profile-settings-default-button
  float: right


.profile-settings-enter-active
  opacity: 0


.profile-settings-leave-active
  opacity: 0


.profile-settings-enter .profile-settings-container,
.profile-settings-leave-active .profile-settings-container
  transform: scale(1.1)

</style>
