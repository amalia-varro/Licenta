<template>
  <v-container fluid fill-height class="height-top">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Login</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field v-model="username" label="Username" outlined required></v-text-field>
              <v-text-field v-model="password" label="Password" outlined required type="password"></v-text-field>
              <v-btn @click="onLogin()" rounded="xl" size="x-large" elevation="24" color="purple-lighten-2" block>Login</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
        <router-link class="d-block py-5" :to="{'path': '/register', query: {'role': 'manager'}}">Register as a manager</router-link>
        <router-link class="d-block" :to="{'path': '/register', query: {'role': 'employee'}}">Register as a employee</router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {useUserStore} from "@/stores/user";

export default {
  name: "LoginPage",
  data() {
    return {
      username: null,
      password: null
    }
  },
  setup() {
    return {
      userStore: useUserStore()
    }
  },
  methods: {
    async onLogin() {
      try {
        await this.userStore.login(this.username, this.password)
        this.$router.push({ path: '/vacation' })
      } catch (e) {
        console.error(e)
        this.$swal.fire({
          title: 'Error!',
          text: 'Failed to login',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
      }
    }
  }
}
</script>

<style>
.height-top {
  padding-top: 50px;
}
</style>
