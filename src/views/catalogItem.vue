<template>
  <div>
    <h2>{{ category.title }} </h2>
    <hr>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("categories", { categoryProxy: "item" }),
    id() {
      return this.$route.params.id;
    },
    category() {
      return this.categoryProxy(this.id);
    }
  }
};
</script>

<style scoped>

</style>