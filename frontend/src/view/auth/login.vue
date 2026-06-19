<template>
    <div
        class="grid min-h-screen place-items-center bg-[radial-gradient(circle_at_top_left,rgba(34,197,94,0.18),transparent_32%),radial-gradient(circle_at_bottom_right,rgba(59,130,246,0.16),transparent_30%),linear-gradient(135deg,#f8fafc_0%,#eef2f7_100%)] p-4 sm:p-6"
    >
        <section
            class="w-full max-w-[430px] rounded-lg border border-slate-300/30 bg-white/90 p-5 shadow-[0_24px_70px_rgba(15,23,42,0.13)] backdrop-blur-xl sm:p-9"
            aria-label="Login form"
        >
            <div
                class="mb-7 grid h-[52px] w-[52px] place-items-center rounded-lg bg-gradient-to-br from-teal-700 to-blue-600 text-lg font-extrabold text-white"
            >
                IE
            </div>

            <div class="mb-7">
                <p class="mb-2 text-[13px] font-extrabold uppercase text-teal-700">Welcome back</p>
                <h1 class="m-0 text-[26px] font-extrabold leading-tight text-gray-900 sm:text-[32px]">
                    Sign in to your account
                </h1>
                <p class="mt-3 text-[15px] leading-relaxed text-slate-500">
                    Manage your income, expenses, and exchange rates from one clean workspace.
                </p>
            </div>

            <form class="grid gap-[18px]" @submit.prevent="submitLogin">
                <label class="grid gap-2">
                    <span class="text-sm font-bold text-slate-700">Username</span>
                    <input
                        v-model="username"
                        class="min-h-[50px] w-full rounded-lg border border-slate-300 bg-white px-[15px] text-slate-950 outline-none transition placeholder:text-slate-400 focus:border-teal-700 focus:shadow-[0_0_0_4px_rgba(15,118,110,0.14)]"
                        type="text"
                        name="username"
                        autocomplete="username"
                        placeholder="Enter username"
                        required
                    />
                </label>

                <label class="grid gap-2">
                    <span class="text-sm font-bold text-slate-700">Password</span>
                    <input
                        v-model="password"
                        class="min-h-[50px] w-full rounded-lg border border-slate-300 bg-white px-[15px] text-slate-950 outline-none transition placeholder:text-slate-400 focus:border-teal-700 focus:shadow-[0_0_0_4px_rgba(15,118,110,0.14)]"
                        type="password"
                        name="password"
                        autocomplete="current-password"
                        placeholder="Enter password"
                        required
                    />
                </label>

                <p
                    v-if="error"
                    class="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm font-semibold text-red-700"
                >
                    {{ error }}
                </p>

                <button
                    type="submit"
                    :disabled="loading"
                    class="mt-1 min-h-[52px] cursor-pointer rounded-lg border-0 bg-gradient-to-br from-teal-700 to-blue-600 font-extrabold text-white shadow-[0_16px_30px_rgba(37,99,235,0.24)] transition hover:-translate-y-px hover:shadow-[0_20px_36px_rgba(37,99,235,0.28)] active:translate-y-0 disabled:cursor-not-allowed disabled:opacity-70 disabled:hover:translate-y-0"
                >
                    {{ loading ? "Logging in..." : "Login" }}
                </button>
            </form>
        </section>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composable/useAuth'

const username = ref('')
const password = ref('')
const router = useRouter()
const { loading, error, login } = useAuth()

const submitLogin = async () => {
    const result = await login(username.value, password.value)

    if (result.success) {
        router.push('/dashboard')
    }
}
</script>
