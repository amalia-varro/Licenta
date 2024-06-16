// Utilities
import {defineStore} from 'pinia'
import axios from "axios";

export const useTeleworkingStore = defineStore('teleworking', {
  state: () => ({
    teleworkingRequests: []
  }),
  actions: {
    async getTeleworking() {
      let response = await axios.get("http://localhost:8000/teleworking/")
      this.teleworkingRequests = response?.data ?? []
    },
    async makeRequest(data) {
      await axios.post("http://localhost:8000/teleworking/", data)
    },
    async deleteItem(id) {
      await axios.delete(`http://localhost:8000/teleworking/${id}`)
    },
    async approveTeleworking(id) {
      await axios.put(`http://localhost:8000/teleworking/${id}/approve`)

    },
    async disapproveTeleworking(id) {
      await axios.put(`http://localhost:8000/teleworking/${id}/disapprove`)
    }
  }
})
