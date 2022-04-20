<template>
  <header class="header">
    <div class="header__container header__wrapper">
      <router-link to="/" class="header__logo">
        <icon-template name="logo" width="36" height="36" />
      </router-link>
      <nav class="header__menu">
        <ul class="header__menu-wrapper">
          <li class="header__menu-item">
            <button class="header__menu-button" @click="handleToggleModal">
              Open
            </button>
            <auth-modal @close="handleToggleModal" v-if="isAuthModalVisible" />
          </li>
          <li class="header__menu-item">
            <router-link :to="{ name: 'CartPage' }" class="header__menu-button">
              Cart
            </router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script lang="ts">
import { defineAsyncComponent, defineComponent, ref } from 'vue'

export default defineComponent({
  components: {
    AuthModal: defineAsyncComponent(
      () => import('@/components/Modals/Auth/AuthModal.vue')
    ),
  },
  setup() {
    const isAuthModalVisible = ref(false)

    const handleToggleModal = (): void => {
      isAuthModalVisible.value = !isAuthModalVisible.value
    }

    return {
      isAuthModalVisible,
      handleToggleModal,
    }
  },
})
</script>

<style scoped lang="scss">
.header {
  &__wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__menu {
    &-wrapper {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    &-button {
      color: $color-black;
    }

    &-item {
      margin-right: 2rem;
    }
  }
}
</style>
