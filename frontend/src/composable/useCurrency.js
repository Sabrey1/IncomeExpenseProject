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

  async function addCurrency(data){
    try{
      loading.value = true

      const res = await api.post('/currencies', data)
      if(res.data){
        currency.value.push(res.data)
      }
    }catch(err){
      console.error('Error adding currency:', err)
    }finally{
      loading.value = false
    }
  }
  
  return {
    currency,
    loading,
    getCurrencyList,
    addCurrency
  }
}
