<template>
  <ion-content>
    <main class="min-h-screen bg-slate-50 p-4 md:p-6">
      <!-- Header -->
      <div
        class="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
      >
        <div>
          <h1 class="text-3xl font-extrabold text-slate-900">
            User Management
          </h1>

          <p class="mt-1 text-sm text-slate-500">
            Manage system users and their accounts.
          </p>
        </div>

        <Button
          label="Add User"
          icon="pi pi-plus"
          severity="info"
        />
      </div>

      <!-- Statistics -->
      <div class="mb-6 grid gap-4 md:grid-cols-3">
        <div
          class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
        >
          <p class="text-sm text-slate-500">Total Users</p>
          <p class="mt-2 text-2xl font-bold text-slate-900">
            {{ users.length }}
          </p>
        </div>

        <div
          class="rounded-xl border border-slate-200 bg-white p-4 shadow-sm"
        >
          <p class="text-sm text-slate-500">Visible</p>
          <p class="mt-2 text-2xl font-bold text-green-600">
            {{ filteredUsers.length }}
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
            User List
          </h2>

          <IconField>
            <InputIcon class="pi pi-search" />

            <InputText
              v-model="search"
              placeholder="Search user..."
              class="w-full md:w-72"
            />
          </IconField>
        </div>

        <!-- DataTable -->
        <DataTable
          :value="filteredUsers"
          stripedRows
          showGridlines
          scrollable
          scrollHeight="600px"
          tableStyle="min-width: 70rem"
        >
          <template #empty>
            <div class="py-8 text-center text-slate-500">
              No users found.
            </div>
          </template>

          <Column header="No" style="width:80px">
            <template #body="slotProps">
              {{ slotProps.index + 1 }}
            </template>
          </Column>

          <Column field="username" header="Username" sortable>
            <template #body="slotProps">
              <span class="font-medium text-slate-800">
                {{ slotProps.data.username }}
              </span>
            </template>
          </Column>

          <Column field="email" header="Email" sortable>
            <template #body="slotProps">
              {{ slotProps.data.email }}
            </template>
          </Column>

          <Column field="phone" header="Phone">
            <template #body="slotProps">
              {{ slotProps.data.phone || '-' }}
            </template>
          </Column>

          <Column header="Action" style="width:140px">
            <template #body="slotProps">
              <div class="flex justify-center gap-2">
                <Button
                 label="Edit"
                  severity="info"
                  rounded
                  outlined
                />

                <Button
                  label="Delete"
                  severity="danger"
                  rounded
                  outlined
                />
              </div>
            </template>
          </Column>
        </DataTable>
      </div>
    </main>
  </ion-content>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { IonContent } from '@ionic/vue'

import { useUser } from '@/composable/useUser.js'

const search = ref('')

const { users, getUserList } = useUser()

const filteredUsers = computed(() => {
  const keyword = search.value.toLowerCase().trim()

  if (!keyword) return users.value

  return users.value.filter(user =>
    [
      user.username,
      user.email,
      user.phone
    ]
      .filter(Boolean)
      .some(value =>
        String(value)
          .toLowerCase()
          .includes(keyword)
      )
  )
})

onMounted(() => {
  getUserList()
})
</script>
