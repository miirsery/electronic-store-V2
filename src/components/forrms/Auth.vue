<template>
  <!--  <transition name="modal">-->
  <!--    <div class="modal-mask">-->
  <!--      <div class="modal-wrapper" @click="$emit('close')">-->
  <!--        <div-->
  <!--          class="modal fixed absolute bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 z-10"-->
  <!--        >-->
  <!--          <div class="modal__top mb-3 flex justify-between">-->
  <!--            <div class="buttons flex flex-col">-->
  <!--              <button-->
  <!--                :class="{ active: mode === 'signIn' }"-->
  <!--                type="button"-->
  <!--                @click="mode = isSignInForm ? 'signUp' : 'signIn'"-->
  <!--                :disabled="isSignInForm"-->
  <!--              >-->
  <!--                Вход /-->
  <!--              </button>-->
  <!--              <button-->
  <!--                :class="{ active: mode === 'signUp' }"-->
  <!--                type="button"-->
  <!--                @click="mode = isSignInForm ? 'signUp' : 'signIn'"-->
  <!--                :disabled="!isSignInForm"-->
  <!--              >-->
  <!--                Регистрация-->
  <!--              </button>-->
  <!--            </div>-->
  <!--            <button type="button" @click="auth = true">X</button>-->
  <!--          </div>-->
  <!--          <Form-->
  <!--            @submit="onSubmit"-->
  <!--            :validation-schema="schemaSignIn"-->
  <!--            @invalid-submit="onInvalidSubmit"-->
  <!--            v-if="mode === 'signIn'"-->
  <!--          >-->
  <!--            <TextInput-->
  <!--              name="name"-->
  <!--              type="text"-->
  <!--              label="Username"-->
  <!--              placeholder="Your username"-->
  <!--              success-message="Nice to meet you!"-->
  <!--            />-->
  <!--            <TextInput-->
  <!--              name="password"-->
  <!--              type="password"-->
  <!--              label="Password"-->
  <!--              placeholder="Your password"-->
  <!--              success-message="Nice and secure!"-->
  <!--            />-->
  <!--            <button-->
  <!--              class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"-->
  <!--              type="submit"-->
  <!--            >-->
  <!--              Подтвердить-->
  <!--            </button>-->
  <!--          </Form>-->
  <!--          <Form-->
  <!--            @submit="onSubmit"-->
  <!--            :validation-schema="schema"-->
  <!--            @invalid-submit="onInvalidSubmit"-->
  <!--            v-if="mode === 'signUp'"-->
  <!--          >-->
  <!--            <TextInput-->
  <!--              name="name"-->
  <!--              type="text"-->
  <!--              label="Username"-->
  <!--              placeholder="Your username"-->
  <!--              success-message="Nice to meet you!"-->
  <!--            />-->
  <!--            <TextInput-->
  <!--              name="email"-->
  <!--              type="email"-->
  <!--              label="E-mail"-->
  <!--              placeholder="Your email address"-->
  <!--              success-message="Got it, we won't spam you!"-->
  <!--            />-->
  <!--            <TextInput-->
  <!--              name="password"-->
  <!--              type="password"-->
  <!--              label="Password"-->
  <!--              placeholder="Your password"-->
  <!--              success-message="Nice and secure!"-->
  <!--            />-->
  <!--            <TextInput-->
  <!--              name="confirm_password"-->
  <!--              type="password"-->
  <!--              label="Confirm Password"-->
  <!--              placeholder="Type it again"-->
  <!--              success-message="Glad you remembered it!"-->
  <!--            />-->
  <!--            <button-->
  <!--              class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"-->
  <!--              type="submit"-->
  <!--            >-->
  <!--              Подтвердить-->
  <!--            </button>-->
  <!--          </Form>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--  </transition>-->
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper" @click="$emit('close')">
        <div class="modal-container" @click.stop>
          <div class="modal-header mb-3 flex justify-between">
            <slot name="header">
              <!-- <div class="buttons flex flex-col justify-start justify-start">
                 <button class="block" type="button">Вход /</button>
                 <button class="block" type="button">Регистрация</button>
               </div>
               -->
              <el-tabs
                v-model="activeName"
                class="demo-tabs"
                @tab-click="handleClick"
              >
                <el-tab-pane label="Авторизация" name="signIn">Авторизация</el-tab-pane>
                <el-tab-pane label="Регистрация" name="signUp">Регистрация</el-tab-pane>
              </el-tabs>
              <button class="block" type="button" @click="$emit('close')">
                X
              </button>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <Form
                @submit="onSubmit"
                :validation-schema="schema"
                @invalid-submit="onInvalidSubmit"
                v-if="isSignInForm"
              >
                <TextInput
                  name="email"
                  type="email"
                  label="Почта"
                  placeholder="Введите почту"
                  success-message="Got it, we won't spam you!"
                />
                <TextInput
                  name="password"
                  type="password"
                  label="Пароль"
                  placeholder="Введите пароль"
                  success-message="Nice and secure!"
                />
                <button
                  class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"
                  type="submit"
                >
                  Подтвердить
                </button>
              </Form>
              <Form
                @submit="onSubmit"
                :validation-schema="schema"
                @invalid-submit="onInvalidSubmit"
                v-if="!isSignInForm"
              >
                <TextInput
                  name="signUpEmail"
                  type="email"
                  label="Почта"
                  placeholder="Введите почту"
                  success-message="Got it, we won't spam you!"
                />
                <TextInput
                  name="signUpUsername"
                  type="email"
                  label="Почта"
                  placeholder="Введите логин"
                  success-message="Got it, we won't spam you!"
                />
                <TextInput
                  name="signUpPassword"
                  type="password"
                  label="Пароль"
                  placeholder="Введите пароль"
                  success-message="Got it, we won't spam you!"
                />
                <TextInput
                  name="confirmPassword"
                  type="password"
                  label="Повторите пароль"
                  placeholder="Повторите пароль"
                  success-message="Got it, we won't spam you!"
                />
                <button
                  class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"
                  type="submit"
                >
                  Подтвердить
                </button>
              </Form>
            </slot>
          </div>
          <div class="modal-footer">
            <slot name="footer">
              default footer
              <button class="modal-default-button" @click="$emit('close')">
                OK
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { Form } from "vee-validate";
import TextInput from "@/components/UI/TextInput";
import * as Yup from "yup";
import { mapActions } from "vuex";
import { ref } from "vue";

