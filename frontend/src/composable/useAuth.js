import { ref, computed } from "vue"
import { useRoute } from "vue-router"
import api from "@/services/api-service"

export function getAuthUser() {
  const savedUser = localStorage.getItem("user")

  if (!savedUser) {
    return null
  }

  try {
    return JSON.parse(savedUser)
  } catch {
    localStorage.removeItem("user")
    return null
  }
}

export function isAuthenticated() {
  return !!getAuthUser() && !!localStorage.getItem("access_token")
}

export function useAuth() {
  const user = ref(getAuthUser())
  const loading = ref(false)
  const error = ref("")

  async function login(username, password) {
    loading.value = true
    error.value = ""

    try {
      const res = await api.post("/login/login", null, {
        params: {
          username,
          password,
        },
      })

      if (!res.data?.success) {
        error.value = res.data?.message || "Invalid username or password"
        user.value = null
        localStorage.removeItem("user")
        localStorage.removeItem("access_token")
        return res.data
      }

      const authData = res.data.data
      user.value = authData.user ?? authData
      localStorage.setItem("user", JSON.stringify(user.value))
      localStorage.setItem("access_token", authData.access_token)
      return res.data
    } catch (err) {
      error.value = err.response?.data?.detail || err.message || "Login failed"
      user.value = null
      localStorage.removeItem("user")
      localStorage.removeItem("access_token")
      return {
        success: false,
        message: error.value,
        data: null,
      }
    } finally {
      loading.value = false
    }
  }

  function logout() {
    user.value = null
    error.value = ""
    localStorage.removeItem("user")
    localStorage.removeItem("access_token")
  }

  const route = useRoute()
  const isAuth = computed(() => route.name === 'login')

  return {
    user,
    loading,
    error,
    login,
    logout,
    isAuth,
  }
}
