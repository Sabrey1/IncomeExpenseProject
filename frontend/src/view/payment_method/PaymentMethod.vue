<template>
  <ion-content class="ion-padding">
    <h2>Payment Method</h2>
    <div class="card">
        
       <DataTable :value="paymentMethod" stripedRows  tableStyle="min-width: 50rem">
            <Column header="No">
                <template #body="slotProps">
                    {{ slotProps.index + 1 }}
                </template>
            </Column>
            <Column field="name" header="Name"></Column> 
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

import { usePaymentMethod } from "@/composable/usePaymentMethod.js"
const { paymentMethod,
    getPaymentMethodList } = usePaymentMethod()

onMounted(() => {
  getPaymentMethodList()
})
</script>