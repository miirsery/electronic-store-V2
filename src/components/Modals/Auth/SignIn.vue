<template>
  <div class="sign-in">
    <form class="sign-in__form">
      <div class="sign-in__form-item">
        <label class="sign-in__label label" for="signInEmail">Email</label>
        <input
          v-model="email"
          type="text"
          id="signInEmail"
          placeholder="Your email..."
          class="sign-in__input input"
        />
      </div>
      <div class="sign-in__form-item">
        <label class="sign-in__label label" for="signInPassword">
          Password
        </label>
        <input
          v-model="password"
          type="password"
          id="signInPassword"
          placeholder="Your password..."
          class="sign-in__input input"
        />
      </div>
      <button type="button" class="sign-in__button" @click="handleSubmit">
        Submit
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from 'vue'
import { authApi } from '@/api/auth.api'
import axios from 'axios'

export default defineComponent({
  name: 'SignIn',
  setup() {
    const email = ref<string>()
    const password = ref<string>()

    const signInData = reactive({
      email,
      password,
    })

    const handleSubmit = async (): Promise<void> => {
      const sendSignInData = await authApi.signIn(signInData)
      // const sendSignInData = await axios({
      //   method: 'POST',
      //   url: 'http://localhost:8000/api/token-create',
      //   data: { email, password },
      // })
      console.log(sendSignInData)
    }

    return {
      ...toRefs(signInData),
      handleSubmit,
    }
  },
})
</script>

<style scoped lang="scss">
.sign-in {
  &__form {
    &-item {
      margin: 1rem 0;
    }
  }

  &__label {
    margin-bottom: 0.5rem;
  }
}
</style>
