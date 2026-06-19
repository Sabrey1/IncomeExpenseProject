import { ref } from "vue"
import api from "@/services/api-service"

export function useExpenseType() {
  
  const expenseType = ref([])
  const loading = ref(false)
 
 async function getExpenseList(){
    loading.value = true

    try {
      const res = await api.get('/expense-types')
      if(res.data){
          expenseType.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    expenseType,
    loading,
    getExpenseList
  }
}
