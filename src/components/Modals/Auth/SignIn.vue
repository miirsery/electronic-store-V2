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
import { UserType } from '@/types/user.type'
import { useStore } from 'vuex'
import { MutationTypes } from '@/store/store'

export default defineComponent({
  name: 'SignIn',
  emits: ['close'],
  setup(_, { emit }) {
    const email = ref<string>()
    const password = ref<string | number>()
    const store = useStore()

    const signInData: Partial<Omit<UserType, 'username'>> = reactive({
      email,
      password,
    })

    const saveToken = async (token): Promise<void> => {
      localStorage.setItem('tokenData', JSON.stringify(token))
      await signIn(token)
    }

    const tokenCreate = async (): Promise<void> => {
      const [_, tokenData] = await authApi.tokenCreate(signInData)
      await saveToken(tokenData.token)
    }
    const setProfileImage = async (avatar): Promise<void> => {
      store.commit(MutationTypes.SET_PROFILE_IMAGE, avatar)
    }

    const signIn = async (token): Promise<void> => {
      const [_, responseData] = await authApi.signIn(token)
      await setProfileImage(responseData.avatar)
      store.commit(MutationTypes.TOGGLE_AUTHORIZATION, true)
    }

    const closeModal = async (): Promise<void> => {
      emit('close')
    }

    const handleSubmit = async (): Promise<void> => {
      await tokenCreate()
      await closeModal()
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

  &__button {
    border-radius: 10px;
    padding: 8px 16px;
    font-size: 18px;
    color: $color-white;
    background-color: $color-accent;
  }
}
</style>
