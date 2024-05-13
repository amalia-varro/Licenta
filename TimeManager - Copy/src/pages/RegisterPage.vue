<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      username: null,
      password: null,
      email: null
    };
  }
};
</script>

<template>
    <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Register</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field v-model="username" label="Username" outlined required></v-text-field>
              <v-text-field v-model="email" label="Email" outlined required type="password"></v-text-field>
              <v-text-field v-model="password" label="Password" outlined required type="password"></v-text-field>
              <v-text-field v-model="password" label="Confirm Password" outlined required type="password"></v-text-field>
              <v-btn rounded="xl" size="x-large" elevation="24" type="submit" color="purple-lighten-3" block>Register</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>



