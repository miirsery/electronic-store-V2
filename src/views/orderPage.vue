<template>
  <h2 class="title mb-8 mt-4 font-bold text-2xl">Страница заказа</h2>
  <form
    class="max-w-2xl"
    @submit.prevent="sendForm"
    novalidate
  >
    <div class="order__contacts mb-6">
      <label
        for="name"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"

      >Ваше имя</label
      >
      <input
        type="text"
        id="name"
        v-model="form.name"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Введите имя" required>
      <label
        for="surname"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"
      >Ваша фамилия</label
      >
      <input
        type="text"
        id="surname"
        v-model="form.surname"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Введите фамилию" required>
      <label
        for="phone"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"
      >Ваш телефон</label
      >
      <input
        type="text"
        id="phone"
        v-model="form.phone"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Введите номер телефона " required>
      <div class="delivery-type flex items-center mt-6">
        <button
          @click="toggleType"
          :class="{ 'bg-blue-700': delivery }"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-6"
          type="button"
          :disabled="disabled"
        >Доставка
        </button>
        <button
          @click="toggleType"
          :class="{ 'bg-blue-700': !delivery }"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="button"
          :disabled="!disabled"
        >Самовывоз
        </button>
      </div>

    </div>
    <div class="delivery" v-if="delivery" id="delivery">
      <label
        for="address"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"
      >Ваш адрес</label>
      <input
        type="text"
        id="address"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Введите адрес доставки"
        required
      />
      <label
        for="additionalInformation"
        class="block mb-2 mt-4 text-sm font-medium text-gray-900 dark:text-gray-300"
      >Дополнительная информация</label>
      <textarea id="additionalInformation" class="resize-none rounded-md w-full">
      </textarea>
    </div>
    <div class="pickup" v-if="!delivery" id="pickup">

    </div>
    <button
      type="submit"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-6"
    >
      Оформить заказ
    </button>
  </form>
</template>

<script>

export default {
  data() {
    return {
      delivery: true,
      disabled: true,
      form: {
        name: this.name,
        surname: this.surname,
        phone: this.phone
      }
    };
  },
  methods: {
    toggleType() {
      this.delivery = !this.delivery;
      this.disabled = !this.disabled;
    },
    redirect() {
      this.$router.push("/");
    },
    async sendForm() {
      console.log("Отправка JSON", this.form);
      try {
        const data = (
          await this.$api.order.sendOrder({
            name: this.form.name,
            surname: this.form.surname,
            phone: this.form.phone
          })
        ).data;
        console.log(data);
      } catch (error) {
        console.log(error.response.data);
      }
    }
  }
};
</script>

<style scoped lang="sass">

</style>
