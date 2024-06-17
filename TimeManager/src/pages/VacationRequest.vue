<template>
  <v-container class="attendance-history">
    <!-- Top section -->
    <v-row class="top-section py-5">
      <!--      <v-col cols="5">-->
      <!--        <v-select v-model="selectedMonth" placeholder="Month" :items="months"></v-select>-->
      <!--      </v-col>-->
      <!--      <v-col cols="5">-->
      <!--        <v-select v-model="selectedYear" placeholder="Year" :items="years"></v-select>-->
      <!--      </v-col>-->
      <!--      &lt;!&ndash; Filter button &ndash;&gt;-->
      <!--      <v-col cols="auto">-->
      <!--        <v-btn @click="filterData" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">Filter</v-btn>-->
      <!--      </v-col>-->
      <!-- Days left box -->
      <v-col cols="6" class="mr-2">
        <v-btn @click="openDialog" rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2">
          Create Vacation Request
        </v-btn>
      </v-col>
      <v-col>
        <h2>Available days: {{userStore.daysAvailable}}</h2>
      </v-col>
      <!--      <v-col cols="auto" class="days-left-box">-->
      <!--        <span class="days-left">{{ availableVacationDays }}</span> Days Left-->
      <!--      </v-col>-->
    </v-row>

    <!-- Table -->
    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="vacationRequestsForUser">
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.date1 }}</td>
              <td>{{ item.date2 }}</td>
              <td>{{ item.days }}</td>
              <td :class="{
                'font-weight-bold': item.status !== 'pending',
                'approved': item.status === 'approved',
                'disapproved': item.status === 'disapproved',
              }">{{ item.status }}</td>
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

    <!-- Dialog for creating vacation request -->
    <v-dialog v-model="dialogOpen" max-width="600px">
      <v-card>
        <v-card-title>Create Vacation Request</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-text-field disabled="disabled" color="purple-lighten-1">{{ userStore.fullName }}</v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="vacationStartDate" label="Start Date" type="date"
                            color="purple-lighten-1"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="vacationEndDate" label="End Date" type="date"
                            color="purple-lighten-1"></v-text-field>
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

<script>
import {useUserStore} from "@/stores/user";
import {useVacationStore} from "@/stores/vacation";
import _ from "lodash";
import moment from "moment";

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
        {title: 'Requester', align: 'start', key: 'name'},
        {title: 'Start', align: '', key: 'date1'},
        {title: 'End', align: '', key: 'date2'},
        {title: 'Days', align: '', key: 'days'},
        {title: 'Status', align: '', key: 'status'},
        {title: 'Actions', align: '', key: 'actions'},
      ],
      desserts: [],
      dialogOpen: false,
      vacationStartDate: null,
      vacationEndDate: null,
      availableVacationDays: +Infinity,
    };
  },
  setup() {
    return {
      userStore: useUserStore(),
      vacationStore: useVacationStore()
    }
  },
  async mounted() {
    await this.userStore.getUsers()
    await this.updateList()
  },
  computed: {
    vacationRequestsForUser() {
      return _.filter(this.desserts, i => i.user_id === this.userStore.userId)
    }
  },
  methods: {
    async updateList() {
      this.desserts = []
      await this.vacationStore.getVacations()

      this.vacationStore.vacationRequests.forEach(i => {
        let user = _.find(this.userStore.users, p => p.id === i.user_id)
        this.desserts.push({
          id: i.id,
          user_id: user.id,
          name: user.full_name,
          date1: i.start_date,
          date2: i.end_date,
          days: moment(i.end_date).diff(moment(i.start_date), "days"),
          status: i.status
        });
      })
    },
    deleteItem(item) {
      if (item.user_id === this.userStore.userId) {
        const index = this.desserts.indexOf(item);
        if (index !== -1) {
          this.availableVacationDays += parseInt(item.days);
          this.desserts.splice(index, 1);
          let daysRequested = moment(item.date2).diff(moment(item.date1), "days")
          this.userStore.updateDaysAvailable(parseInt(`${daysRequested}`, 10))

        }
        this.vacationStore.deleteItem(item.id)
      }
    },
    async approveItem(item) {
      await this.vacationStore.approveVacation(item.id)
      let el = _.find(this.desserts, i => i.id === item.id)
      el.status = "approved"
    },
    async disapproveItem(item) {
      await this.vacationStore.disapproveVacation(item.id)
      let el = _.find(this.desserts, i => i.id === item.id)
      el.status = "disapproved"
    },
    openDialog() {
      this.dialogOpen = true;
    },
    closeDialog() {
      this.dialogOpen = false;
    },
    async submitVacationRequest() {
      if (!this.vacationStartDate || !this.vacationEndDate) {
        alert("Please fill in all fields.");
        return;
      }

      let result = _.find(this.vacationStore.vacationRequests, i => {
        return i.user_id === this.userStore.userId && i.start_date === this.vacationStartDate && i.end_date === this.vacationEndDate
      })
      if (result) {
        this.$swal.fire({
          title: 'Error!',
          text: 'Failed create vacation request for given date. Already exists!',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
        this.closeDialog()
        return
      }

      let daysRequested = moment(this.vacationEndDate).diff(moment(this.vacationStartDate), "days")
      if (this.userStore.daysAvailable - daysRequested <= 0) {
        this.closeDialog()
        this.$swal.fire({
          title: 'Error!',
          text: 'Failed create vacation request for given date. Not enough days!',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
        return
      }
      this.userStore.updateDaysAvailable(parseInt(`-${daysRequested}`, 10))
      await this.vacationStore.makeRequest(
        {
          user_id: this.userStore.userId,
          start_date: this.vacationStartDate,
          end_date: this.vacationEndDate,
        }
      )
      await this.updateList()

      this.vacationStartDate = null;
      this.vacationEndDate = null;

      this.closeDialog();
    }
  }
};
</script>


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
.approved { color: green}
.disapproved { color: red}
</style>
