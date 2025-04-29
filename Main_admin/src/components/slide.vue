<script setup>
import { ref } from 'vue'
const window = ref(0)
</script>
<template>
    
    <v-carousel show-arrows="hover" cycle="true">
        <v-carousel-item class="img" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" cover></v-carousel-item>

        <v-carousel-item class="img" src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg" cover></v-carousel-item>

        <v-carousel-item class="img" src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" cover></v-carousel-item>
    </v-carousel>
</template>
<style scoped>
img {
    border-radius: 10px;
    height: 100%;
}
</style>