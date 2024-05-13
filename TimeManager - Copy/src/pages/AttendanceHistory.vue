<template>
  <v-container class="attendance-history">
    <!-- Top section -->
    <v-row class="top-section">
      <v-col>
        <v-select v-model="selectedMonth" :items="months"></v-select>
      </v-col>
      <v-col>
        <v-select v-model="selectedYear" :items="years"></v-select>
      </v-col>
      <!-- Filter button -->
      <v-col>
        <v-btn @click="filterData" color="primary">Filter</v-btn>
      </v-col>
    </v-row>

    <!-- Table -->
    <v-data-table :headers="headers" :items="desserts">
      <template v-slot:item="{ item }">
        <tr>
          <td>{{ item.Day }}</td>
          <td>{{ item.Type }}</td>
          <td>{{ item.ArrivalTime }}</td>
          <td>{{ item.LeaveTime }}</td>
          <td>{{ item.Break }}</td>
          <td>{{ item.WorkedHours }}</td>
          <td>
            <v-btn icon @click="editItem(item)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon @click="deleteItem(item)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  name: "AttendanceHistory",
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
        { title: 'Day', align: 'start', key: 'day' },
        { title: 'Type', align: '', key: 'type' },
        { title: 'Arrival Time', align: '', key: 'arrivalTime' },
        { title: 'Leave Time', align: '', key: 'leaveTime' },
        { title: 'Break', align: '', key: 'break' },
        { title: 'Worked Hours', align: '', key: 'workedHours' },
        { title: 'Actions', align: '', key: 'actions' },
      ],
      desserts: [
        { Day: 1, Type: "Full-time", ArrivalTime: "9:00 AM", LeaveTime: "5:00 PM", Break: "1 hour", WorkedHours: "7 hours" },
        { Day: 2, Type: "Part-time", ArrivalTime: "10:00 AM", LeaveTime: "2:00 PM", Break: "30 minutes", WorkedHours: "3.5 hours" },
        // Add more data objects as needed
      ]
    };
  },
  methods: {
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

</style>
