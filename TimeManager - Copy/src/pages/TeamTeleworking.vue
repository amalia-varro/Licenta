<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedMonth: '2024-05',
      requests: [
        { id: 1, name: 'John Doe', date: '2024-05-01', address: '123 Main St', status: 'Pending' },
        { id: 2, name: 'Jane Smith', date: '2024-05-02', address: '456 Oak St', status: 'Pending' },
        // More requests
      ],
    };
  },
  computed: {
    filteredRequests() {
      return this.requests.filter(request =>
        request.name.toLowerCase().includes(this.searchQuery.toLowerCase()) &&
        request.date.startsWith(this.selectedMonth)
      );
    }
  },
  methods: {
    searchEmployee() {
      console.log('Searching for:', this.searchQuery);
    },
    updateCalendar() {
      console.log('Selected month:', this.selectedMonth);
    },
    approveRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) {
        request.status = 'Approved';
      }
    },
    declineRequest(id) {
      const request = this.requests.find(req => req.id === id);
      if (request) {
        request.status = 'Declined';
      }
    }
  }
};
</script>

<template>
  <div class="manager-view">
    <h1 class="title">Teleworking Requests</h1>
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
        <th>Date</th>
        <th>Address</th>
        <th>Status</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="request in filteredRequests" :key="request.id">
        <td>{{ request.name }}</td>
        <td>{{ request.date }}</td>
        <td>{{ request.address }}</td>
        <td :class="{'approved': request.status === 'Approved', 'pending': request.status === 'Pending', 'declined': request.status === 'Declined'}">{{ request.status }}</td>
        <td>
          <button @click="approveRequest(request.id)" :disabled="request.status === 'Approved'" class="approve-button">
            Approve
          </button>
          <button @click="declineRequest(request.id)" :disabled="request.status === 'Declined'" class="decline-button">
            Decline
          </button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.manager-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

/* Stilizare pentru câmpul de căutare */
.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  border-radius: 20px; /* Transformare în casetă ovală */
  padding: 10px 20px; /* Spatiere internă */
  width: 300px; /* Lățimea dorită a câmpului de căutare */
}

.search-button {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ba68c8;
  border: none;
  border-radius: 50%; /* Buton rotund */
  padding: 10px;
  cursor: pointer;
  margin-left: 10px; /* Spațiere între câmpul de căutare și buton */
}

.search-button svg {
  fill: white;
  width: 20px;
  height: 20px;
}

.calendar-container {
  margin-bottom: 20px;
}

input[type="month"] {
  -webkit-appearance: none;
}

input[type="month"]::-webkit-calendar-picker-indicator {
  color: white;
  padding: 0.5em;
  border: none;
}

input[type="month"]:focus::-webkit-calendar-picker-indicator {
  background-color: #ba68c8;
  color: white;
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

.approve-button, .decline-button {
  background-color: #ba68c8;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  margin-right: 5px;
}

.approve-button:disabled, .decline-button:disabled {
  background-color: grey;
  cursor: not-allowed;
}

.approved {
  color: green;
  font-weight: bold;
}

.pending {
  color: #ef06de;
  font-weight: bold;
}

.declined {
  color: #FF5733;
  font-weight: bold;
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

