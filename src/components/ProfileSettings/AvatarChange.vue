<template>
  <transition name="menu">
    <div class="menu__wrapper" v-if="showModal">
      <div class="menu__w cursor-pointer" @click="$emit('close')"></div>
      <div class="menu__content absolute left-0">
        <div class="mb-4">
          <button type="button">Upload a photo...</button>
        </div>
        <form>
          <button class="block" type="button">
            Remove photo
          </button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    showModal: Boolean
  }
};
</script>

<style scoped lang="sass">
.menu
  &__wrapper
    position: absolute
    left: 0
    bottom: 0

  &__content
    bottom: -4rem
    width: 150px
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33)
    padding: 8px 12px
  &__w
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0
    z-index: 100
    display: block
    cursor: default
    content: ""
    background: transparent


</style>