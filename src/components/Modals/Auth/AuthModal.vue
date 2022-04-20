<template>
  <div class="auth-modal-overlay" @click="handleCloseModal">
    <div class="auth-modal__wrapper" @click.stop>
      <div class="auth-modal__actions">
        <button
          @click="handleToggleAuthType"
          data-name="SignIn"
          class="auth-modal__action subtitle"
          :class="{ active: authType === 'SignIn' }"
        >
          SignIn
        </button>
        <button
          @click="handleToggleAuthType"
          data-name="SignUp"
          class="auth-modal__action subtitle"
          :class="{ active: authType === 'SignUp' }"
        >
          SignUp
        </button>
      </div>
      <div class="auth-modal__body">
        <keep-alive>
          <component :is="authType" />
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineAsyncComponent, defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'AuthModal',
  emits: ['close'],

  components: {
    SignIn: defineAsyncComponent(
      () => import('@/components/Modals/Auth/SignIn.vue')
    ),
    SignUp: defineAsyncComponent(
      () => import('@/components/Modals/Auth/SignUp.vue')
    ),
  },

  setup(_, { emit }) {
    let authType = ref('SignIn')

    const handleCloseModal = (): void => {
      emit('close')
    }

    const handleToggleAuthType = (event): void => {
      authType.value = event.target.dataset.name
    }

    return {
      authType,
      handleCloseModal,
      handleToggleAuthType,
    }
  },
})
</script>

<style scoped lang="scss">
.auth-modal-overlay {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 10;
  width: 100%;
  height: 100%;
  background-color: rgba(78, 73, 73, 0.3);
}

.auth-modal {
  &__wrapper {
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 11;
    border-radius: 10px;
    padding: 10px 30px;
    width: 400px;
    min-height: 300px;
    background-color: $color-white;
    transform: translate(-50%, -50%);
  }

  &__actions {
    display: flex;
    justify-content: space-between;
  }

  &__action {
    width: 45%;
    height: 30px;
    color: $color-dark;
    transition: border-bottom 0.2s ease-in;

    &.active {
      border-bottom: 2px solid $color-accent-dark;
    }
  }
}
</style>
