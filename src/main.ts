import { createApp } from 'vue'
import { createVuetify } from 'vuetify/'
import App from './App.vue'
import router from './router'

import * as components from 'vuetify/lib/components/index'
import * as directives from 'vuetify/lib/directives/index'
import * as icons from 'vuetify/lib/index'
import 'vuetify/lib/styles/main.sass'
import IconTemplate from '@/components/IconTemplate.vue'
import '@/styles/main.scss'

const app = createApp(App)
const vuetify = createVuetify({
  components,
  directives,
})

app.use(vuetify)
app.use(router).mount('#app')

const requireAll = (requireContext) => requireContext.keys().map(requireContext)
requireAll(require.context('@/assets/icons/', true, /\.svg$/))
app.component('IconTemplate', IconTemplate)
