<template>
  <ion-content>
    <main class="min-h-screen bg-slate-50 p-4 md:p-6">
      <!-- Header -->
      <div
        class="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
      >
        <div>
           
          <h1 class="text-3xl font-extrabold text-slate-900">
            Payment Methods
          </h1>

          <p class="mt-1 text-sm text-slate-500">
            Manage available payment methods for sales and purchases.
          </p>
        </div>

        <Button
          label="Add Payment Method"
          icon="pi pi-plus"
          severity="info"
        />
      </div>

      <!-- Stats -->
      <div class="mb-6 grid gap-4 md:grid-cols-3">
        <div class="rounded-xl bg-white p-4 shadow-sm border border-slate-200">
          <p class="text-sm text-slate-500">Total Methods</p>
          <p class="mt-2 text-2xl font-bold text-slate-900">
            {{ paymentMethod.length }}
          </p>
        </div>

        <div class="rounded-xl bg-white p-4 shadow-sm border border-slate-200">
          <p class="text-sm text-slate-500">Active</p>
          <p class="mt-2 text-2xl font-bold text-green-600">
            {{ paymentMethod.length }}
          </p>
        </div>

        <div class="rounded-xl bg-white p-4 shadow-sm border border-slate-200">
          <p class="text-sm text-slate-500">Status</p>
          <p class="mt-2 text-2xl font-bold text-cyan-600">
            Ready
          </p>
        </div>
      </div>

      <!-- Table Card -->
      <div
        class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm"
      >
        <!-- Toolbar -->
        <div
          class="flex flex-col gap-3 border-b border-slate-200 p-4 md:flex-row md:items-center md:justify-between"
        >
          <h2 class="font-bold text-slate-900">
            Payment Method List
          </h2>

          <IconField>
            <InputIcon class="pi pi-search" />

            <InputText
              v-model="search"
              placeholder="Search payment method..."
              class="w-full md:w-72"
            />
          </IconField>
        </div>
        

        <!-- Table -->
        <DataTable
          :value="filteredPaymentMethod"
          stripedRows
          
          responsiveLayout="scroll"
          tableStyle="min-width: 50rem"
        >
          <template #empty>
            <div class="py-6 text-center text-slate-500">
              No payment methods found.
            </div>
          </template>

          <Column header="No" style="width: 80px">
            <template #body="slotProps">
              {{ slotProps.index + 1 }}
            </template>
          </Column>

          <Column field="name" header="Name" sortable>
            <template #body="slotProps">
              <span class="font-medium text-slate-800">
                {{ slotProps.data.name }}
              </span>
            </template>
          </Column>
 

          <Column header="Action" style="width: 220px">
            <template #body>
              <div class="flex gap-2">
                <Button
                  icon="pi pi-pencil"
                  label="Edit"
                  severity="info"
                  outlined
                  size="small"
                />

                <Button
                  icon="pi pi-trash"
                  label="Delete"
                  severity="danger"
                  outlined
                  size="small"
                />
              </div>
            </template>
          </Column>
        </DataTable>
      </div>
    </main>
  </ion-content>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { IonContent } from "@ionic/vue";

import { usePaymentMethod } from "@/composable/usePaymentMethod.js";

const search = ref("");

const {
  paymentMethod,
  getPaymentMethodList
} = usePaymentMethod();

const filteredPaymentMethod = computed(() => {
  const keyword = search.value.toLowerCase().trim();

  if (!keyword) {
    return paymentMethod.value;
  }

  return paymentMethod.value.filter((item) =>
    [item.name, item.symbol]
      .filter(Boolean)
      .some((value) =>
        String(value)
          .toLowerCase()
          .includes(keyword)
      )
  );
});

onMounted(() => {
  getPaymentMethodList();
});
</script>