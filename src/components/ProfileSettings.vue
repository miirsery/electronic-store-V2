<template>
  <div class="profile-settings" v-if="isAuth.user !== null && showSettingsModal ===true">
    <h2>Здравствуйте qwdqwd</h2>
    <router-link to="/" class="mb-2 mt-4 block"> Настройки</router-link>
    <router-link to="/" class="mb-2 block"> Сообщения</router-link>
    <button type="button" class="cursor-pointer" @click="logout">
      Выход
    </button>
  </div>
</template>

<script>
export default {

};
</script>

<style scoped>

</style>