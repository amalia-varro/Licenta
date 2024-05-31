<template>
  <div class="manager-view">
    <h1 class="title">My Team Timesheet</h1>
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
        <th>Total Hours</th>
        <th v-for="(day, index) in daysInMonth" :key="index" :class="{'weekend': isWeekend(day)}">
          {{ day }} <span v-if="isWeekend(day)">W</span>
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="employee in filteredEmployees" :key="employee.name">
        <td>{{ employee.name }}</td>
        <td>{{ employee.totalHours }}</td>
        <td v-for="(day, index) in daysInMonth" :key="index" :class="{'weekend': isWeekend(day)}">
          <!-- Placeholder for employee's hours per day -->
          {{ getEmployeeHours(employee, day) }}
        </td>
      </tr>
      </tbody>
    </table>
    <v-container>
      <v-row class="mt-5">
        <v-spacer/>
        <v-col cols="6">
          <TimesheetChart :employees="employees"/>
        </v-col>
        <v-spacer/>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import TimesheetChart from "@/components/TimesheetChart.vue";

export default {
  components: {TimesheetChart},
  data() {
    return {
      searchQuery: '',
      selectedMonth: '2024-05',
      employees: [
        { name: 'John Doe', totalHours: 160, dailyHours: { 1: 8, 2: 8, /* ... */ 31: 8 } },
        { name: 'Jane Smith', totalHours: 150, dailyHours: { 1: 8, 2: 7, /* ... */ 31: 7 } },
        // More employees
      ],
    };
  },
  computed: {
    filteredEmployees() {
      return this.employees.filter(employee =>
        employee.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    daysInMonth() {
      const [year, month] = this.selectedMonth.split('-');
      const date = new Date(year, month, 0);
      return Array.from({ length: date.getDate() }, (_, i) => i + 1);
    }
  },
  methods: {
    searchEmployee() {
      // Implement search functionality if needed
      console.log('Searching for:', this.searchQuery);
    },
    updateCalendar() {
      // Handle calendar update if needed
      console.log('Selected month:', this.selectedMonth);
    },
    isWeekend(day) {
      const [year, month] = this.selectedMonth.split('-');
      const date = new Date(year, month - 1, day);
      const dayOfWeek = date.getDay();
      return dayOfWeek === 0 || dayOfWeek === 6;
    },
    getEmployeeHours(employee, day) {
      return employee.dailyHours[day] || 0;
    }
  }
};
</script>

<style scoped>
/* Stilizare pentru manager-view */
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
  padding: 10px 20px; /* Spatiere interna */
  width: 300px; /* Lățimea dorită a câmpului de căutare */
}

/* Stilizare pentru butonul de căutare */
.search-button {
  display: flex;
  justify-content: center; /* Așeză elementele pe axa principală */
  align-items: center; /* Așeză elementele pe axa secundară */
  background-color: #ba68c8;
  border: none;
  border-radius: 50%; /* Buton rotund */
  padding: 10px;
  cursor: pointer;
}

.search-button svg {
  fill: white;
  width: 20px;
  height: 20px;
}

/* Stilizare pentru tabel */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  border-radius: 10px;
  overflow: hidden; /* Ascunde overflow-ul dacă există */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Adaugă o umbră subtilă */
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

/* Stilizare pentru rândurile din tabel */
tr:nth-child(even) {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #e1c8e4;
}

/* Stilizare pentru zilele de weekend */
.weekend {
  background-color: #f0f0f0;
  color: #605b5b;
}

/* Stilizare pentru inputul de tip month */
input[type="month"] {
  -webkit-appearance: none;
}

input[type="month"]::-webkit-calendar-picker-indicator {
  color: white;
  padding: 0.5em;
  border: none;
}

input[type="month"]::-webkit-calendar-picker-indicator:hover {

}

input[type="month"]:focus::-webkit-calendar-picker-indicator {
  background-color: #ba68c8;
  color: white;
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

