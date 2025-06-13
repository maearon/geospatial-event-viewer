/ File: src/App.vue
<template>
  <v-app class="app">
    <Header />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useSessionStore } from './stores/session'
import Header from './layouts/Header.vue'
import Footer from './layouts/Footer.vue'

const sessionStore = useSessionStore()

onMounted(async () => {
  await sessionStore.fetchUser()
})
</script>

<style>
.app {
  font-family: var(--font-geist-sans), sans-serif;
  background-color: #f8f9fa;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.v-main {
  flex-grow: 1;
}
</style>