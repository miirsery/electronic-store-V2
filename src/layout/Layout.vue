<template>
  <general-header />
  <router-view />
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import GeneralHeader from '@/components/GeneralHeader.vue'

export default defineComponent({
  name: 'layout',
  components: {
    GeneralHeader,
  },
})
</script>
