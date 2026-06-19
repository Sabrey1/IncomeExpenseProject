import { ref } from "vue"
import api from "@/services/api-service"

export function useCurrency() {
  
  const currency = ref([])
  const loading = ref(false)
 
 async function getCurrencyList(){
    loading.value = true

    try {
      const res = await api.get('/currencies')
      if(res.data){
          currency.value = res.data
      }
    } finally {
      loading.value = false
    }
  }
  
  return {
    currency,
    loading,
    getCurrencyList
  }
}
