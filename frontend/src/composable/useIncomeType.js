import { ref } from "vue"
import api from "@/services/api-service"

export function useIncomeType() {
  
  const incomeType = ref([])
  const loading = ref(false)
 
 async function getIncomeTypeList(){
    loading.value = true

    try {
      const res = await api.get('/income-types')
      if(res.data){
          incomeType.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    incomeType,
    loading,
    getIncomeTypeList
  }
}
