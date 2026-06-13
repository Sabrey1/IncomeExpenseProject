<template>
  <div>
    <ion-menu content-id="main-content">
      <ion-header>
        <ion-toolbar>
          <ion-title>Menu</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content>
        <ion-list>
          <router-link to="/dashboard">
            <ion-item >
              Dashboard
            </ion-item>
          </router-link>
          
          <router-link to="/currency">
            <ion-item >
              Currency
            </ion-item>
          </router-link>
          <router-link to="/exchange_rate">
            <ion-item >
              Exchange Rate
            </ion-item>
          </router-link>
          <router-link to="/expense">
            <ion-item >
              Expense
            </ion-item>
          </router-link>
          <router-link to="/expense-type">
            <ion-item >
              Expense Type
            </ion-item>
          </router-link>
          <router-link to="/income">
            <ion-item >
              Income
            </ion-item>
          </router-link>
          <router-link to="/income">
            <ion-item >
              Income
            </ion-item>
          </router-link>
          <router-link to="/income-type">
            <ion-item >
              Income Type
            </ion-item>
          </router-link>
          <router-link to="/payment-method">
            <ion-item >
              Payment Method
            </ion-item>
          </router-link>
          <router-link to="/role">
            <ion-item >
              Role
            </ion-item>
          </router-link>
          <router-link to="/user">
            <ion-item >
              User
            </ion-item>
          </router-link>

          <router-link to="/login">
            <ion-item>
              Logout
            </ion-item>
          </router-link>
        </ion-list>
      </ion-content>
    </ion-menu>

    <ion-page id="main-content">
      <ion-header>
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button />
          </ion-buttons>
          <ion-title>App</ion-title>
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
  IonItem,
  IonList,
  IonMenu,
  IonMenuButton,
  IonPage,
  IonTitle,
  IonToolbar,
  menuController
} from '@ionic/vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
 
</script>
