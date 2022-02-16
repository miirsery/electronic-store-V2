<template>
  <header class="header">
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
            <router-link :to="{ name: 'cart' }" class="actions__link icon">
              <img :src="cartImgUrl" alt="cart">
            </router-link>
            {{ cartCnt }}
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
              @click="toggle = !toggle"
            >
              <img src="../assets/avatar.png" alt="logo" />
            </button>
          </li>
        </ul>
        <div
          class="modal fixed absolute bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 z-10"
          v-show="toggle"
        >
          <div class="modal__top mb-3">
            <button
              :class="{ active: login }"
              type="button"
              @click="login = !login"
              :disabled="login"
            >
              Вход /
            </button>
            <button
              :class="{ active: !login }"
              type="button"
              @click="login = !login"
              :disabled="!login"
            >
              Регистрация
            </button>
          </div>
          <div class="w-full max-w-xs sign-in" v-show="login">
            <form>
              <div class="mb-4">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="username"
                >
                  Username
                </label>
                <input
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="username"
                  type="text"
                  placeholder="Username"
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
                         required>
                </div>
                <div class="ml-3 text-sm">
                  <label for="remember" class="font-medium text-gray-900 dark:text-gray-300">Remember me</label>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <button
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  type="button"
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
          <div class="w-full max-w-xs sign-in" v-show="!login">
            <form>
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
                />
                <p class="text-red-500 text-xs italic">
                  Please choose a password.
                </p>
              </div>
              <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="button"
              >
                Sign Up
              </button>
            </form>
            <p class="text-center text-gray-500 text-xs">
              &copy;2020 Acme Corp. All rights reserved.
            </p>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>

import { mapGetters } from "vuex";

export default {
  data() {
    return {
      toggle: false,
      login: true,
      favoriteImgUrl: require("../assets/heart.svg"),
      cartImgUrl: require("../assets/cart.svg"),
    };
  },
  computed: {
    ...mapGetters("cart", { cartCnt: "length" })
  },
};
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
</style>
