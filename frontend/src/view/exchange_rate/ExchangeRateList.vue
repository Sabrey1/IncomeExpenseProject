<template>
  <ion-content>
    <main class="min-h-full bg-slate-50 px-4 py-6 sm:px-6 lg:px-8">
      <section class="mx-auto max-w-7xl">
        <div class="mb-6 grid gap-4 lg:grid-cols-[1fr_auto] lg:items-end">
          <div>
            <p class="mb-2 text-sm font-extrabold uppercase text-cyan-600">
              Market Setup
            </p>

            <h1 class="m-0 text-3xl font-extrabold text-slate-900">
              Exchange Rates
            </h1>

            <p class="mt-2 max-w-2xl text-sm text-slate-600">
              Keep conversion rates visible for transactions that move between
              currencies.
            </p>
          </div>

          <Button
            label="Add Rate"
            severity="info"
            class="w-full lg:w-auto"
          />
        </div>

        <!-- Statistics -->
        <div class="mb-5 grid gap-3 sm:grid-cols-3">
          <div
            class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
          >
            <p class="m-0 text-sm text-slate-500">Total Rates</p>
            <p class="m-0 mt-2 text-2xl font-extrabold text-slate-900">
              {{ exchangeRate.length }}
            </p>
          </div>

          <div
            class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
          >
            <p class="m-0 text-sm text-slate-500">Visible</p>
            <p class="m-0 mt-2 text-2xl font-extrabold text-slate-900">
              {{ filteredExchangeRate.length }}
            </p>
          </div>

          <div
            class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
          >
            <p class="m-0 text-sm text-slate-500">Status</p>
            <p class="m-0 mt-2 text-2xl font-extrabold text-slate-900">
              {{ loading ? 'Syncing' : 'Ready' }}
            </p>
          </div>
        </div>

        <!-- Table -->
        <div
          class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm"
        >
          <div
            class="flex flex-col gap-3 border-b border-slate-200 p-4 sm:flex-row sm:items-center sm:justify-between"
          >
            <h2 class="m-0 text-base font-extrabold text-slate-900">
              Rate Board
            </h2>

            <input
              v-model="search"
              class="min-h-11 w-full rounded-lg border border-slate-300 px-3 text-sm outline-none transition focus:border-cyan-600 focus:shadow-[0_0_0_4px_rgba(8,145,178,0.14)] sm:max-w-xs"
              type="search"
              placeholder="Search currencies or rate"
            />
          </div>

          <DataTable
            :value="filteredExchangeRate"
            :loading="loading"
            stripedRows
            responsiveLayout="scroll"
            tableStyle="min-width: 54rem"
          >
            <template #empty>
              <div
                class="py-8 text-center text-sm font-semibold text-slate-500"
              >
                No exchange rate found.
              </div>
            </template>

            <Column header="No" style="width: 80px">
              <template #body="slotProps">
                {{ slotProps.index + 1 }}
              </template>
            </Column>

            <Column
              field="from_currency_id"
              header="From Currency"
              sortable
            />

            <Column
              field="to_currency_id"
              header="To Currency"
              sortable
            />

            <Column field="rate" header="Rate" sortable>
              <template #body="slotProps">
                <span
                  class="rounded-lg bg-cyan-100 px-3 py-1 font-bold text-cyan-700"
                >
                  {{ slotProps.data.rate }}
                </span>
              </template>
            </Column>

            <Column header="Action" style="width: 190px">
              <template #body>
                <div class="flex gap-2">
                  <Button
                    label="Edit"
                    severity="info"
                    size="small"
                    outlined
                  />

                  <Button
                    label="Delete"
                    severity="danger"
                    size="small"
                    outlined
                  />
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
import { computed, onMounted, ref } from "vue";
import { IonContent } from "@ionic/vue";
import { useExchangeRate } from "@/composable/useExchangeRate.js";

const { exchangeRate, loading, getExchangeRateList } = useExchangeRate();

const search = ref("");

const filteredExchangeRate = computed(() => {
  const keyword = search.value.trim().toLowerCase();

  if (!keyword) {
    return exchangeRate.value;
  }

  return exchangeRate.value.filter((item) => {
    return [item.from_currency_id, item.to_currency_id, item.rate]
      .filter(Boolean)
      .some((value) =>
        String(value).toLowerCase().includes(keyword)
      );
  });
});

onMounted(() => {
  getExchangeRateList();
});
</script>