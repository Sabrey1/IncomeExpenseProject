import { ref } from "vue"
import api from "@/services/api-service"

export function usePaymentMethod() {
  
  const paymentMethod = ref([])
  const loading = ref(false)
 
 async function getPaymentMethodList(){
    const res = await api.get('/payment-methods')
    if(res.data){
        paymentMethod.value = res.data
    }
  }
  
  return {
    paymentMethod,
    getPaymentMethodList
  }
}