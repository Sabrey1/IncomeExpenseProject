<template>
  <div>
    <h2>User List</h2>

    <ul v-if="users.length">
      <li v-for="user in users" :key="user.id">
        {{ user.username }} - {{ user.email }}
      </li>
    </ul>

    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import { useUser } from "@/composable/useUser.js"
const { users, getUserList } = useUser()

onMounted(() => {
  getUserList()
})
</script>