export default {
  components: {
    Form,
    TextInput
  },
  data() {
    let schemaData = {
      email: Yup.string().required(),
      password: Yup.string().min(6).required()
    };
    let schema = Yup.object().shape(schemaData);
    return {
      mode: "signIn",
      activeName: ref("signIn"),
      schema,
      schemaData
    };
  },
  methods: {
    ...mapActions({
      setUser: "user/setUser",
      deleteUser: "user/deleteUser"
    }),
    handleClick(tab) {
      this.mode = tab.props.name;
      this.schema = this.changeSchema(tab.props.name);
      console.log(this.schema);
    },
    onInvalidSubmit() {
      const submitBtn = document.querySelector(".submit-btn");
      submitBtn.classList.add("invalid");
      setTimeout(() => {
        submitBtn.classList.remove("invalid");
      }, 1000);
    },
    onSubmit(values) {
      if (this.isSignInForm) this.signIn(values);
      else this.signUp(values);
    },
    changeSchema(name) {
      let newData = {};
      if (name === "signUp") {
        newData = {
          signUpEmail: Yup.string().email().required(),
          signUpUsername: Yup.string().min(6).required(),
          signUpPassword: Yup.string().min(6).required(),
          confirmPassword: Yup.string()
            .required()
            .oneOf([Yup.ref("signUpPassword")], "Passwords do not match")
        };
      }
      if (name === "signIn") {
        newData = this.schemaData;
      }
      return Yup.object().shape(newData);
    },
    async signIn(data) {
      console.log(data);
      try {
        const responseData = (await this.$api.auth.signIn(data)).data;
        console.log(responseData);
        localStorage.setItem("user", JSON.stringify(responseData));
        this.$store.dispatch("user/setUser");
        this.$emit("close");
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async signUp(data) {
      console.log(data);
      try {
        const responseData = (await this.$api.auth.signUp(data)).data;
        console.log(responseData);
        console.log(responseData);
        localStorage.setItem("user", JSON.stringify(responseData));
        this.$store.dispatch("user/setUser");
        this.$emit("close");
      } catch (error) {
        console.log(error.response.data);
      }
    }
  },
  computed: {
    isSignInForm() {
      return this.mode === "signIn";
    }
  }
};
</script>

<style scoped>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  background-color: #f4f5f7;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
