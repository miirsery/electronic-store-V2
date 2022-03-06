<template>
  <div class="password-recovery">
    <h2 class="password-recovery__title font-bold text-3xl">
      Восстановление пароля
    </h2>
    <div class="password-recovery__wrapper">
      <div class="password-recovery__tabs flex items-center mb-4 mt-4">
        <button
          @click="toggleType"
          :disabled="!phone"
          :class="{ active: !phone }"
          class="password-recovery__tab text-xl block mr-4 pt-1 pb-1 pl-2 pr-2"
        >
          Восстановить по E-mail
        </button>
        <button
          :disabled="phone"
          @click="toggleType"
          class="password-recovery__tab text-xl block pt-1 pb-1 pl-2 pr-2"
          :class="{ active: phone }"
        >
          Восстановить по телефону
        </button>
      </div>
      <div class="password-recovery__content">
        <form class="password-recovery__email" v-if="!phone">
          <label class="password-recovery__label" for="email">E-mail <sup>*</sup></label>
          <input id="email" class="password-recovery__input mb-4" type="text" />
          <button type="button" class="text-white bg-blue-400 block p-4 uppercase bold">Восстановить</button>
        </form>
        <form class="password-recovery__phone" v-else>
          <label class="password-recovery__label" for="phone">Phone <sup>*</sup></label>
          <input id="phone" class="password-recovery__input mb-4" type="text" />
          <button type="button" class="text-white bg-blue-400 block p-4 uppercase bold">Восстановить</button>
        </form>
        <div class="password-recovery__actions mt-4">
          <button @click="toggleModal" type="button" class="block">
            У меня есть пароль. Войти на сайт
          </button>
          <button @click="toggleModal" type="button" class="block">
            Я хочу зарегистрироваться
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      phone: false
    };
  },
  methods: {
    toggleType() {
      console.log(this.phone);
      this.phone = !this.phone;
    },
    toggleModal() {
      this.$store.dispatch("toggleModal");
    }
  }
};
</script>

<style scoped lang="sass">
.password-recovery
  &__tab
    border-radius: 5px
    transition: all 200ms ease-in-out

    &.active
      transition: all 200ms ease-in-out
      background-color: rgba(51, 161, 255, 0.87)
      color: #fff

    &:hover
      background-color: rgba(119, 193, 255, 0.44)
      color: #fff

  &__email,
  &__phone
    background-color: rgba(210, 210, 210, 0.3)
    padding: 30px

  &__label
    sup
      color: rgba(226, 65, 65, 0.73)
</style>
