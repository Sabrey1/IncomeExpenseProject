import { ref } from "vue"
import api from "@/services/api-service"

export function useIncomeType() {
  
  const incomeType = ref([])
  const loading = ref(false)
 
 async function getIncomeTypeList(){
    const res = await api.get('/income-types')
    if(res.data){
        incomeType.value = res.data
    }
  }
  
  return {
    incomeType,
    getIncomeTypeList
  }
}