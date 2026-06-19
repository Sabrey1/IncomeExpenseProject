<template>
  <ion-content>
    <main class="min-h-full bg-emerald-50/60 px-4 py-6 sm:px-6 lg:px-8">
      <section class="mx-auto max-w-7xl">
        <div class="mb-6 overflow-hidden rounded-lg bg-gradient-to-r from-emerald-700 to-teal-600 p-6 text-white shadow-lg">
          <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
              <p class="m-0 text-sm font-extrabold uppercase text-emerald-100">Revenue</p>
              <h1 class="m-0 mt-2 text-3xl font-extrabold">Income List</h1>
              <p class="mt-2 text-sm text-emerald-50">Review incoming money by type and payment method.</p>
            </div>
            <div class="rounded-lg bg-white/15 px-5 py-3">
              <p class="m-0 text-sm text-emerald-50">Total amount</p>
              <p class="m-0 mt-1 text-2xl font-extrabold">{{ formatMoney(totalIncome) }}</p>
            </div>
          </div>
        </div>

        <div class="rounded-lg border border-emerald-100 bg-white shadow-sm">
          <div class="flex flex-col gap-3 border-b border-emerald-100 p-4 sm:flex-row sm:items-center sm:justify-between">
            <input
              v-model="search"
              class="min-h-11 w-full rounded-lg border border-slate-300 px-3 text-sm outline-none transition focus:border-emerald-600 focus:shadow-[0_0_0_4px_rgba(5,150,105,0.12)] sm:max-w-sm"
              type="search"
              placeholder="Search income"
            />
            <Button label="Add Income" severity="success" class="w-full sm:w-auto" />
          </div>

          <DataTable :value="filteredIncome" :loading="loading" stripedRows responsiveLayout="scroll" tableStyle="min-width: 58rem">
            <template #empty>
              <div class="py-8 text-center text-sm font-semibold text-slate-500">No income found.</div>
            </template>
            <Column header="No" style="width: 80px">
              <template #body="slotProps">{{ slotProps.index + 1 }}</template>
            </Column>
            <Column field="title" header="Title" sortable>
              <template #body="slotProps">
                <span class="font-bold text-slate-900">{{ slotProps.data.title }}</span>
              </template>
            </Column>
            <Column field="income_type_id" header="Income Type" />
            <Column field="payment_method_id" header="Payment Method" />
            <Column field="amount" header="Amount" sortable>
              <template #body="slotProps">
                <span class="font-extrabold text-emerald-700">{{ formatMoney(slotProps.data.amount) }}</span>
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
import { useIncome } from "@/composable/useIncome.js"

const { income, loading, getIncomeList } = useIncome()
const search = ref('')

const totalIncome = computed(() => {
  return income.value.reduce((sum, item) => sum + Number(item.amount || 0), 0)
})

const formatMoney = (value: number | string) => {
  return `$${Number(value || 0).toLocaleString()}`
}

const filteredIncome = computed(() => {
  const keyword = search.value.trim().toLowerCase()
  if (!keyword) return income.value

  return income.value.filter((item) => {
    return [item.title, item.income_type_id, item.payment_method_id, item.amount]
      .filter(Boolean)
      .some((value) => String(value).toLowerCase().includes(keyword))
  })
})

onMounted(() => {
  getIncomeList()
})
</script>
