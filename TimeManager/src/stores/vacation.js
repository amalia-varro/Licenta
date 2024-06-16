// Utilities
import {defineStore} from 'pinia'
import axios from "axios";

export const useVacationStore = defineStore('vacation', {
  state: () => ({
    vacationRequests: []
  }),
  actions: {
    async getVacations() {
      let response = await axios.get("http://localhost:8000/timeoff/")
      this.vacationRequests = response?.data ?? []
    },
    async makeRequest(data) {
      await axios.post("http://localhost:8000/timeoff/", data)
    },
    async deleteItem(id) {
      await axios.delete(`http://localhost:8000/timeoff/${id}`)
    },
    async approveVacation(id) {
      await axios.put(`http://localhost:8000/timeoff/${id}/approve`)

    },
    async disapproveVacation(id) {
      await axios.put(`http://localhost:8000/timeoff/${id}/disapprove`)

    }
  }
})
