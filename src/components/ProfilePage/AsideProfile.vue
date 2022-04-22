<template>
  <aside class="aside-profile">
    <nav class="aside-profile__wrapper">
      <ul class="aside-profile__menu">
        <li class="aside-profile__item" v-for="item in data">
          <a :href="`#${item.value}`" class="aside-profile__link">
            {{ item.name }}
          </a>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'
import AsideProfile from '@/testBackend/AsideProfile'
export default defineComponent({
  name: 'AsideProfile',
  setup() {
    const data = AsideProfile()
    console.log(data)
    return {
      data,
    }
  },
})
</script>

<style scoped lang='scss'>
.aside-profile {
  width: 300px;
}
</style>
