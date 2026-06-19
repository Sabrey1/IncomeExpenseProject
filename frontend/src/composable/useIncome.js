import { ref } from "vue"
import api from "@/services/api-service"

export function useIncome() {
  
  const income = ref([])
  const loading = ref(false)
 
 async function getIncomeList(){
    const res = await api.get('/incomes')
    if(res.data){
        income.value = res.data
    }
  }
  
  return {
    income,
    getIncomeList
  }
}