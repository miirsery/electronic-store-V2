<template>
  <header class="header container">
    <div
      class="wrapper flex justify-between border-4 items-center border-b-2 border-gray-100 p-3"
    >
      <router-link to="/" class="actions__link">Logo</router-link>
      <nav>
        <ul class="relative flex">
          <li class="item mr-4">
            <select name="" id="" class="select-text">
              <option value="Novosibirsk">Новосибирск</option>
              <option value="Omsk">Омск</option>
              <option value="Barnaul">Барнаул</option>
              <option value="Moscow">Москва</option>
            </select>
          </li>
          <li class="item">
            <form class="search border-b-2 w-full">
              <input
                class="border-none bg-transparent"
                type="text"
                placeholder="Начать поиск..."
                @focus="focused = true"
                @blur="focused = false"
                @onFocus="focusThis"
              >
            </form>
          </li>
        </ul>
      </nav>
      <div class="actions">
        <ul class="actions__menu flex items-center">
          <li class="actions__item">
            <router-link :to="{ name: 'cart' }" class="actions__link icon cart">
              <img :src="cartImgUrl" alt="cart">
              <p class="cart__cnt">
                {{ cartCnt }}
              </p>
            </router-link>
          </li>
          <li class="actions__item ml-4">
            <a href="/" class="actions__link icon">
              <img :src="favoriteImgUrl" alt="favorite" />
            </a>
          </li>
          <li class="actions__item ml-4">
            <button
              type="button"
              class="actions__link icon"
              data-micromodal-trigger="modal-1"
              @click="toggleType"
            >
              <img src="../assets/avatar.png" alt="logo" />
            </button>
          </li>
        </ul>
        <div
          class="modal fixed absolute bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 z-10"
          v-if="!auth"
        >
          <div class="modal__top mb-3">
            <button
              :class="{ active: mode === 'signIn' }"
              type="button"
              @click="mode = isSignInForm ? 'signUp' : 'signIn'"
              :disabled="isSignInForm"
            >
              Вход /
            </button>
            <button
              :class="{ active: mode === 'signUp' }"
              type="button"
              @click="mode = isSignInForm ? 'signUp' : 'signIn'"
              :disabled="!isSignInForm"
            >
              Регистрация
            </button>
          </div>
          <div class="w-full max-w-xs sign-in" v-if="mode === 'signIn'">
            <form @submit.prevent="formSubmit">
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="emailSignIn"
                >
                  Email
                </label>
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="emailSignIn"
                  type="text"
                  placeholder="Email"
                  v-model="user.email"
                />
              </div>
              <div class="mb-6">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="password"
                >
                  Password
                </label>
                <input
                  class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="password"
                  type="password"
                  v-model="user.password"
                  placeholder="******************"
                />
                <p class="text-red-500 text-xs italic">
                  Please choose a password.
                </p>
              </div>
              <div class="flex items-start mb-6">
                <div class="flex items-center h-5">
                  <input id="remember" aria-describedby="remember" type="checkbox"
                         class="w-4 h-4 bg-gray-50 rounded border border-gray-300 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800"
                  >
                </div>
                <div class="ml-3 text-sm">
                  <label for="remember" class="font-medium text-gray-900 dark:text-gray-300">Remember me</label>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <button
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  type="submit"
                >
                  Sign In
                </button>
                <a
                  class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
                  href="#"
                >
                  Forgot Password?
                </a>
              </div>
            </form>
            <p class="text-center text-gray-500 text-xs">
              &copy;2020 Acme Corp. All rights reserved.
            </p>
          </div>
          <div class="w-full max-w-xs sign-up" v-if="mode === 'signUp'">
            <form @submit.prevent="formSubmit">
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="usernameSignUp"
                >
                  Username
                </label>
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="usernameSignUp"
                  type="text"
                  placeholder="Username"
                  v-model="user.username"
                  required
                />
              </div>
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="email"
                >
                  Email
                </label>
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="email"
                  type="text"
                  placeholder="Email"
                  required
                  v-model="user.email"
                />
              </div>
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="passwordSignUp"
                >
                  Password
                </label>
                <input
                  class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="passwordSignUp"
                  type="password"
                  placeholder="******************"
                  v-model="user.password"
                  required
                />
                <p class="text-red-500 text-xs italic">
                  Please choose a password.
                </p>
              </div>
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="passwordRetry"
                >
                  Повторите пароль
                </label>
                <input
                  class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="passwordRetry"
                  type="password"
                  placeholder="******************"
                  required
                  v-model="user.retryPassword"
                />
                <p class="text-red-500 text-xs italic">
                  Please choose a password.
                </p>
              </div>
              <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
              >
                Sign Up
              </button>
            </form>
            <p class="text-center text-gray-500 text-xs">
              &copy;2020 Acme Corp. All rights reserved.
            </p>
          </div>
        </div>
        <div class="profile-settings" v-if="toggle && auth && mode==='auth'">
          <h2>Здравствуйте {{ user.name }}</h2>
          <router-link to="/" class="mb-2 mt-4 block">
            Настройки
          </router-link>
          <router-link to="/" class="mb-2 block">
            Сообщения
          </router-link>
          <button
            type="button" class="cursor-pointer"
            @click="logOut"
          >Выход
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>

