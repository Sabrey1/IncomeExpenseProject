<template>
  <ion-content>
    <main class="min-h-full bg-zinc-50 px-4 py-6 sm:px-6 lg:px-8">
      <section class="mx-auto max-w-6xl">
        <div class="mb-6 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h1 class="m-0 text-3xl font-extrabold text-zinc-950">Expense Types</h1>
            <p class="mt-2 text-sm text-zinc-500">Group spending into readable categories.</p>
          </div>
          <Button label="Add Expense Type" severity="success" class="w-full sm:w-auto" />
        </div>

        <div class="grid gap-4 lg:grid-cols-[280px_1fr]">
          <aside class="rounded-lg border border-zinc-200 bg-white p-4 shadow-sm">
            <p class="m-0 text-sm font-bold text-zinc-500">Category count</p>
            <p class="m-0 mt-2 text-4xl font-extrabold text-zinc-950">{{ expenseType.length }}</p>
            <input
              v-model="search"
              class="mt-5 min-h-11 w-full rounded-lg border border-zinc-300 px-3 text-sm outline-none transition focus:border-emerald-600 focus:shadow-[0_0_0_4px_rgba(5,150,105,0.12)]"
              type="search"
              placeholder="Search type"
            />
          </aside>

          <div class="rounded-lg border border-zinc-200 bg-white shadow-sm">
            <DataTable :value="filteredExpenseType" :loading="loading" stripedRows responsiveLayout="scroll" tableStyle="min-width: 44rem">
              <template #empty>
                <div class="py-8 text-center text-sm font-semibold text-zinc-500">No expense type found.</div>
              </template>
              <Column header="No" style="width: 80px">
                <template #body="slotProps">{{ slotProps.index + 1 }}</template>
              </Column>
              <Column field="name" header="Name" sortable>
                <template #body="slotProps">
                  <span class="font-extrabold text-zinc-900">{{ slotProps.data.name }}</span>
                </template>
              </Column>
              <Column field="description" header="Description">
                <template #body="slotProps">{{ slotProps.data.description || '-' }}</template>
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
        </div>
      </section>
    </main>
  </ion-content>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { IonContent } from '@ionic/vue'
import { useExpenseType } from "@/composable/useExpenseType.js"

const { expenseType, loading, getExpenseList } = useExpenseType()
const search = ref('')

const filteredExpenseType = computed(() => {
  const keyword = search.value.trim().toLowerCase()
  if (!keyword) return expenseType.value

  return expenseType.value.filter((item) => {
    return [item.name, item.description]
      .filter(Boolean)
      .some((value) => String(value).toLowerCase().includes(keyword))
  })
})

onMounted(() => {
  getExpenseList()
})
</script>
