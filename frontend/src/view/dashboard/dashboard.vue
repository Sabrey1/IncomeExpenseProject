<template>
  <ion-content class="ion-padding">
    <h2>Dashboard</h2>
    <p>Welcome to the dashboard page.</p>
    <div class="card">
       <DataTable :value="products" tableStyle="min-width: 50rem">
            <Column field="code" header="Code"></Column>
            <Column field="name" header="Name"></Column>
            <Column field="category" header="Category"></Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
    </div>
  </ion-content>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { IonContent } from '@ionic/vue'

const products = ref(
    [{
        code: 'P001',
        name: 'Product 1',
        category: 'Category 1',
        quantity: 10
    }]
);
</script>