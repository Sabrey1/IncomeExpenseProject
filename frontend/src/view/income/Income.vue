<template>
  <ion-content class="ion-padding">
    <h2>Income List</h2>
    <div class="card">
       <DataTable :value="income" stripedRows  tableStyle="min-width: 50rem">
            <Column header="No">
                <template #body="slotProps">
                    {{ slotProps.index + 1 }}
                </template>
            </Column>
            <Column field="title" header="Title"></Column> 
            <Column field="income_type_id" header="Income Type"></Column> 
            <Column field="payment_method_id" header="Payment Method"></Column>
            <Column field="amount" header="Amount"></Column> 
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

import { useIncome } from "@/composable/useIncome.js"
const { income,
    getIncomeList } = useIncome()

onMounted(() => {
  getIncomeList()
})
</script>