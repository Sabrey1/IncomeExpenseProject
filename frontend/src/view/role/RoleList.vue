<template>
  <ion-content>
    <main class="min-h-screen bg-slate-50 p-4 md:p-6">
      <!-- Header -->
      <div
        class="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
      >
        <div>
          <h1 class="text-3xl font-extrabold text-slate-900">
            Role Management
          </h1>

          <p class="mt-1 text-sm text-slate-500">
            Manage user roles and permissions within the system.
          </p>
        </div>

        <Button
          label="Add Role"
          icon="pi pi-plus"
          severity="info"
        />
      </div>

      <!-- Statistics -->
      <div class="mb-6 grid gap-4 md:grid-cols-3">
        <div
          class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
        >
          <p class="text-sm text-slate-500">Total Roles</p>
          <p class="mt-2 text-2xl font-bold text-slate-900">
            {{ role.length }}
          </p>
        </div>

        <div
          class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
        >
          <p class="text-sm text-slate-500">Visible</p>
          <p class="mt-2 text-2xl font-bold text-green-600">
            {{ filteredRole.length }}
          </p>
        </div>

        <div
          class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
        >
          <p class="text-sm text-slate-500">Status</p>
          <p class="mt-2 text-2xl font-bold text-cyan-600">
            Ready
          </p>
        </div>
      </div>

      <!-- Table -->
      <div
        class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm"
      >
        <!-- Toolbar -->
        <div
          class="flex flex-col gap-3 border-b border-slate-200 p-4 md:flex-row md:items-center md:justify-between"
        >
          <h2 class="text-lg font-bold text-slate-900">
            Role List
          </h2>

          <IconField>
            <InputIcon class="pi pi-search" />

            <InputText
              v-model="search"
              placeholder="Search role..."
              class="w-full md:w-72"
            />
          </IconField>
        </div>

        <!-- DataTable -->
        <DataTable
          :value="filteredRole"
          stripedRows
          showGridlines
          scrollable
          scrollHeight="600px"
          tableStyle="min-width: 60rem"
        >
          <template #empty>
            <div class="py-8 text-center text-slate-500">
              No roles found.
            </div>
          </template>

          <Column header="No" style="width: 80px">
            <template #body="slotProps">
              {{ slotProps.index + 1 }}
            </template>
          </Column>

          <Column field="name" header="Role Name" sortable>
            <template #body="slotProps">
              <Tag
                :value="slotProps.data.name"
                severity="info"
              />
            </template>
          </Column>

          <Column field="description" header="Description">
            <template #body="slotProps">
              <span class="text-slate-600">
                {{ slotProps.data.description }}
              </span>
            </template>
          </Column>
            <Column header="Action" style="width: 220px">
            <template #body="slotProps">
                <div class="flex items-center justify-center gap-2">
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

import { useRole } from "@/composable/useRole.js";

const search = ref("");

const {
  role,
  getRoleList
} = useRole();

const filteredRole = computed(() => {
  const keyword = search.value.toLowerCase().trim();

  if (!keyword) {
    return role.value;
  }

  return role.value.filter((item) =>
    [item.name, item.description]
      .filter(Boolean)
      .some((value) =>
        String(value)
          .toLowerCase()
          .includes(keyword)
      )
  );
});

onMounted(() => {
  getRoleList();
});
</script>