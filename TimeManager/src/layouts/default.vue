<template>
  <v-app>
    <v-card>
      <v-layout>
        <v-app-bar color="purple-lighten-2" prominent>
          <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

          <v-toolbar-title>Time Flow Manager
            <v-icon>
              mdi-clock-time-four-outline
            </v-icon>
          </v-toolbar-title>

          <v-spacer></v-spacer>
          <v-btn icon="mdi-account" variant="text"></v-btn>
          <v-btn variant="text">{{ userStore.fullName ?? "Hello!" }}</v-btn>
          <v-btn icon="mdi-dots-vertical" variant="text" @click="toggleMenu"></v-btn>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer" :location="$vuetify.display.mobile ? 'bottom' : undefined" temporary>
          <v-list>
            <v-list-item v-for="item in routeItems" :key="item.title">
              <router-link :to="item.route" class="v-list-item--link">
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </router-link>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>

        <div class="gradient-background">
          <!-- Dropdown menu -->
          <v-menu v-model="menuOpen" class="menu-model" v-if="userStore.isLoggedIn">
            <!-- Menu items -->
            <v-list>
              <v-list-item @click="logout">
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>

        <v-main>
          <router-view/>
        </v-main>

      </v-layout>
    </v-card>
    <AppFooter/>
  </v-app>
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
import { mdiAccount, mdiClockTimeFourOutline, mdiDotsVertical } from "@mdi/js";
import {useUserStore} from "@/stores/user";

export default {
  name: "DefaultLayout",
  components: { AppFooter },
  data: () => ({
    mdiAccount,
    mdiClockTimeFourOutline,
    mdiDotsVertical,
    drawer: false,
    menuOpen: false,
    items: [
      { title: 'Attendance History', route: '/attendance', role: "manager" },
      { title: 'WorkLog', route: '/', role: "employee" },
      { title: 'Team Teleworking', route: '/teamteleworking', role: "manager" },
      { title: 'Team Vacation', route: '/teamvacation', role: "manager" },
      { title: 'Teleworking Request', route: '/teleworking', role: "employee" },
      { title: 'Vacation Request', route: '/vacation', role: "employee" },
      // { title: 'Team Timesheet', route: '/' },
      // { title: 'Team Teleworking Request', route: '/' },
      // { title: 'Team Vacation Request', route: '/' }
    ]
  }),
  setup() {
    return {
      userStore: useUserStore()
    }
  },
  computed: {
    routeItems() {
      let userRole = this.userStore.role
      return this.items.filter(i => i.role === userRole)
    }
  },
  mounted() {
    this.userStore.checkLogin()
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    goToProfile() {
      // Add your logic to navigate to the profile page
    },
    logout() {
      // Add your logic to handle logout, such as clearing tokens or user data
      this.userStore.logout()
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
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
