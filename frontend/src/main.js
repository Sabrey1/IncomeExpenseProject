import { createApp } from 'vue'
import App from './App.vue'

import { IonicVue } from '@ionic/vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';

import '@ionic/vue/css/core.css'
import '@ionic/vue/css/normalize.css'
import '@ionic/vue/css/structure.css'
import '@ionic/vue/css/typography.css'
import '@ionic/vue/css/padding.css'
import '@ionic/vue/css/float-elements.css'
import '@ionic/vue/css/text-alignment.css'
import '@ionic/vue/css/text-transformation.css'
import '@ionic/vue/css/flex-utils.css'
import '@ionic/vue/css/display.css'

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';


import './style.css'

const app = createApp(App)

app.use(IonicVue)
app.use(router)

app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

app.component('DataTable', DataTable);
app.component('Column', Column);

router.isReady().then(() => {
  app.mount('#app')
})
