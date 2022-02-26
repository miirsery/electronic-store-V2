<template>
  <h2 class="title mb-8 mt-4 font-bold text-2xl">Страница заказа</h2>
  <a
    @click="redirect"
    class="ml-2 cursor-pointer text-lg leading-6 font-medium text-gray-900"
  >
    Вернуться назад
  </a>
  <Form
    @submit="onSubmit"
    :validation-schema="schema"
    @invalid-submit="onInvalidSubmit"
  >
    <TextInput
      name="orderName"
      type="text"
      label="Имя"
      placeholder="Ваше имя"
      success-message="Nice to meet you!"
    />
    <TextInput
      name="orderSurname"
      type="text"
      label="Фамилия"
      placeholder="Ваша фамилия"
      success-message="Nice to meet you!"
    />
    <TextInput
      name="orderPhone"
      type="text"
      label="phone"
      placeholder="Ваш телефон"
    />
    <div class="delivery-type flex items-center mb-6 mt-6">
      <button
        @click="toggleType"
        :class="{ 'bg-blue-700': delivery }"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-6"
        type="button"
        :disabled="delivery"
      >
        Доставка
      </button>
      <button
        @click="toggleType"
        :class="{ 'bg-blue-700': !delivery }"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        type="button"
        :disabled="!delivery"
      >
        Самовывоз
      </button>
    </div>
    <div class="delivery" v-if="delivery" id="delivery">
      <TextInput
        name="orderAddress"
        type="text"
        label="Адрес доставки"
        placeholder="Введите адрес доставки"
        success-message="Адрес найден!"
      />
      <label
        for="additionalInformation"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"
        >Дополнительная информация</label
      >
      <textarea
        id="additionalInformation"
        class="resize-none rounded-md w-full"
      />
    </div>
    <button
      class="submit-btn bg-indigo-400 pt-2 pb-2 pr-4 pl-4 text-xl text-white font-bold uppercase hover:bg-indigo-500"
      type="submit"
    >
      Подтвердить
    </button>
  </Form>
</template>

<script>
import { Form } from "vee-validate";
import TextInput from "@/components/UI/TextInput";
import * as Yup from "yup";

export default {
  components: {
    Form,
    TextInput,
  },
  data() {
    let schemaData = {
      orderName: Yup.string().required(),
      orderSurname: Yup.string().required(),
      orderPhone: Yup.string().required(),
      orderAddress: Yup.string().min(6).required(),
    };
    return {
      delivery: true,
      schema: schemaData,
      schemaData,
    };
  },
  methods: {
    toggleType() {
      console.log(this.schema);
      this.delivery = !this.delivery;
      this.schema = this.changeSchema(this.delivery);
    },
    redirect() {
      this.$router.push("/");
    },
    async onSubmit(data) {
      console.log("Отправка JSON", data);
      try {
        const responseData = (await this.$api.order.sendOrder(data)).data;
        console.log(responseData);
      } catch (error) {
        console.log(error.response.data);
      }
    },
    onInvalidSubmit() {
      const submitBtn = document.querySelector(".submit-btn");
      submitBtn.classList.add("invalid");
      setTimeout(() => {
        submitBtn.classList.remove("invalid");
      }, 1000);
    },
    changeSchema(delivery) {
      const newData = this.schemaData;
      if (!delivery) {
        newData["orderAddress"] = Yup.string().min(6);
      }
      return Yup.object().shape(newData);
    },
  },
};
</script>

<style scoped lang="sass"></style>
