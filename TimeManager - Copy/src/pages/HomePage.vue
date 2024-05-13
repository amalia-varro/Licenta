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
        {title: 'Project', align: 'start', key: 'name'},
        {title: 'Time', align: '', key: 'time'},
        {title: 'Comments', align: '', key: 'time'}
      ],
      desserts: [
        {name: 'Test Analysis', time: ''},
        {name: 'Test Scripting', time: ''},
        {name: 'Debugging', time: ''},
        {name: 'Meetings', time: ''}
      ],
      dialogVisible: false,
      selectedRow: null,
      selectedRows: [],
      selectedDropdown1: null,
      selectedDropdown2: null,
      dropdownOptions1: [0, 1, 2, 3, 4, 5, 6, 7, 8],
      dropdownOptions2: [10, 20, 30, 40, 50],
      inputField: '',
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
    },
    saveInformation() {
      this.dialogVisible = false;

      // Save selected hour and minute values to the selected row
      this.selectedRow.selectedHour = this.selectedDropdown1;
      this.selectedRow.selectedMinute = this.selectedDropdown2;
      this.selectedRow.comments = this.inputField;

      // Close dialog
      this.dialogVisible = false;
    }
  }
};
</script>


<template>
  <v-container>
    <!-- Left Section -->
    <v-row>
      <v-col cols="6">
        <v-date-picker></v-date-picker>
      </v-col>
      <!-- Right Section -->
      <v-col cols="6" class="margin-top-right-section">
        <!-- Login Time Picker -->
        <v-row>
          <v-col cols="8">
            <v-text-field
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
          </v-col>
          <v-col cols="4">
            <!-- Login Button -->
            <v-btn rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2" @click="login"
                   class="button-margin">Login
            </v-btn>
          </v-col>
        </v-row>

        <!-- Logout Time Picker -->
        <v-row>
          <v-col cols="8">
            <v-text-field
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
          </v-col>
          <v-col cols="4">
            <!-- Logout Button -->
            <v-btn rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2" @click="logout"
                   class="button-margin">Logout
            </v-btn>
          </v-col>
        </v-row>
        <v-combobox
          label="Break"
          :items="['10 min', '20 min', '30 min', '40 min', '50 min', '1 h']"
          prepend-icon="mdi-clock-time-four-outline"
        ></v-combobox>
      </v-col>
    </v-row>
    <!-- Add container for the table with fixed height and scroll -->
    <v-row>
      <v-col cols="12">
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
              <td>{{ item.selectedHour }} hours {{ item.selectedMinute }} minutes</td>
              <td>{{ item.comments }}</td>
            </tr>
          </template>

        </v-data-table>

        <v-dialog v-model="dialogVisible" max-width="500">
          <v-card>
            <v-card-title>
              Worked hours
            </v-card-title>
            <v-card-text>
              <v-row>
                <!-- Hourglass icon -->
                <v-col cols="1">
                  <v-icon>mdi-hourglass</v-icon>
                </v-col>
                <!-- Dropdowns -->
                <v-col cols="4">
                  <v-select
                    v-model="selectedDropdown1"
                    :items="dropdownOptions1"
                    label="Hours"
                  ></v-select>
                </v-col>
                <v-col cols="4">
                  <v-select
                    v-model="selectedDropdown2"
                    :items="dropdownOptions2"
                    label="Minutes"
                  ></v-select>
                </v-col>
              </v-row>
              <!-- Input field -->
              <v-text-field v-model="inputField" label="Comments"></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="closeDialog">Close</v-btn>
              <v-btn color="primary" @click="saveInformation">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>

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

.margin-top-right-section {
  margin-top: 20vh;
}

</style>
