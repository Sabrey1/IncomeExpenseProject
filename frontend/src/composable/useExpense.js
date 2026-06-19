import { ref } from "vue"
import api from "@/services/api-service"

export function useExpense() {
  
  const expense = ref([])
  const loading = ref(false)
 
 async function getExpenseList(){
    const res = await api.get('/expenses')
    if(res.data){
        expense.value = res.data
    }
  }
  
  return {
    expense,
    getExpenseList
  }
}