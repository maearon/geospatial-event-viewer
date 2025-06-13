<template>
  <v-container>
    <h1 class="text-h4 font-weight-bold mb-4">Geospatial Events</h1>

    <div ref="mapContainer" class="map-container" />

    <v-divider class="my-6"></v-divider>

    <div v-for="event in events" :key="event.id" class="mb-6">
      <v-card elevation="2" class="pa-4">
        <v-card-title>{{ event.title }}</v-card-title>
        <v-card-text>
          <p><strong>{{ formatDate(event.timestamp) }}</strong></p>
          <p>{{ event.description }}</p>
          <p>Location: {{ event.location }}</p>
          <p>Coordinates: {{ event.latitude }}, {{ event.longitude }}</p>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import mapboxgl from 'mapbox-gl'
import axios from 'axios'
import dayjs from 'dayjs'

const events = ref<any[]>([])
const mapContainer = ref<HTMLElement | null>(null)

const formatDate = (ts: string) => dayjs(ts).format('DD/MM/YYYY, h:mm:ss A')

onMounted(async () => {
  const { data } = await axios.get('http://localhost:8000/api/events/')
  events.value = data.results

  mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN
  const map = new mapboxgl.Map({
    container: mapContainer.value!,
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [0, 20], // Default world center
    zoom: 1.5,
  })

  events.value.forEach((event) => {
    const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(`
      <h3>${event.title}</h3>
      <p>${event.description}</p>
      <p><strong>${formatDate(event.timestamp)}</strong></p>
    `)

    new mapboxgl.Marker()
      .setLngLat([event.longitude, event.latitude])
      .setPopup(popup)
      .addTo(map)
  })
})
</script>

<style scoped>
.map-container {
  height: 500px;
  width: 100%;
  margin-bottom: 30px;
  border-radius: 8px;
  overflow: hidden;
}
</style>
