import Login from '@/view/auth/login.vue'
import Dashboard from '@/view/dashboard/dashboard.vue'
import NotFound from '@/view/NotFound.vue'
import MainLayout from '@/view/MainLayout.vue'
import CurrencyList from '@/view/currency/CurrencyList.vue'
import ExchangeRateList from '@/view/exchange_rate/ExchangeRateList.vue'
import ExpenseList from '@/view/expense/ExpenseList.vue'
import ExpenseType from '@/view/expense_type/ExpenseType.vue'
import Income from '@/view/income/Income.vue'
import IncomeType from '@/view/income_type/IncomeType.vue'
import PaymentMethod from '@/view/payment_method/PaymentMethod.vue'
import RoleList from '@/view/role/RoleList.vue'
import UserList from '@/view/user/UserList.vue'

export const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: 'login',
        name: 'login',
        component: Login
      },
      {
        path: '',
        redirect: '/dashboard'
      },
      {
        path: 'dashboard',
        name: 'dashboard',
        component: Dashboard
      },
      {
        path: 'currency',
        name: 'currency',
        component: CurrencyList
      },
      {
        path: 'exchange_rate',
        name: 'exchange_rate',
        component: ExchangeRateList
      },
      {
        path: 'expense',
        name: 'expense',
        component: ExpenseList
      },
      {
        path: 'expense-type',
        name: 'expense-type',
        component: ExpenseType
      },
      {
        path: 'income',
        name: 'income',
        component: Income
      },
      {
        path: 'income-type',
        name: 'income-type',
        component: IncomeType
      },
      {
        path: 'payment-method',
        name: 'payment-method',
        component: PaymentMethod
      },
      {
        path: 'role',
        name: 'role',
        component: RoleList
      },
      {
        path: 'user',
        name: 'user',
        component: UserList
      },
      
    ]
  },

  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  }
]