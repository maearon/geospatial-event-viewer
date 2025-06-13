// File: src/views/Home.vue
<template>
  <v-container fluid class="pa-0">
    <v-row no-gutters>
      <v-col cols="12">
        <h1 class="text-h4 font-weight-bold my-6 text-center">Geospatial Events</h1>
      </v-col>

      <v-col cols="12">
        <div ref="mapContainer" class="map-container" />
      </v-col>

      <v-col cols="12">
        <v-divider class="my-6"></v-divider>
      </v-col>

      <v-col
        v-for="event in events"
        :key="event.id"
        cols="12"
        md="6"
        lg="4"
      >
        <v-card elevation="2" class="pa-4" @click="focusOnEvent(event)">
          <v-card-title>{{ event.title }}</v-card-title>
          <v-card-text>
            <p><strong>{{ formatDate(event.timestamp) }}</strong></p>
            <p>{{ event.description }}</p>
            <p>Location: {{ event.location }}</p>
            <p>Coordinates: {{ event.latitude }}, {{ event.longitude }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import mapboxgl from 'mapbox-gl'
import axios from 'axios'
import dayjs from 'dayjs'

const events = ref<any[]>([])
const mapContainer = ref<HTMLElement | null>(null)
let map: mapboxgl.Map

const formatDate = (ts: string) => dayjs(ts).format('DD/MM/YYYY, h:mm:ss A')

const focusOnEvent = (event: any) => {
  if (map) {
    map.flyTo({
      center: [event.longitude, event.latitude],
      zoom: 8,
      speed: 1.2,
    })
  }
}

onMounted(async () => {
  const { data } = await axios.get('http://localhost:8000/api/events/')
  events.value = data.results

  mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN

  map = new mapboxgl.Map({
    container: mapContainer.value!,
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [0, 20],
    zoom: 1.5,
  })

  map.on('load', () => {
    map.resize()

    events.value.forEach((event) => {
      const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(`
        <div class="custom-popup">
          <h3>${event.title}</h3>
          <p>${event.description}</p>
          <p><strong>${formatDate(event.timestamp)}</strong></p>
        </div>
      `)

      new mapboxgl.Marker()
        .setLngLat([event.longitude, event.latitude])
        .setPopup(popup)
        .addTo(map)
    })

    if (events.value.length > 0) {
      focusOnEvent(events.value[0])
    }
  })
})
</script>

<style scoped>
.map-container {
  height: calc(100vh - 240px);
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
}

:deep(.mapboxgl-popup-content) {
  font-family: 'Roboto', sans-serif;
  padding: 12px 16px;
  border-radius: 8px;
  background-color: white;
  color: #212121;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  max-width: 300px;
  z-index: 9999;
}

:deep(.mapboxgl-popup-content h3) {
  margin: 0 0 8px;
  font-size: 16px;
  color: #1e88e5;
}

:deep(.mapboxgl-popup-content p) {
  margin: 4px 0;
  font-size: 14px;
}
</style>
