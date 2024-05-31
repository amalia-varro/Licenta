<script>
export default {
  name: "LoginPage",
  data() {
    return {
      username: null,
      password: null
    }
  }
}
</script>

<template>
  <v-container fluid fill-height>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Login</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field v-model="username" label="Username" outlined required></v-text-field>
              <v-text-field v-model="password" label="Password" outlined required type="password"></v-text-field>
              <v-btn rounded="xl" size="x-large" elevation="24" type="submit" color="purple-lighten-2" block>Login</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped lang="sass">

</style>
