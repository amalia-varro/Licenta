// Utilities
import { defineStore } from 'pinia'
import axios from "axios";

export const useWorklogStore = defineStore('worklog', {
  state: () => ({
    workLogData: []
  }),
  actions: {
    async submitWorklog(data) {
      await axios.post("http://localhost:8000/worklog/", data)
    },
    async getAllWorklog() {
      let response = await axios.get("http://localhost:8000/worklog/")
      this.workLogData = response.data ?? []
    }
  }
})
