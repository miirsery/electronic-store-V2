<template>
  <div class="offers flex justify-between w-full p-2 ">
    <button
      v-for="item in items" :key="item.title"
      type="button">{{ item.title }}</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: "Каталог"
        },
        {
          title: "ВСЕ АКЦИИ"
        },
        {
          title: "БЫСТРАЯ ДОСТАВКА"
        },
        {
          title: "ГАРАНТИЯ НИЗКОЙ ЦЕНЫ"
        },
        {
          title: "ДОСТУПНЫЕ ЦЕНЫ"
        },
        {
          title: "РАССРОЧКА"
        }
      ]
    };
  }
};
</script>

<style scoped lang="sass">

</style>