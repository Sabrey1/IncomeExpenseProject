import { ref } from "vue"
import api from "@/services/api-service"

export function useUser() {
  
  const users = ref([])
  const loading = ref(false)
 
 async function getUserList(){
    loading.value = true

    try {
      const res = await api.get('/users')
      users.value = res.data
    } finally {
      loading.value = false
    }
  }
  
  return {
    users,
    loading,
    getUserList
  }
}
