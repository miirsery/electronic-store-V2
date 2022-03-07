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
              />
            </form>
          </li>
        </ul>
      </nav>
      <div class="actions">
        <ul class="actions__menu flex items-center">
          <li class="actions__item">
            <router-link :to="{ name: 'cart' }" class="actions__link icon cart">
              <img :src="cartImgUrl" alt="cart" />
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
          <li class="actions__item actions__item-avatar ml-4">
            <button
              type="button"
              class="actions__link icon"
              data-micromodal-trigger="modal-1"
              @click="toggleModal"
            >
              <img :src="isUser.user.avatar" alt="logo" />
            </button>
          </li>
        </ul>
        <auth
          :show-modal="showModal && isUser.isAuth === false"
          @close="toggleModal"
        />
        <profile-settings
          :show-modal="showModal && isUser.isAuth !== false"
          @close="toggleModal"
        />
      </div>
    </div>
  </header>
</template>
<script>
import Auth from "@/components/forrms/Auth";
import { mapGetters } from "vuex";
import ProfileSettings from "@/components/ProfileSettings";

export default {
  components: {
    Auth,
    ProfileSettings
  },
  data() {
    return {
      favoriteImgUrl: require("../assets/heart.svg"),
      cartImgUrl: require("../assets/cart.svg")
    };
  },
  methods: {
    toggleModal() {
      this.$store.dispatch("toggleModal");
    }
  },
  computed: {
    ...mapGetters("cart", { cartCnt: "length" }),
    isUser() {
      return this.$store.state.user;
    },
    showModal() {
      return this.$store.state.showAuthModal;
    }
  }
};
</script>

<style scoped lang="sass">
.modal
  &-mask
    position: fixed
    z-index: 9998
    top: 0
    left: 0
    width: 100%
    height: 100%
    background-color: rgba(0, 0, 0, .5)
    display: table
    transition: opacity .3s ease

  &-wrapper
    display: table-cell
    vertical-align: middle


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

.actions
  position: relative

.profile-settings
  background-color: #fff
  height: 300px
  width: 350px
  position: absolute
  z-index: 10

.submit-btn
  transition: ease-in-out all 300ms

.actions
  &__item
    &-avatar
      width: 36px
      height: 36px

      img
        width: 100%
        height: 100%
        object-fit: cover
        border-radius: 50%
</style>
