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
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Login</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field v-model="username" label="Username" outlined required></v-text-field>
              <v-text-field v-model="password" label="Password" outlined required type="password"></v-text-field>
              <v-btn rounded="xl" size="x-large" elevation="24" type="submit" color="purple-lighten-3" block>Login</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
        <v-list lines="one">
          <v-list-item
            v-for="n in 30"
            :key="n"
            :title="'Item ' + n"
            subtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit"
          ></v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
  .divex3 {
  overflow-y: auto;
}
</style>
