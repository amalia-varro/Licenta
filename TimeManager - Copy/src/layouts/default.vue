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

          <template v-if="$vuetify.display.mdAndUp">
            <v-btn icon="mdi-magnify" variant="text"></v-btn>

            <v-btn icon="mdi-filter" variant="text"></v-btn>
          </template>

          <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>
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
          <!-- Your component content here -->
        </div>
        <v-main style="padding-left: 300px">
          <v-card-text>
            <router-view/>
          </v-card-text>
        </v-main>

      </v-layout>
    </v-card>
    <AppFooter/>
  </v-app>
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
export default {
  name: "DefaultLayout",
  components: {AppFooter},
  data: () => ({
    drawer: false,
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
}

</script>
