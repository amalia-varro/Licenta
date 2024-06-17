<template>
  <v-container>
    <!-- Left Section -->
    <v-row>
      <v-col cols="6">
        <v-date-picker v-model="selectedDate"></v-date-picker>
      </v-col>
      <!-- Right Section -->
      <v-col cols="6" class="margin-top-right-section">
        <!-- Login Time Picker -->
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="loginTime"
              :active="loginModal"
              :focused="loginModal"
              label="Start Hour"
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
        </v-row>

        <!-- Logout Time Picker -->
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="logoutTime"
              :active="logoutModal"
              :focused="logoutModal"
              label="End Hour"
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
        </v-row>
        <v-combobox
          v-model="selectedBreak"
          label="Break"
          :items="['10 min', '20 min', '30 min', '40 min', '50 min', '60 min']"
          prepend-icon="mdi-clock-time-four-outline"
        ></v-combobox>
      </v-col>
      <v-col cols="12" class="text-center">
        <v-btn rounded="xl" size="large" elevation="24" type="submit" color="purple-lighten-2" @click="submitWorklog"
               class="button-margin">Submit Worklog
        </v-btn>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import {useUserStore} from "@/stores/user";
import {useWorklogStore} from "@/stores/worklog";
import moment from "moment";

export default {
  data() {
    return {
      selectedDate: null,
      selectedBreak: null,
      loginTime: null,
      logoutTime: null,
      loginModal: false,
      logoutModal: false,
      isChecked: false,
      showPopup: false,
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
  setup() {
    return {
      userStore: useUserStore(),
      worklogStore: useWorklogStore()
    }
  },
  async mounted() {
    this.userStore.checkLogin()
    if (!this.userStore.isLoggedIn) {
      this.$router.push({path: '/login'})
    }
  },
  methods: {
    async submitWorklog() {
      let breakTime = this.selectedBreak.split(" ")[0]
      if (breakTime === "60") {
        breakTime = "00"
      }
      try {
        console.log("submit worklog", this.selectedDate, this.loginTime, this.logoutTime, this.selectedBreak)
        await this.worklogStore.submitWorklog({
          "user_id": this.userStore.userId,
          "project_id": 1,
          "date": moment(this.selectedDate).format("YYYY-MM-DD"),
          "start_hour": this.loginTime,
          "end_hour": this.logoutTime,
          "break_start_hour": `13:${breakTime}:00.289Z`,
          "break_end_hour": "13:00:00.289Z"
        })
      } catch (e) {
        this.$swal.fire({
          title: 'Error!',
          text: 'Failed to submit worklog',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
      }
    }
  }
};
</script>


<style scoped>

.button-margin {
  margin-left: 10px;
}

.margin-top-right-section {
  margin-top: 20vh;
}

</style>