import { mapActions, mapGetters } from "vuex";

export default {
  created() {
    this.setUser(JSON.parse(localStorage.getItem("user")));
  },
  data() {
    return {
      toggle: false,
      favoriteImgUrl: require("../assets/heart.svg"),
      cartImgUrl: require("../assets/cart.svg"),
      user: {
        username: "",
        password: "",
        email: "",
        retryPassword: ""
      },
      mode: "signIn",
      errors: [],
      auth: false
    };
  },

  methods: {
    ...mapActions({
      setUser: "user/setUser",
      deleteUser: "user/deleteUser"
    }),
    formSubmit() {
      if (this.isSignInForm) {
        this.signIn();
      } else {
        this.signUp();
      }
    },
    close() {
      this.$emit("close");
    },
    logOut() {
      this.$api.auth.logout();
      localStorage.removeItem("user");
      this.deleteUser();
      this.mode = "signIn";
      this.$router.push({ name: "home" });
    },
    toggleType() {
      if (this.mode !== "auth") {
        this.auth = !this.auth;
      }
      if (this.mode === "auth") {
        this.toggle = !this.toggle;
      }
    },
    async signIn() {
      try {
        const data = (
          await this.$api.auth.signIn({
            email: this.user.email,
            password: this.user.password
          })
        ).data;
        console.log(data);
        localStorage.setItem("user", JSON.stringify(data));
        this.$store.dispatch("user/setUser");
        this.$emit("close");
        this.mode = "auth";
        this.auth = true;
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async signUp() {
      try {
        const data = (
          await this.$api.auth.signUp({
            email: this.user.email,
            password: this.user.password,
            retryPassword: this.user.retryPassword,
            username: this.user.username
          })
        ).data;
        console.log(data);
        localStorage.setItem("user", JSON.stringify(data));
        this.$store.dispatch("user/setUser");
        this.$emit("close");
        this.mode = "auth";
        this.auth = true;
      } catch (error) {
        console.log(error.response.data);
      }
    }
  },
  computed: {
    ...
      mapGetters("cart", { cartCnt: "length" }),
    isSignInForm() {
      return this.mode === "signIn";
    }
  }
}
;
</script>

<style scoped lang="sass">
.logo
  padding: 15px 0

.wrapper
  width: 100%

.icon
  max-width: 36px
  max-height: 36px
  display: block

  img
    width: 100%
    object-fit: cover


.sign-in,
.sign-up
  display: flex
  flex-direction: column

.modal
  left: 50%
  top: 50%
  transform: translate(-50%, -50%)

  &__top
    button
      font-size: 22px
      font-weight: 300
      opacity: 0.4

      &.active
        font-weight: 500
        opacity: 1

.cart
  position: relative
  display: block

  &__cnt
    position: absolute
    top: 0
    left: 0
    color: #fff
    z-index: 10
    font-size: 14px

    &::after
      content: ''
      position: absolute
      top: -2px
      left: -5px
      height: 20px
      width: 20px
      background-color: rgb(86, 195, 205)
      border-radius: 50%
      color: #ffffff
      text-align: left
      z-index: -1


.profile-settings
  background-color: #fff
  height: 300px
  width: 350px
  position: absolute
  z-index: 10
</style>
