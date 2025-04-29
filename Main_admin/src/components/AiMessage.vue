<script setup>
import {defineProps} from 'vue'
const props=defineProps({
  message:{
    type:String,
    default:"默认值"
  }
})
</script>
<template>
  <div class="my-message">{{ message }}</div>
</template>
<style scoped>
.my-message{
    max-width: 600px;
    display: inline-block;
    width: auto;
    background-color: white;
    border-radius: 10px;
    padding: 20px;
}
</style>