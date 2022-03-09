<template>
  <div class="settings" v-if="isUser.isAuth">
    <h2 class="settings__title">Настройки пользователя</h2>
    <hr />
    <div class="settings__content flex">
      <ul class="settings__categories w-1/6 mr-8">
        <li v-for="tab in tabs" :key="tab">
          <button @click="currentTab = tab.tab" type="button" :class="['tab-button', {active: currentTab === tab.tab}]">
            {{ tab.name }}
          </button>
        </li>
      </ul>
      <div class="settings__fields w-2/3">
        <form>
          <div class="settings__wrapper flex">
            <keep-alive>
              <component :is="currentTabComponent" class="tab"></component>
            </keep-alive>
          </div>
          <button
            @click="onSubmit"
            type="button"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-6"
          >
            Update profile
          </button>
        </form>
      </div>
    </div>
  </div>
  <div v-else>Зарегистрируйтесь или войдите, чтобы настроить свой профиль.</div>
</template>

<script>
import SettingsGeneral from "@/components/ProfileSettings/SettingsGeneral.vue";
import SettingsContact from "@/components/ProfileSettings/SettingsContact.vue";

export default {
  name: "accountSettings",

  data() {
    return {
      currentTab: "SettingsGeneral",
      tabs: [
        {
          name: "Общие",
          tab: "SettingsGeneral"
        },
        {
          name: "Контакты",
          tab: "SettingsContact"
        }
      ],
      userData: {}
    };
  },
  components: {
    SettingsGeneral,
    SettingsContact
  },
  computed: {
    currentTabComponent() {
      return this.currentTab;
    },
    isUser() {
      return this.$store.state.user;
    }
  },
  methods: {
    onSubmit() {
      this.$api.user.updateProfile(this.userData);
    }
  }
};
</script>

<style scoped lang="sass">
.tab
  &-button
    width: 100%
    text-align: left
    padding: 12px 8px
    cursor: pointer
    background-color: #f0f0f0

    &:hover
      background-color: #e0e0e0

    &.active
      background-color: #cbcbcb

.settings
  &__input
    margin-bottom: 2rem

</style>
