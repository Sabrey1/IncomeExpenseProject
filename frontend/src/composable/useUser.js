import { ref } from "vue"
import api from "@/services/api-service"

export function useUser() {
  
  const users = ref([])
  const loading = ref(false)
 
 async function getUserList(){
    const res = await api.get('/users').then(res => {
      users.value = res.data
    })
  }
  
  return {
    users,
    getUserList
  }
}