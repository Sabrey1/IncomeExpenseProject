<template>
  <div>
    <ion-menu content-id="main-content" class="app-menu">
      <ion-content>
        <aside class="flex min-h-full flex-col bg-white">
          <div class="border-b border-slate-200 px-5 py-5">
            <div class="flex items-center gap-3">
              <div
                class="grid h-11 w-11 place-items-center rounded-lg bg-gradient-to-br from-teal-700 to-blue-600 text-base font-extrabold text-white"
              >
                IE
              </div>
              <div>
                <h1 class="m-0 text-base font-extrabold text-slate-950">Finance App</h1>
                <p class="m-0 text-xs font-semibold text-slate-500">Income and expense</p>
              </div>
            </div>
          </div>

          <nav class="flex-1 px-3 py-4">
            <p class="mb-2 px-3 text-xs font-extrabold uppercase text-slate-400">Menu</p>

            <button
              v-for="item in menuItems"
              :key="item.to"
              class="mb-1 flex min-h-11 w-full items-center gap-3 rounded-lg px-3 text-left text-sm font-bold transition"
              :class="isActiveRoute(item.to)
                ? 'bg-teal-50 text-teal-700'
                : 'text-slate-600 hover:bg-slate-100 hover:text-slate-950'"
              type="button"
              @click="handleMenuClick(item.to)"
            >
              <span
                class="grid h-9 w-9 place-items-center rounded-lg"
                :class="isActiveRoute(item.to) ? 'bg-teal-100 text-teal-700' : 'bg-slate-100 text-slate-500'"
              >
                <ion-icon :icon="item.icon" class="text-lg" />
              </span>
              <span>{{ item.label }}</span>
            </button>
          </nav>

          <div class="border-t border-slate-200 p-3">
            <button
              class="flex min-h-11 w-full items-center gap-3 rounded-lg px-3 text-left text-sm font-bold text-red-600 transition hover:bg-red-50"
              type="button"
              @click="handleLogout"
            >
              <span class="grid h-9 w-9 place-items-center rounded-lg bg-red-50 text-red-600">
                <ion-icon :icon="logOutOutline" class="text-lg" />
              </span>
              <span>Logout</span>
            </button>
          </div>
        </aside>
      </ion-content>
    </ion-menu>

    <ion-page id="main-content">
      <ion-header>
        <ion-toolbar class="app-toolbar">
          <ion-buttons slot="start">
            <ion-menu-button />
          </ion-buttons>
          <ion-title>{{ currentTitle }}</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content>
        <router-view />
      </ion-content>
    </ion-page>
  </div>
</template>

<script setup lang="ts">
import {
  IonButtons,
  IonContent,
  IonHeader,
  IonIcon,
  IonMenu,
  IonMenuButton,
  IonPage,
  IonTitle,
  IonToolbar,
  menuController
} from '@ionic/vue'
import {
  cardOutline,
  cashOutline,
  gridOutline,
  logOutOutline,
  peopleOutline,
  pricetagsOutline,
  receiptOutline,
  shieldCheckmarkOutline,
  swapHorizontalOutline,
  trendingUpOutline,
  walletOutline
} from 'ionicons/icons'
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuth } from '@/composable/useAuth'

const router = useRouter()
const route = useRoute()
const { logout } = useAuth()

const menuItems = [
  { label: 'Dashboard', to: '/dashboard', icon: gridOutline },
  { label: 'Currency', to: '/currency', icon: cashOutline },
  { label: 'Exchange Rate', to: '/exchange_rate', icon: swapHorizontalOutline },
  { label: 'Expense', to: '/expense', icon: receiptOutline },
  { label: 'Expense Type', to: '/expense-type', icon: pricetagsOutline },
  { label: 'Income', to: '/income', icon: trendingUpOutline },
  { label: 'Income Type', to: '/income-type', icon: walletOutline },
  { label: 'Payment Method', to: '/payment-method', icon: cardOutline },
  { label: 'Role', to: '/role', icon: shieldCheckmarkOutline },
  { label: 'User', to: '/user', icon: peopleOutline },
]

const currentTitle = computed(() => {
  return menuItems.find((item) => item.to === route.path)?.label || 'App'
})

const isActiveRoute = (path: string) => {
  return route.path === path
}

const handleMenuClick = async (path: string) => {
  await menuController.close()

  if (route.path !== path) {
    router.push(path)
  }
}

const handleLogout = async () => {
  logout()
  await menuController.close()
  router.push('/login')
}
 
</script>

<style scoped>
.app-menu {
  --width: 292px;
}

.app-toolbar {
  --background: #ffffff;
  --border-color: #e2e8f0;
  --color: #0f172a;
}
</style>
