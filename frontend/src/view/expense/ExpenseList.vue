<template>
  <ion-content>
    <main class="min-h-full bg-slate-50 px-4 py-6 sm:px-6 lg:px-8">
      <section class="mx-auto max-w-7xl">
        <div class="mb-6 rounded-lg border border-rose-100 bg-white p-5 shadow-sm">
          <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
              <p class="mb-1 text-sm font-extrabold uppercase text-rose-600">Spending</p>
              <h1 class="m-0 text-3xl font-extrabold text-slate-950">Expenses</h1>
              <p class="mt-2 text-sm text-slate-500">Track outgoing money by type, method, and amount.</p>
            </div>
            <Button label="Add Expense" severity="danger" class="w-full md:w-auto" />
          </div>
        </div>

        <div class="mb-4 flex flex-col gap-3 rounded-lg border border-slate-200 bg-white p-4 shadow-sm sm:flex-row sm:items-center sm:justify-between">
          <input
            v-model="search"
            class="min-h-11 w-full rounded-lg border border-slate-300 px-3 text-sm outline-none transition focus:border-rose-500 focus:shadow-[0_0_0_4px_rgba(244,63,94,0.12)] sm:max-w-sm"
            type="search"
            placeholder="Search expense"
          />
          <div class="rounded-lg bg-rose-50 px-4 py-2 text-sm font-bold text-rose-700">
            {{ filteredExpense.length }} records
          </div>
        </div>

        <div class="rounded-lg border border-slate-200 bg-white shadow-sm">
          <DataTable :value="filteredExpense" :loading="loading" stripedRows responsiveLayout="scroll" tableStyle="min-width: 58rem">
            <template #empty>
              <div class="py-8 text-center text-sm font-semibold text-slate-500">No expense found.</div>
            </template>
            <Column header="#" style="width: 70px">
              <template #body="slotProps">{{ slotProps.index + 1 }}</template>
            </Column>
            <Column field="title" header="Title" sortable>
              <template #body="slotProps">
                <span class="font-bold text-slate-900">{{ slotProps.data.title }}</span>
              </template>
            </Column>
            <Column field="expense_type_id" header="Expense Type" />
            <Column field="payment_method_id" header="Payment Method" />
            <Column field="amount" header="Amount" sortable>
              <template #body="slotProps">
                <span class="font-extrabold text-rose-600">{{ formatMoney(slotProps.data.amount) }}</span>
              </template>
            </Column>
            <Column header="Action" style="width: 190px">
              <template #body>
                <div class="flex gap-2">
                  <Button label="Edit" severity="info" size="small" outlined />
                  <Button label="Delete" severity="danger" size="small" outlined />
                </div>
              </template>
            </Column>
          </DataTable>
        </div>
      </section>
    </main>
  </ion-content>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { IonContent } from '@ionic/vue'
import { useExpense } from "@/composable/useExpense.js"

const { expense, loading, getExpenseList } = useExpense()
const search = ref('')

const formatMoney = (value: number | string) => {
  return `$${Number(value || 0).toLocaleString()}`
}

const filteredExpense = computed(() => {
  const keyword = search.value.trim().toLowerCase()
  if (!keyword) return expense.value

  return expense.value.filter((item) => {
    return [item.title, item.expense_type_id, item.payment_method_id, item.amount]
      .filter(Boolean)
      .some((value) => String(value).toLowerCase().includes(keyword))
  })
})

onMounted(() => {
  getExpenseList()
})
</script>
