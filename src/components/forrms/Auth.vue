<template>
  <transition name="modal">
    <div class="modal-mask" v-if="showModal">
      <div class="modal-wrapper" @click="$emit('close')">
        <div class="modal-container" @click.stop>
          <div class="modal-header mb-3 flex justify-between">
            <slot name="header">
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
                  type="text"
                  label="Введите логин"
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
import instance from "@/api/instance";

export default {
  props: {
    showModal: Boolean
  },
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
      schemaData,
      isAuth: false
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
    async test() {
      await this.$api.auth.test()
    },
    async signIn(data) {
      try {
        const responseData = (await this.$api.auth.signIn(data)).data;
        this.$store.dispatch("user/setUser");
        this.$store.dispatch("user/IS_AUTH", true);
        this.$emit("close");
        this.saveToken(responseData);
      } catch (error) {
        console.log(error.response.data);
      }
    },

    async signUp(data) {
      console.log(data);
      try {
        delete data.confirmPassword;
        const newData = {
          username: data.signUpUsername,
          password: data.signUpPassword,
          email: data.signUpEmail
        };
        let responseData = (await this.$api.auth.signUp(newData)).data;
        console.log(responseData);
        console.log("Success");
        this.$emit("close");
      } catch (error) {
        console.log(error.response.data);
      }
    },
    logout() {
      this.$api.auth.logout();
      localStorage.removeItem("user");
      this.$store.dispatch("user/deleteUser");
      this.$store.dispatch("user/IS_AUTH", false);
      this.$router.push({ name: "home" });
    },
    saveToken(token) {
      sessionStorage.setItem("tokenData", JSON.stringify(token.token));
      instance.defaults.headers.common['Authorization'] = `Bearer ${token.token}`
      this.test()
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

.modal-enter-active {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  transform: scale(1.1);
}
</style>
