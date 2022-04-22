<template>
  <div class="profile-page">
    <div class="profile-page__wrapper profile-page__container">
      <aside-profile />
      <body-profile />
      <image-profile />
    </div>
  </div>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'
import AsideProfile from '@/components/ProfilePage/AsideProfile.vue'
import BodyProfile from '@/components/ProfilePage/BodyProfile.vue'
import ImageProfile from '@/components/ProfilePage/ImageProfile.vue'
export default defineComponent({
  name: 'ProfilePage',
  components: {
    AsideProfile,
    BodyProfile,
    ImageProfile,
  },
  setup() {
    return {}
  },
})
</script>

<style scoped lang='scss'>
.profile-page {
  &__wrapper {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }
}
</style>
