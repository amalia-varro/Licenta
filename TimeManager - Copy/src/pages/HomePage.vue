<script>
export default {
  data() {
    return {
      loginTime: null,
      logoutTime: null,
      loginModal: false,
      logoutModal: false,
      isChecked: false,
      showPopup: false,
      headers: [
        { title: 'Project', align: 'start', key: 'name' },
        { title: 'Time', align: 'end', key: 'time' },
        { title: 'Comments', align: 'end', key: 'time' }
      ],
      desserts: [
        { name: 'Test Analysis', time: '' },
        { name: 'Test Scripting', time: '' },
        { name: 'Debugging', time: '' },
        { name: 'Meetings', time: '' }
      ],
      dialogVisible: false,
      selectedRow: null,
      selectedRows: [],
    };
  },
  methods: {
    login() {
      // Implement your login logic here
    },
    logout() {
      // Implement your logout logic here
    },
    onRowClick(item) {
      // Perform action when a row is selected
      console.log('Row selected:', item);
      console.log('Row selected:', item);
      // You can perform any action you want here, such as updating a state or displaying a dialog
      this.selectedRow = item;
      this.dialogVisible = true;
      this.isChecked = true;
    },
    toggleCheckbox(item) {
      // Open dialog when checkbox is clicked
      if (!this.selectedRows.includes(item)) {
        this.selectedRow = item;
        this.dialogVisible = true;
      } else {
        this.dialogVisible = false;
      }
    },
    closeDialog() {
      this.dialogVisible = false;
    }
  }
};
</script>



<template>
  <div class="container">
    <!-- Left Section -->
    <div class="left-section">
      <v-date-picker width="400"></v-date-picker>
    </div>
    <!-- Right Section -->
    <div class="right-section">
      <v-col cols="6">
        <!-- Login Time Picker -->
        <div class="time-picker-container">
          <v-text-field
            class="time-picker-field"
            v-model="loginTime"
            :active="loginModal"
            :focused="loginModal"
            label="Login Hour"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
          >
            <v-dialog
              v-model="loginModal"
              activator="parent"
              width="auto"
            >
              <v-time-picker
                format="24hr"
                v-if="loginModal"
                v-model="loginTime"
              ></v-time-picker>
            </v-dialog>
          </v-text-field>
          <!-- Login Button -->
          <v-btn rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2" @click="login" class="button-margin">Login</v-btn>
        </div>
        <!-- Logout Time Picker -->
        <div class="time-picker-container">
          <v-text-field
            class="time-picker-field"
            v-model="logoutTime"
            :active="logoutModal"
            :focused="logoutModal"
            label="Logout Hour"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
          >
            <v-dialog
              v-model="logoutModal"
              activator="parent"
              width="auto"
            >
              <v-time-picker
                format="24hr"
                v-if="logoutModal"
                v-model="logoutTime"
              ></v-time-picker>
            </v-dialog>
          </v-text-field>
          <!-- Logout Button -->
          <v-btn rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2" @click="logout" class="button-margin">Logout</v-btn>
        </div>
        <v-combobox
          label="Break"
          :items="['10 min', '20 min', '30 min', '40 min', '50 min', '1 h']"
          prepend-icon="mdi-clock-time-four-outline"
        ></v-combobox>
      </v-col>

    </div>
  </div>
  <!-- Add container for the table with fixed height and scroll -->
  <div class="table-container">
    <v-data-table
      :headers="headers"
      :items="desserts"
      :item-value="item => `${item.name}-${item.version}`"
      items-per-page="5"
      select-strategy="single"
      show-select
      @click:row="onRowClick"
    >
      <template v-slot:item="{ item }">
        <tr @click="toggleCheckbox(item)">
          <td>
            <v-checkbox v-model="selectedRows" :value="item"></v-checkbox>
          </td>
          <td>{{ item.name }}</td>
        </tr>
      </template>

    </v-data-table>

    <v-dialog v-model="dialogVisible" max-width="500">
      <v-card>
        <v-card-title>
          Dialog Content
        </v-card-title>
        <v-card-text>
          <!-- Dialog content goes here -->
          <p>You clicked on: {{ selectedRow }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="closeDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>


</template>



<style scoped>

.container {
  display: flex;
}

.left-section {
  display: flex;
  margin-left: 0px;
  margin-right: 100px;
}
.right-section {
  flex: 1;
  padding: 20px;
}

.right-section {
  display: flex;
  flex-direction: column;
}

.time-picker-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 50px;
  margin-top: 60px;
}

.button-margin {
  margin-left: 10px;
}

.table-container {
  max-height: 1000px; /* set the height as per your requirement */
  overflow-y: auto; /* add scroll when content exceeds the height */
}

.body {
    overflow-y: auto;
  }

</style>
