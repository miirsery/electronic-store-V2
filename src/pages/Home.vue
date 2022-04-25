<template>
  <div class="home">
    <div class="home__container home__wrapper">
      This is home page.
      <div class="counter" @click="increment">
        {{ count.counter }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useStore } from 'vuex'
import { MutationTypes } from '@/store/store'

export default defineComponent({
  name: 'Home',
  setup() {
    const store = useStore()
    const count = ref(store.state)
    const increment = (): void => {
      store.commit(MutationTypes.INC_COUNTER, 1)
    }
    return {
      count,
      increment,
    }
  },
})
</script>

<style scoped>

</style>
