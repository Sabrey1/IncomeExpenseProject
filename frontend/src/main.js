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
import Button from 'primevue/button';
 
import InputText from "primevue/inputtext";
import InputIcon from "primevue/inputicon";
import IconField from "primevue/iconfield";
import Tag from "primevue/tag";


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
app.component('Button', Button);
app.component('InputText', InputText);
app.component('InputIcon', InputIcon);
app.component('IconField', IconField);
app.component('Tag', Tag);


router.isReady().then(() => {
  app.mount('#app')
})
