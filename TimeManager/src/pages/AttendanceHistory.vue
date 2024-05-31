<template>
  <v-container class="attendance-history">
    <!-- Top section -->
    <v-row class="top-section">
      <v-col cols="5">
        <v-select v-model="selectedMonth" placeholder="Month" :items="months"></v-select>
      </v-col>
      <v-col cols="5">
        <v-select v-model="selectedYear" placeholder="Year" :items="years"></v-select>
      </v-col>
      <!-- Filter button -->
      <v-col cols="2" class="mt-2">
        <v-btn @click="filterData" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Filter</v-btn>
      </v-col>
    </v-row>

    <!-- Table -->
    <v-row>
      <v-col cols="12">
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
      </v-col>
    </v-row>

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
        { Day: 1, Type: "Teleworking Day", ArrivalTime: "9:00 AM", LeaveTime: "5:00 PM", Break: "1 hour", WorkedHours: "7 hours" },
        { Day: 2, Type: "Normal Day", ArrivalTime: "10:00 AM", LeaveTime: "2:00 PM", Break: "30 minutes", WorkedHours: "3.5 hours" },
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