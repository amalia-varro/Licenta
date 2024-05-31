<script>
export default {
  name: "TeleworkingRequest",
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
        { title: 'Date', align: '', key: 'date' },
        { title: 'Address', align: '', key: 'address' },
        { title: 'Status', align: '', key: 'status' },
        { title: 'Approver', align: '', key: 'approver' },
        { title: 'Actions', align: '', key: 'actions' },
      ],
      desserts: [],  // Removed initial data with Amalia
      dialogOpen: false,
      teleworkingDate: null,
      teleworkingAddress: ""
    };
  },
  methods: {
    filterData() {
      // Implement filtering logic here
    },
    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      if (index !== -1) {
        this.desserts.splice(index, 1);
      }
    },
    openDialog() {
      this.dialogOpen = true;
    },
    closeDialog() {
      this.dialogOpen = false;
    },
    submitTeleworkingRequest() {
      if (!this.teleworkingDate || !this.teleworkingAddress) {
        alert("Please fill in all fields.");
        return;
      }

      const existingRequest = this.desserts.find(request => request.date === this.teleworkingDate);
      if (existingRequest) {
        alert("A request for this date already exists.");
        return;
      }

      this.desserts.push({
        name: "Requester Name",  // Add logic to get requester's name if needed
        date: this.teleworkingDate,
        address: this.teleworkingAddress,
        status: "Pending",
        approver: "Manager"  // Adjust as needed
      });

      this.teleworkingDate = null;
      this.teleworkingAddress = "";
      this.closeDialog(); // Close dialog after submitting
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
      <v-col cols="2" class="mt-1">
        <v-btn @click="filterData" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Filter</v-btn>
      </v-col>
      <v-col cols="6" class="mr-2">
        <v-btn @click="openDialog" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Create Teleworking Request</v-btn>
      </v-col>
    </v-row>

    <!-- Table -->
    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="desserts">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.date }}</td>
              <td>{{ item.address }}</td>
              <td>{{ item.status }}</td>
              <td>{{ item.approver }}</td>
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

    <!-- Dialog for creating teleworking request -->
    <v-dialog v-model="dialogOpen" max-width="600px">
      <v-card>
        <v-card-title>Create Teleworking Request</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-text-field v-model="teleworkingDate" label="Teleworking Date" type="date" color="purple-lighten-1"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="teleworkingAddress" label="Address" rows="3" multi-line color="purple-lighten-1"></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn color="purple-lighten-1" @click="submitTeleworkingRequest">Submit</v-btn>
          <v-btn color="purple-lighten-1" @click="closeDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<style scoped>
.top-section {
  margin-bottom: 20px;
}

.days-left-box {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Aligned to the right */
  margin-right: 10px; /* Adjusted as needed */
}

.days-left {
  font-size: 24px; /* Adjust font size as needed */
  font-weight: bold;
  color: rgb(171, 71, 188); /* Purple color */
}

.menu-wrapper {
  position: relative;
  display: inline-block;
  margin-right: 5px; /* Adjust margin as needed */
}

.menu-model {
  margin-top: 8vh;
  margin-left: 91vw;
}

.v-list-item--link {
  text-decoration: none;
  color: inherit;
}
</style>

