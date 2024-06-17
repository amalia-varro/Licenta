<template>
  <v-container class="attendance-history">
    <!-- Top section -->
    <v-row class="top-section">
      <v-col class="text-center">
        <h1 class="title">Attendance History</h1>
      </v-col>
    </v-row>

    <!-- Table -->
    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="desserts">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.ArrivalTime }}</td>
              <td>{{ item.LeaveTime }}</td>
              <td>{{ item.Break }}</td>
              <td>{{ item.WorkedHours }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import {useUserStore} from "@/stores/user";
import {useWorklogStore} from "@/stores/worklog";
import moment from "moment";
import _ from "lodash";

export default {
  name: "AttendanceHistory",
  setup() {
    return {
      userStore: useUserStore(),
      worklogStore: useWorklogStore()
    }
  },
  async mounted() {
    await this.userStore.getUsers()
    await this.worklogStore.getAllWorklog()

    this.worklogStore.workLogData.forEach(i => {
      let user = _.find(this.userStore.users, p => p.id === i.user_id)

      let breakTime = i.break_start_hour.split(":")[1]
      if (breakTime === "00") {
        breakTime = "1 hour"
      } else {
        breakTime = `${breakTime} minutes`
      }
      this.desserts.push({
        name: user.full_name,
        ArrivalTime: i.start_hour,
        LeaveTime: i.end_hour,
        WorkedHours: `${this.differenceInHours(i.start_hour, i.end_hour)} hours`,
        Break: breakTime
      })
    })
  },
  data() {
    return {
      selectedMonth: null,
      selectedYear: null,
      months: [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ],
      years: [
        2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030
      ],
      headers: [
        { title: 'Name', align: '', key: 'name' },
        { title: 'Arrival Time', align: '', key: 'ArrivalTime' },
        { title: 'Leave Time', align: '', key: 'leaveTime' },
        { title: 'Break', align: '', key: 'break' },
        { title: 'Worked Hours', align: '', key: 'workedHours' },
      ],
      desserts: [
        { name: "pulea", ArrivalTime: "9:00 AM", LeaveTime: "5:00 PM", Break: "1 hour", WorkedHours: "7 hours" },
        { name: "pulea", ArrivalTime: "10:00 AM", LeaveTime: "2:00 PM", Break: "30 minutes", WorkedHours: "3.5 hours" },
        // Add more data objects as needed
      ]
    };
  },
  methods: {
    differenceInHours(startTime, endTime) {
      const startParts = startTime.split(":");
      const endParts = endTime.split(":");

      const startHours = parseInt(startParts[0], 10);
      const startMinutes = parseInt(startParts[1], 10);
      const startSeconds = parseInt(startParts[2], 10);
      const endHours = parseInt(endParts[0], 10);
      const endMinutes = parseInt(endParts[1], 10);
      const endSeconds = parseInt(endParts[2], 10);

      // ... rest of the logic with adjustments for seconds
      const totalSeconds = (endHours - startHours) * 3600 +
        (endMinutes - startMinutes) * 60 +
        (endSeconds - startSeconds);
      const totalHours = totalSeconds / 3600;
      return Math.abs(Math.round(totalHours));
    },
    filterData() {
      // Implement filtering logic here
    },
    editItem(item) {
      // Handle edit action
    },
    deleteItem(item) {
      // Handle delete action
    }
  }
};
</script>

<style scoped>
.attendance-history {
  /* Add styling for the main container */
}

.top-section {
  margin-bottom: 20px;
}
.title {
  font-size: 2em;
  font-weight: bold;
  color: #ba68c8;
  margin-bottom: 20px;
  text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.4); /* Adaugă umbre */
  transition: text-shadow 0.3s; /* Adaugă o tranziție pentru umbra textului */
  text-align: center;
}
</style>
