<template>
  <v-app>
    <v-app-bar app color="indigo" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Executive Buttton</v-toolbar-title>
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer fixed app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>
