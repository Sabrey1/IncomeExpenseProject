import { ref } from "vue"
import api from "@/services/api-service"

export function useRole() {
  
  const role = ref([])
  const loading = ref(false)
 
 async function getRoleList(){
    loading.value = true

    try {
      const res = await api.get('/roles')
      if(res.data){
          role.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    role,
    loading,
    getRoleList
  }
}
