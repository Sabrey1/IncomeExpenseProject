import { ref } from "vue"
import api from "@/services/api-service"

export function getAuthUser() {
  const savedUser = localStorage.getItem("user")

  if (!savedUser) {
    return null
  }

  try {
    return JSON.parse(savedUser)
  } catch {
    localStorage.setItem("user", "")
    return null
  }
}

export function isAuthenticated() {
  return !!getAuthUser()
}

export function useAuth() {
  const user = ref(getAuthUser())
  const loading = ref(false)
  const error = ref("")

  async function login(username, password) {
    loading.value = true
    error.value = ""

    try {
      const res = await api.post("/users/login", null, {
        params: {
          username,
          password,
        },
      })

      if (!res.data?.success) {
        error.value = res.data?.message || "Invalid username or password"
        user.value = null
        localStorage.setItem("user", "")
        return res.data
      }

      user.value = res.data.data
      localStorage.setItem("user", JSON.stringify(res.data.data))
      return res.data
    } catch (err) {
      error.value = err.response?.data?.detail || err.message || "Login failed"
      user.value = null
      localStorage.setItem("user", "")
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
  }

  return {
    user,
    loading,
    error,
    login,
    logout,
  }
}
