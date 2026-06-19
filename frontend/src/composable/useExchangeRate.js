import { ref } from "vue"
import api from "@/services/api-service"

export function useExchangeRate() {
  
  const exchangeRate = ref([])
  const loading = ref(false)
 
 async function getExchangeRateList(){
    const res = await api.get('/exchange-rates')
    if(res.data){
        exchangeRate.value = res.data
    }
  }
  
  return {
    exchangeRate,
    getExchangeRateList
  }
}