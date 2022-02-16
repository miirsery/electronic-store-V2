<template>
  <div class="fullCategories">
    <div class="fullCategories__item mt-4">
      <p class="fullCategories__item-title mb-8 font-bold">Телефоны</p>
      <div class="fullCategories__item-content">
        <ul class="fullCategories__item-content-menu">
          <li class="fullCategories__item-content-item mb-4 hover:underline" v-for="item in categories" :key="item.id">
            <router-link :to="item.url" class="fullCategories__item-content-link">{{ item.title }}</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
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
.fullCategories
  &__item
    &-title
      font-size: 24px
</style>