import { ref } from "vue"
import api from "@/services/api-service"

export function useExchangeRate() {
  
  const exchangeRate = ref([])
  const loading = ref(false)
 
 async function getExchangeRateList(){
    loading.value = true

    try {
      const res = await api.get('/exchange-rates')
      if(res.data){
          exchangeRate.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    exchangeRate,
    loading,
    getExchangeRateList
  }
}
