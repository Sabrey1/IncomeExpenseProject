import { ref } from "vue"
import api from "@/services/api-service"

export function useIncome() {
  
  const income = ref([])
  const loading = ref(false)
 
 async function getIncomeList(){
    loading.value = true

    try {
      const res = await api.get('/incomes')
      if(res.data){
          income.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    income,
    loading,
    getIncomeList
  }
}
