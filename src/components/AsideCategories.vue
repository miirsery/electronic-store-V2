<template>
  <aside class="aside">
    <nav>
      <ul class="aside__menu">
        <li
          class="aside__item pl-4 pb-3 pr-4 pt-3"
          v-for="item in items"
          :key="item.id"
        >
          <div class="aside__link-img inline-block mr-1.5">
            <img :src="item.imgUrl" alt="img" />
          </div>
          <router-link :to="item.url" class="aside__link">{{
            item.title
          }}</router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          id: 1,
          title: "Телефоны",
          imgUrl: require("../assets/phone.svg"),
          url: "/catalog/phones"
        },
        {
          id: 2,
          title: "Ноутбуки и компьютеры",
          imgUrl: require("../assets/laptop.svg"),
          url: "/catalog/laptops"
        },
        {
          id: 3,
          title: "Фото и видео",
          imgUrl: require("../assets/camera.svg"),
          url: "/catalog/photo-and-video"
        },
        {
          id: 4,
          title: "Товары для авто",
          imgUrl: require("../assets/car.svg"),
          url: "/catalog/products-for-auto"
        },
        {
          id: 5,
          title: "Техника для дома",
          imgUrl: require("../assets/home.svg"),
          url: "/catalog/products-for-home"
        }
      ]
    };
  }
};
</script>

<style scoped lang="sass">
.aside
  &__menu
    box-shadow: 0px 10px 13px rgba(0, 0, 0, 0.3)

  &__item
    &:hover
      background-color: rgba(34, 211, 238, 0.25)

  &__link
    color: #000
    font-size: 13px

    &-img
      width: 12px
      height: 12px

      img
        width: 100%
        object-fit: cover
</style>
