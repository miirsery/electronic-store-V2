<template>
  <div class="sign-up">
    <form class="sign-up__form">
      <div class="sign-up__form-item">
        <label class="sign-up__label label" for="signUpUsername">
          Username
        </label>
        <input
          v-model="username"
          type="text"
          id="signUpUsername"
          placeholder="Your email..."
          class="sign-up__input input"
        />
      </div>
      <div class="sign-up__form-item">
        <label class="sign-up__label label" for="signUpEmail">Email</label>
        <input
          v-model="email"
          type="text"
          id="signUpEmail"
          placeholder="Your email..."
          class="sign-up__input input"
        />
      </div>
      <div class="sign-up__form-item">
        <label class="sign-up__label label" for="signUpPassword">
          Password
        </label>
        <input
          v-model="password"
          type="password"
          id="signUpPassword"
          placeholder="Your password..."
          class="sign-up__input input"
        />
      </div>
      <div class="sign-up__form-item">
        <label class="sign-up__label label" for="signUpRetryPassword">
          Retry Password
        </label>
        <input
          v-model="retryPassword"
          type="password"
          id="signUpRetryPassword"
          placeholder="Your password..."
          class="sign-up__input input"
        />
      </div>
      <button type="button" class="sign-up__button" @click="handleSubmit">
        Submit
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from 'vue'
import { authApi } from '@/api/auth.api'
import { UserType } from '@/types/user.type'

export default defineComponent({
  name: 'SignUp',
  setup() {
    const username = ref<string>()
    const email = ref<string>()
    const password = ref<string | number>()
    const retryPassword = ref<string | number>()

    const signUpData: UserType = reactive({
      username,
      email,
      password,
    })

    const handleSubmit = async (): Promise<void> => {
      try {
        await authApi.signUp(signUpData)
      } catch (error) {
        console.error(error.response.data)
      }
    }

    return {
      handleSubmit,
      retryPassword,
      ...toRefs(signUpData),
    }
  },
})
</script>

<style scoped lang="scss">
.sign-up {
  &__form {
    &-item {
      margin: 1rem 0;
    }
  }

  &__label {
    margin-bottom: 0.5rem;
  }

  &__button {
    border-radius: 10px;
    padding: 8px 16px;
    font-size: 18px;
    color: $color-white;
    background-color: $color-accent;
  }
}
</style>
