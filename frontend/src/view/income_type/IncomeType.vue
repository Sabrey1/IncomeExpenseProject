<template>
  <ion-content>
    <main class="min-h-full bg-slate-50 px-4 py-6 sm:px-6 lg:px-8">
      <section class="mx-auto max-w-7xl">
        <div class="mb-6 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h1 class="m-0 text-2xl font-extrabold text-slate-950 sm:text-3xl">Income Type</h1>
            <p class="mt-2 text-sm text-slate-500">
              Organize income categories for cleaner reports and faster entry.
            </p>
          </div>

          <Button label="Add Income Type" severity="success" class="w-full sm:w-auto" />
        </div>

        <div class="rounded-lg border border-slate-200 bg-white shadow-sm">
          <div class="flex flex-col gap-3 border-b border-slate-200 p-4 sm:flex-row sm:items-center sm:justify-between">
            <div class="relative w-full sm:max-w-xs">
              <span class="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">⌕</span>
              <input
                v-model="search"
                class="min-h-11 w-full rounded-lg border border-slate-300 bg-white pl-10 pr-3 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-700 focus:shadow-[0_0_0_4px_rgba(15,118,110,0.12)]"
                type="search"
                placeholder="Search income type"
              />
            </div>
            <div>
              <p class="mt-1 text-sm text-slate-500">{{ filteredIncomeType.length }} records found</p>
            </div>

            
          </div>

          <DataTable
            :value="filteredIncomeType"
            :loading="loading"
            stripedRows
            responsiveLayout="scroll"
            tableStyle="min-width: 52rem"
          >
            <template #empty>
              <div class="py-8 text-center text-sm font-semibold text-slate-500">
                No income type found.
              </div>
            </template>

            <Column header="No" style="width: 90px">
              <template #body="slotProps">
                <span class="font-semibold text-slate-600">{{ slotProps.index + 1 }}</span>
              </template>
            </Column>

            <Column field="name" header="Name" sortable>
              <template #body="slotProps">
                <span class="font-bold text-slate-900">{{ slotProps.data.name }}</span>
              </template>
            </Column>

            <Column field="description" header="Description">
              <template #body="slotProps">
                <span class="text-slate-600">{{ slotProps.data.description || '-' }}</span>
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
import { computed, ref, onMounted } from 'vue'
import { IonContent } from '@ionic/vue'

import { useIncomeType } from "@/composable/useIncomeType.js"
const { incomeType,
    loading,
    getIncomeTypeList } = useIncomeType()

const search = ref('')

const filteredIncomeType = computed(() => {
  const keyword = search.value.trim().toLowerCase()

  if (!keyword) {
    return incomeType.value
  }

  return incomeType.value.filter((item) => {
    return [item.name, item.description]
      .filter(Boolean)
      .some((value) => String(value).toLowerCase().includes(keyword))
  })
})

onMounted(() => {
  getIncomeTypeList()
})
</script>
