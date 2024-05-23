<script>
export default {
  name: "VacationRequest",
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
        { title: 'Requester', align: 'start', key: 'name' },
        { title: 'Start', align: '', key: 'date1' },
        { title: 'End', align: '', key: 'date2' },
        { title: 'Days', align: '', key: 'days' },
        { title: 'Status', align: '', key: 'status' },
        { title: 'Actions', align: '', key: 'actions' },
      ],
      desserts: [],
      dialogOpen: false,
      vacationStartDate: null,
      vacationEndDate: null,
      requesterName: "",
      availableVacationDays: 26,
    };
  },
  methods: {
    filterData() {
      // Implement filtering logic here
    },
    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      if (index !== -1) {
        this.availableVacationDays += parseInt(item.days);
        this.desserts.splice(index, 1);
      }
    },
    openDialog() {
      this.dialogOpen = true;
    },
    closeDialog() {
      this.dialogOpen = false;
    },
    calculateDaysDifference(startDate, endDate) {
      const start = new Date(startDate);
      const end = new Date(endDate);
      const timeDifference = end - start;
      const dayDifference = Math.floor(timeDifference / (1000 * 3600 * 24));
      return dayDifference + 1;
    },
    submitVacationRequest() {
      if (!this.vacationStartDate || !this.vacationEndDate || !this.requesterName) {
        alert("Please fill in all fields.");
        return;
      }

      const daysRequested = this.calculateDaysDifference(this.vacationStartDate, this.vacationEndDate);

      if (daysRequested > this.availableVacationDays) {
        alert("Not enough vacation days available.");
        return;
      }

      const startDate = new Date(this.vacationStartDate);
      const endDate = new Date(this.vacationEndDate);

      const overlap = this.desserts.some(request => {
        const requestStart = new Date(request.date1);
        const requestEnd = new Date(request.date2);
        return (startDate <= requestEnd && endDate >= requestStart);
      });

      if (overlap) {
        alert("There is already a vacation request in this date range.");
        return;
      }

      this.desserts.push({
        name: this.requesterName,
        date1: this.vacationStartDate,
        date2: this.vacationEndDate,
        days: daysRequested.toString(),
        status: "Pending"
      });

      this.availableVacationDays -= daysRequested;

      this.vacationStartDate = null;
      this.vacationEndDate = null;
      this.requesterName = "";

      this.closeDialog();
    }
  }
};
</script>

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
      <v-col cols="auto">
        <v-btn @click="filterData" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Filter</v-btn>
      </v-col>
      <!-- Days left box -->
      <v-col cols="6" class="mr-2">
        <v-btn @click="openDialog" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Create Vacation Request</v-btn>
      </v-col>
      <v-col cols="auto" class="days-left-box">
        <span class="days-left">{{ availableVacationDays }}</span> Days Left
      </v-col>
    </v-row>

    <!-- Table -->
    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="desserts">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.date1 }}</td>
              <td>{{ item.date2 }}</td>
              <td>{{ item.days }}</td>
              <td>{{ item.status }}</td>
              <td>
                <!-- Actions -->
                <v-btn icon @click="deleteItem(item)">
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

    <!-- Dialog for creating vacation request -->
    <v-dialog v-model="dialogOpen" max-width="600px">
      <v-card>
        <v-card-title>Create Vacation Request</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-text-field v-model="requesterName" label="Requester Name" color="purple-lighten-1"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="vacationStartDate" label="Start Date" type="date" color="purple-lighten-1"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="vacationEndDate" label="End Date" type="date" color="purple-lighten-1"></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn color="purple-lighten-1" @click="submitVacationRequest">Submit</v-btn>
          <v-btn color="purple-lighten-1" @click="closeDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<style scoped>
.top-section {
  margin-bottom: 20px;
  justify-content: space-between;
}

.days-left-box {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Schimbăm de la 'center' la 'flex-end' */
  margin-right: 450px; /* Ajustează marginile dacă este necesar */
}

.days-left {
  font-size: 24px; /* Adjust font size as needed */
  font-weight: bold;
  color: rgb(171, 71, 188); /* Purple color */
}
</style>
