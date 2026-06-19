import { ref } from "vue"
import api from "@/services/api-service"

export function useExpenseType() {
  
  const expenseType = ref([])
  const loading = ref(false)
 
 async function getExpenseList(){
    const res = await api.get('/expense-types')
    if(res.data){
        expenseType.value = res.data
    }
  }
  
  return {
    expenseType,
    getExpenseList
  }
}