<template>
  <aside class="aside">
    <nav>
      <ul class="aside__menu">
        <li
          class="aside__item pl-4 pb-3 pr-4 pt-3"
          v-for="item in categories"
          :key="item.id"
        >
          <div class="aside__link-img inline-block mr-1.5">
            <img :src="item.imgUrl" alt="img" />
          </div>
          <router-link
            :to="item.url"
            class="aside__link"
            >{{ item.title }}
          </router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("categories", { categories: "all" })
  }
};
</script>

<style scoped lang="sass">
.aside
  &__menu
    box-shadow: 0 10px 13px rgba(0, 0, 0, 0.3)

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
