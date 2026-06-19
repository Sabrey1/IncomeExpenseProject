<template>
  <ion-content class="ion-padding">
    <h2>Expense List</h2>
    <div class="card">
       <DataTable :value="expense" stripedRows  tableStyle="min-width: 50rem">
            <Column header="No">
                <template #body="slotProps">
                    {{ slotProps.index + 1 }}
                </template>
            </Column>
            <Column field="title" header="Title"></Column> 
            <Column field="expense_type_id" header="Expense Type"></Column> 
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

import { useExpense } from "@/composable/useExpense.js"
const { expense,
    getExpenseList } = useExpense()

onMounted(() => {
  getExpenseList()
})
</script>