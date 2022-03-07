<template>
  <ul>
    <router-link to="/">Home</router-link>
    <li class="inline-block" v-for="(item, index) in crumbs" :key="index">
      <router-link :to="item.to">{{ item.to }}</router-link>
    </li>
  </ul>
</template>

<script>
export default {
  computed: {
    crumbs() {
      let pathArray = this.$route.path.split("/");
      pathArray.shift();
      let breadcrumbs = pathArray.reduce((breadcrumbArray, path, idx) => {
        breadcrumbArray.push({
          path: path,
          to: breadcrumbArray[idx - 1]
            ? "/" + breadcrumbArray[idx - 1].path + "/" + path
            : "/" + path
        });
        return breadcrumbArray;
      }, []);
      return breadcrumbs;
    }
  }
};
</script>

<style scoped>

</style>