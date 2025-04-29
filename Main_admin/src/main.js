
// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css"; // Ensure you are using css-loader



import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

//router
import router from "./route/index.js"


const vuetify=createVuetify({
    components,
    directives,
    icons: {
        defaultSet: "mdi", // This is already the default value - only for display purposes
      },
})

const app=createApp(App)
app.use(vuetify)
app.use(router)
app.mount('#app')
