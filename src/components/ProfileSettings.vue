<template>
  <transition name="profile-settings">
    <div class="profile-settings-mask" v-if="showModal">
      <h2>Здравствуйте, {{ isUser.user.username }}</h2>
      <router-link to="/" class="mb-2 mt-4 block"> Настройки</router-link>
      <router-link to="/" class="mb-2 block"> Сообщения</router-link>
      <button type="button" class="cursor-pointer" @click="logout">
        Выход
      </button>
    </div>
  </transition>
</template>

<script>

export default {
  props: {
    showModal: Boolean
  },
  methods: {
    logout() {
      localStorage.removeItem("tokenData");
      this.$store.dispatch("user/deleteUser");
      this.$store.dispatch("user/IS_AUTH", false);
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
.profile-settings-mask
  background-color: #fff
  height: 300px
  width: 350px
  position: absolute
  z-index: 10
</style>