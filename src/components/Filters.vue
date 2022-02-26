<template>
  <el-form>
    <div class="slider-block">
      <el-slider v-model="value" range :max="300000" />
    </div>
  </el-form>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import type { ElForm } from "element-plus";


const value = ref([10000, 40000]);

</script>

<style scoped>

</style>