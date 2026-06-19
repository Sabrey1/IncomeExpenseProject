<template>
  <ion-content class="ion-padding">
    <h2>Exchange Rate</h2>
    <div class="card">
       <DataTable :value="exchangeRate" stripedRows  tableStyle="min-width: 50rem">
            <Column header="No">
                <template #body="slotProps">
                    {{ slotProps.index + 1 }}
                </template>
            </Column>
            <Column field="from_currency_id" header="From Currency"></Column> 
            <Column field="to_currency_id" header="To Currency"></Column> 
            <Column field="rate" header="Rate"></Column> 
            <Column header="Action">
                <template #body="slotProps">
                    <div class="flex gap-2 h-full">
                        <Button severity="info">Edit</Button>
                        <Button severity="danger">Delete</Button>
                    </div>
                </template>
            </Column>
        </DataTable>
    </div>
  </ion-content>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { IonContent } from '@ionic/vue'

import { useExchangeRate } from "@/composable/useExchangeRate.js"
const {exchangeRate,
    getExchangeRateList } = useExchangeRate()

onMounted(() => {
  getExchangeRateList()
})
</script>