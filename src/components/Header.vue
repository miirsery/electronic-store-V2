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
          v-if="!auth && mode!==auth"

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
          <Form
            @submit="onSubmit"
            :validation-schema="schemaSignIn"
            @invalid-submit="onInvalidSubmit"
            v-if="mode === 'signIn'"
          >
            <TextInput
              name="name"
              type="text"
              label="Username"
              placeholder="Your username"
              success-message="Nice to meet you!"
            />
            <TextInput
              name="password"
              type="password"
              label="Password"
              placeholder="Your password"
              success-message="Nice and secure!"
            />
            <button
              class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"
              type="submit">
              Подтвердить
            </button>
          </Form>
          <Form
            @submit="onSubmit"
            :validation-schema="schema"
            @invalid-submit="onInvalidSubmit"
            v-if="mode === 'signUp'"
          >
            <TextInput
              name="name"
              type="text"
              label="Username"
              placeholder="Your username"
              success-message="Nice to meet you!"
            />
            <TextInput
              name="email"
              type="email"
              label="E-mail"
              placeholder="Your email address"
              success-message="Got it, we won't spam you!"
            />
            <TextInput
              name="password"
              type="password"
              label="Password"
              placeholder="Your password"
              success-message="Nice and secure!"
            />
            <TextInput
              name="confirm_password"
              type="password"
              label="Confirm Password"
              placeholder="Type it again"
              success-message="Glad you remembered it!"
            />
            <button
              class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"
              type="submit">
              Подтвердить
            </button>
          </Form>
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
import { Form } from "vee-validate";
import * as Yup from "yup";
import TextInput from "@/components/UI/TextInput";

export default {
  components: {
    Form,
    TextInput
  },
  created() {
    this.setUser(JSON.parse(localStorage.getItem("user")));
  },
  data() {
    const schema = Yup.object().shape({
      name: Yup.string().required(),
      email: Yup.string().email().required(),
      password: Yup.string().min(6).required(),
      confirm_password: Yup.string()
        .required()
        .oneOf([Yup.ref("password")], "Passwords do not match")
    });
    const schemaSignIn = Yup.object().shape({
      name: Yup.string().required(),
      password: Yup.string().min(6).required()
    });
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
      auth: true,
      schema,
      schemaSignIn
    };
  },
  methods: {
    ...mapActions({
      setUser: "user/setUser",
      deleteUser: "user/deleteUser"
    }),
    onSubmit(values) {
      if (this.isSignInForm) this.signIn(values);
      else this.signUp(values);
    },
    onInvalidSubmit() {
      const submitBtn = document.querySelector(".submit-btn");
      submitBtn.classList.add("invalid");
      setTimeout(() => {
        submitBtn.classList.remove("invalid");
      }, 1000);
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
    async signIn(data) {
      console.log(data);
      try {
        const responseData = (
          await this.$api.auth.signIn(data)
        ).data;
        console.log(responseData);
        localStorage.setItem("user", JSON.stringify(responseData));
        this.$store.dispatch("user/setUser");
        this.$emit("close");
        this.mode = "auth";
        this.auth = true;
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async signUp(data) {
      console.log(data);
      try {
        const responseData = (
          await this.$api.auth.signUp(data)
        ).data;
        console.log(responseData);
        localStorage.setItem("user", JSON.stringify(responseData));
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
    ...mapGetters("cart", { cartCnt: "length" }),
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

.submit-btn
  transition: ease-in-out all 300ms
</style>
