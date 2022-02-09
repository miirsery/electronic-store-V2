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
          <a href="/" class="aside__link">{{ item.title }}</a>
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
        },
        {
          id: 2,
          title: "Ноутбуки и компьютеры",
          imgUrl: require("../assets/laptop.svg"),
        },
        {
          id: 3,
          title: "Фото и видео",
          imgUrl: require("../assets/camera.svg"),
        },
        {
          id: 4,
          title: "Товары для авто",
          imgUrl: require("../assets/car.svg"),
        },
        {
          id: 5,
          title: "Техника для дома",
          imgUrl: require("../assets/home.svg"),
        },
      ],
    };
  },
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
