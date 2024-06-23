<template>
  <div class="manager-view">
    <h1 class="title">Vacation Requests</h1>
    <div class="search-container">
      <input type="text" v-model="searchQuery" placeholder="Search for employee name" class="search-input" />
      <button class="search-button" @click="searchEmployee">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="24px" height="24px">
          <path d="M0 0h24v24H0z" fill="none"/>
          <path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 0 0 1.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 0 0-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 0 0 5.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
        </svg>
      </button>
    </div>
    <div class="calendar-container">
      <input type="month" v-model="selectedMonth" @change="updateCalendar" />
    </div>
    <table>
      <thead>
      <tr>
        <th>Employee Name</th>
        <th>Start Date</th>
        <th>End Date</th>
        <th>Days</th>
        <th>Status</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="request in filteredRequests" :key="request.id">
        <td>{{ request.name }}</td>
        <td>{{ request.startDate }}</td>
        <td>{{ request.endDate }}</td>
        <td>{{ request.days + 1}}</td>
        <td :class="{'approved': request.status === 'Approved', 'declined': request.status === 'Declined', 'pending': request.status === 'Pending'}">{{ request.status }}</td>
        <td>
          <button @click="approveRequest(request.id)" :disabled="request.status === 'Approved'" class="approve-button">Approve</button>
          <button @click="declineRequest(request.id)" :disabled="request.status === 'Declined'" class="decline-button">Decline</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {useUserStore} from "@/stores/user";
import {useVacationStore} from "@/stores/vacation";
import _ from "lodash";
import moment from "moment/moment";


export default {
  data() {
    return {
      searchQuery: '',
      selectedMonth: "",
      requests: [],
    };
  },
  setup() {
    return {
      userStore: useUserStore(),
      vacationStore: useVacationStore()
    }
  },
  computed: {
    filteredRequests() {
      if (this.searchQuery === "") {
        return this.requests
      }
      return this.requests.filter(request =>
        request.name.toLowerCase().includes(this.searchQuery.toLowerCase()) &&
        request.startDate.startsWith(this.selectedMonth)
      );
    }
  },
  async mounted() {
    await this.userStore.getUsers()
    await this.updateList()

    let date = new Date()
    const addZero = (val) => (val < 10 ? "0" + val : val);
    let month = addZero(date.getMonth()+1)
    this.selectedMonth = `${date.getFullYear()}-${month}`
  },
  methods: {
    async updateList() {
      this.requests = []
      await this.vacationStore.getVacations()

      this.vacationStore.vacationRequests.forEach(i => {
        let user = _.find(this.userStore.users, p => p.id === i.user_id)
        console.log(this.userStore.users, i)
        this.requests.push({
          id: i.id,
          user_id: user.id,
          name: user.full_name,
          startDate: i.start_date,
          endDate: i.end_date,
          days: moment(i.end_date).diff(moment(i.start_date), "days"),
          status: i.status
        });
      })
    },
    searchEmployee() {
      console.log('Searching for:', this.searchQuery);
    },
    updateCalendar() {
      console.log('Selected month:', this.selectedMonth);
    },
    async approveRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) {
        request.status = 'approved';
      }
      await this.vacationStore.approveVacation(id)
    },
    async declineRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) {
        request.status = 'disapproved';
      }
      await this.vacationStore.disapproveVacation(id)
    }
  }
};
</script>

<style scoped>
.manager-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  border-radius: 20px;
  padding: 10px 20px;
  width: 300px;
}

.search-button {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ba68c8;
  border: none;
  border-radius: 50%;
  padding: 10px;
  cursor: pointer;
  margin-left: 10px;
}

.search-button svg {
  fill: white;
  width: 20px;
  height: 20px;
}

.calendar-container {
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}

th {
  background-color: #ba68c8;
  color: white;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #e1c8e4;
}

.approve-button,
.decline-button {
  background-color: #ba68c8;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  margin-right: 5px;
}

.approve-button:disabled,
.decline-button:disabled {
  background-color: grey;
  cursor: not-allowed;
}

.approved {
  color: green;
  font-weight: bold;
}

.declined {
  color: red;
  font-weight: bold;
}

.pending {
  color: #ef06de;
  font-weight: bold;
}

.title {
  font-size: 2em;
  font-weight: bold;
  color: #ba68c8;
  margin-bottom: 20px;
  text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.4);
  transition: text-shadow 0.3s;
  text-align: center;
}
</style>
