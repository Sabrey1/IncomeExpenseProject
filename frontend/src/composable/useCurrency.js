import { ref } from "vue"
import api from "@/services/api-service"

export function useCurrency() {
  
  const currency = ref([])
  const loading = ref(false)
 
 async function getCurrencyList(){
    const res = await api.get('/currencies')
    if(res.data){
        currency.value = res.data
    }
  }
  
  return {
    currency,
    getCurrencyList
  }
}