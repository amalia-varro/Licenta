<template>
  <v-app>
    <v-card>
      <v-layout>
        <v-app-bar
          color="purple-lighten-2"
          prominent
        >
          <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

          <v-toolbar-title>Time Flow Manager</v-toolbar-title>

          <v-spacer></v-spacer>
          <v-btn icon="mdi-account" variant="text"></v-btn>
          <v-btn variant="text">Amalia Varro</v-btn>
          <v-btn icon="mdi-dots-vertical" variant="text" @click="toggleMenu"></v-btn>
        </v-app-bar>

        <v-navigation-drawer
          v-model="drawer"
          :location="$vuetify.display.mobile ? 'bottom' : undefined"
          temporary
        >
          <v-list
            :items="items"
          ></v-list>
        </v-navigation-drawer>
        <div class="gradient-background">
          <!-- Dropdown menu -->
          <v-menu v-model="menuOpen" class="menu-model">
            <!-- Menu items -->
            <v-list>
              <v-list-item @click="goToProfile">
                <v-list-item-title>My Profile</v-list-item-title>
              </v-list-item>
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
import { mdiAccount, mdiDelete, mdiPencil, mdiShareVariant } from "@mdi/js";

export default {
  name: "DefaultLayout",
  components: {AppFooter},
  data: () => ({
    mdiAccount,
    mdiPencil,
    mdiShareVariant,
    mdiDelete,
    drawer: false,
    menuOpen: false, // Initialize menuOpen to false
    group: null,
    items: [
      {
        title: 'Attendance Record',
        value: 'Attendance Record',
      },
      {
        title: 'Attendance History',
        value: 'Attendance History',
      },
      {
        title: 'Teleworking Request',
        value: 'Teleworking Request',
      },
      {
        title: 'Vacation Request',
        value: 'Vacation Request',
      },
    ],

  }),
  watch: {
    group() {
      this.drawer = false
    },
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
      console.log('dots tapped');
    },
    goToProfile() {
      // Add your logic to navigate to the profile page
    },
    logout() {
      // Add your logic to handle logout
    }
  }
};

</script>

<style>
.menu-wrapper {
  position: relative;
  display: inline-block;
  margin-right: 10px; /* Adjust margin as needed */
}

.menu-model {
  margin-top: 8vh;
  margin-left: 91vw;
}
</style>
