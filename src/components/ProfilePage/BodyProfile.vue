<template>
  <div class="body-profile">
    <form class="body-profile__form">
      <div class="body-profile__item">
        <label for="profileUsername" class="body-profile__item-label">
          Username
        </label>
        <input
          id="profileUsername"
          type="text"
          class="body-profile__input"
          placeholder="Your username..."
        />
      </div>
      <div class="body-profile__item">
        <label for="profileEmail" class="body-profile__item-label">Email</label>
        <input
          id="profileEmail"
          type="text"
          class="body-profile__input"
          placeholder="Your email..."
        />
      </div>
    </form>
  </div>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BodyProfile',
  setup() {
    return {}
  },
})
</script>

<style scoped lang='scss'>
.body-profile {
  width: 80%;

  &__item {
    margin-bottom: 1rem;
  }
}
</style>
