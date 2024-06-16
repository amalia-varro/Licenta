<template>
  <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Register</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field v-model="username" label="Username" outlined required></v-text-field>
              <v-text-field v-model="full_name" label="Full Name" outlined required></v-text-field>
              <v-text-field v-model="email" label="Email" outlined required type="password"></v-text-field>
              <v-text-field v-model="password" label="Password" outlined required type="password"></v-text-field>
              <v-btn @click="onRegister" rounded="xl" size="x-large" elevation="24" color="purple-lighten-2" block>
                Register
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import {useUserStore} from "@/stores/user";

export default {
  name: "RegisterPage",
  data() {
    return {
      username: null,
      full_name: null,
      password: null,
      email: null,
      role: "manager",
    };
  },
  setup() {
    return {
      userStore: useUserStore()
    }
  },
  created() {
    this.role = this.$route.query.role ?? "employee"
  },
  methods: {
    async onRegister() {
      try {
        await this.userStore.register(this.username,
          this.password,
          this.email,
          this.full_name,
          this.role)
        this.$swal.fire({
          title: 'Nice!',
          text: 'User registered, please login',
          icon: 'success',
          confirmButtonText: 'Ok'
        });
        this.$router.push({ path: '/login' })
      } catch (e) {
        this.$swal.fire({
          title: 'Error!',
          text: 'Failed to register',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
      }
    }
  }
};
</script>


