<template>
  <v-container class="attendance-history">
    <!-- Top section -->
    <v-row class="top-section">
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
              <td :class="{
                'font-weight-bold': item.status !== 'pending',
                'approved': item.status === 'approved',
                'disapproved': item.status === 'disapproved',
              }">{{ item.status }}</td>
              <td> Manager </td>
              <td>
                <!-- Actions -->
                <v-btn v-show="userStore.role === 'manager'" color="green" icon @click="approveItem(item)">
                  <v-icon>mdi-check-bold</v-icon>
                </v-btn>
                <v-btn  v-show="userStore.role === 'manager'" color="red" icon @click="disapproveItem(item)">
                  <v-icon>mdi-close-thick</v-icon>
                </v-btn>
                <v-btn v-show="item.user_id === userStore.userId && item.status.toLowerCase() === 'pending'" icon @click="deleteItem(item)">
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

<script>
import {useUserStore} from "@/stores/user";
import {useTeleworkingStore} from "@/stores/teleworking";
import _ from "lodash";

export default {
  name: "TeleworkingRequest",
  setup() {
    return {
      userStore: useUserStore(),
      teleworkingStore: useTeleworkingStore()
    }
  },
  data() {
    return {
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
        { title: 'Status', align: '', key: 'status' },
        { title: 'Approver', align: '', key: 'approver' },
        { title: 'Actions', align: '', key: 'actions' },
      ],
      desserts: [],  // Removed initial data with Amalia
      dialogOpen: false,
      teleworkingDate: null,
    };
  },
  async mounted() {
    await this.userStore.getUsers()
    await this.updateList()
  },
  methods: {
    async updateList() {
      this.desserts = []
      await this.teleworkingStore.getTeleworking()

      this.teleworkingStore.teleworkingRequests.forEach(i => {
        let user = _.find(this.userStore.users, p => p.id === i.user_id)
        this.desserts.push({
          id: i.id,
          user_id: user.id,
          name: user.full_name,
          date: i.date,
          status: i.status
        });
      })
    },
    async approveItem(item) {
      await this.teleworkingStore.approveTeleworking(item.id)
      let el = _.find(this.desserts, i => i.id === item.id)
      el.status = "approved"
    },
    async disapproveItem(item) {
      await this.teleworkingStore.disapproveTeleworking(item.id)
      let el = _.find(this.desserts, i => i.id === item.id)
      el.status = "disapproved"
    },
    async deleteItem(item) {
      const index = this.desserts.indexOf(item);
      if (index !== -1) {
        this.desserts.splice(index, 1);
        await this.teleworkingStore.deleteItem(item.id)
      }
    },
    openDialog() {
      this.dialogOpen = true;
    },
    closeDialog() {
      this.dialogOpen = false;
    },
    async submitTeleworkingRequest() {
      if (!this.teleworkingDate) {
        alert("Please fill in all fields.");
        return;
      }

      await this.teleworkingStore.makeRequest({
        user_id: this.userStore.userId,
        date: this.teleworkingDate
      })
      await this.updateList()

      this.teleworkingDate = null;
      this.closeDialog(); // Close dialog after submitting
    }
  }
};
</script>

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
.approved { color: green}
.disapproved { color: red}
</style>

