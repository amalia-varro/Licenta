// Utilities
import { defineStore } from 'pinia'
import axios from "axios";

export const useUserStore = defineStore('store', {
  state: () => ({
    users: [],
    isLoggedIn: false,
    userId: 0,
    role: null,
    fullName: null,
    token: null
  }),
  actions: {
    checkLogin() {
      let result = localStorage.getItem("login")
      if (result != null) {
        result = JSON.parse(result)
        if (result == null) {
          return
        }
        console.log("local login", result)
        this.userId = result.userId
        this.role = result.role
        this.fullName = result.fullName
        this.token = result.token
        this.isLoggedIn = true
      }
    },
    async getUsers() {
      let response = await axios.get("http://localhost:8000/users/")
      this.users = response?.data ?? []
    },
    async login(username, password) {
      console.log("login", username, password)
      let response = await axios.post("http://localhost:8000/users/login", {
        username,
        password
      })
      console.log("login res", response)
      this.isLoggedIn = true
      this.userId = response.data.user_id
      this.role = response.data.role
      this.fullName = response.data.full_name
      this.token = response.data.token

      localStorage.setItem("login", JSON.stringify({
        "userId": this.userId,
        "role": this.role,
        "fullName": this.fullName,
        "token": this.token,
      }))
    },
    async logout() {
      localStorage.setItem("login", null)
      this.isLoggedIn = false
      this.fullName = null
    },
    async register(username, password, email, fullName, role) {
      let response = await axios.post("http://localhost:8000/users/register", {
        "full_name": fullName,
        "username": username,
        "email": email,
        "role": role,
        "phone_number": "string",
        "password": password
      })
      return response.status === 200;
    },
  },
})
