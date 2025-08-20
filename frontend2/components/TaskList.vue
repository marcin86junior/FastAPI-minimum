<!-- frontend/components/TaskList.vue -->
<template>
  <div>
    <ul>
      <li v-for="task in tasks" :key="task.id">{{ task.name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useTasks } from '~/composables/useTasks';

const { tasks, fetchTasks } = useTasks();

onMounted(() => {
  fetchTasks();
  setInterval(fetchTasks, 5000); // Automatyczne odświeżanie co 5 sekund
});
</script>