<template>
  <div>
    <v-container>
      <h1 class="text-h4 mb-6">Geospatial Events</h1>

      <v-alert v-if="error" type="error" class="mb-4">
        {{ error }}
      </v-alert>

      <v-skeleton-loader v-if="loading" type="card" class="mb-4" />

      <div v-else>
        <div id="map" class="mb-6" style="height: 500px; border-radius: 8px; overflow: hidden"></div>

        <v-row>
          <v-col
            v-for="event in events"
            :key="event.id"
            cols="12"
            md="6"
          >
            <v-card>
              <v-card-title>{{ event.title }}</v-card-title>
              <v-card-subtitle>
                {{ formatDate(event.timestamp) }}
              </v-card-subtitle>
              <v-card-text>
                <p>{{ event.description }}</p>
                <p><strong>Location:</strong> {{ event.location }}</p>
                <p><strong>Coordinates:</strong> {{ event.latitude }}, {{ event.longitude }}</p>
                <v-img
                  v-if="event.image"
                  :src="event.image"
                  max-height="200"
                  contain
                  class="mt-3"
                />
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import mapboxgl from 'mapbox-gl'

interface Event {
  id: number
  title: string
  description: string
  location: string
  latitude: number
  longitude: number
  timestamp: string
  image?: string
}

const events = ref<Event[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

const fetchEvents = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/events/')
    events.value = res.data.results || res.data
  } catch (err: any) {
    error.value = err?.response?.data?.detail || 'Failed to load events'
  } finally {
    loading.value = false
  }
}

const formatDate = (timestamp: string) => {
  const date = new Date(timestamp)
  return date.toLocaleString()
}

const initMap = () => {
  mapboxgl.accessToken = 'YOUR_MAPBOX_ACCESS_TOKEN'

  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [0, 0],
    zoom: 2
  })

  events.value.forEach((event) => {
    const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(`
      <h3>${event.title}</h3>
      <p>${event.description}</p>
      <small>${formatDate(event.timestamp)}</small>
    `)

    new mapboxgl.Marker()
      .setLngLat([event.longitude, event.latitude])
      .setPopup(popup)
      .addTo(map)
  })
}

onMounted(async () => {
  await fetchEvents()
  initMap()
})
</script>

<style scoped>
#map {
  width: 100%;
}
</style>