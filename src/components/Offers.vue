<template>
  <div class="offers flex justify-between w-full p-2">
    <router-link
      v-for="item in items"
      :key="item.title"
      type="button"
      :to="item.url"
      >{{ item.title }}
    </router-link>
  </div>
</template>

<script>

export default {
  data() {
    return {
      items: [
        {
          title: "Каталог",
          url: "/catalog",

        },
        {
          title: "ВСЕ АКЦИИ",
          url: "/offers",
        },
        {
          title: "БЫСТРАЯ ДОСТАВКА",
          url: '/fastDelivery'
        },
        {
          title: "ГАРАНТИЯ НИЗКОЙ ЦЕНЫ",
          url: '/lowPrice'
        },
        {
          title: "ДОСТУПНЫЕ ЦЕНЫ",
          url: '/prices'
        },
        {
          title: "РАССРОЧКА",
          url: '/something'
        },
      ],
    };
  },
};
</script>

<style scoped lang="sass"></style>
