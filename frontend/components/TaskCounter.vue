<template>
  <div class="task-counter">
    <h3>Podsumowanie zadań</h3>
    <p>Ilość zadań: {{ totalTasks }}</p>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useTasks } from '~/composables/useTasks';

const { tasks, fetchTasks } = useTasks();
const currentTime = ref('');
const lastRefresh = ref('');
let clockInterval;

const updateTime = () => {
  const now = new Date();
  currentTime.value = now.toLocaleTimeString();
};

const refreshTasks = async () => {
  await fetchTasks();
  lastRefresh.value = new Date().toLocaleTimeString();
};

const completedTasks = computed(() => 
  tasks.value.filter(task => task.completed).length
);

const totalTasks = computed(() => tasks.value.length);

const progressPercentage = computed(() => {
  if (totalTasks.value === 0) return 0;
  return Math.round((completedTasks.value / totalTasks.value) * 100);
});

// Obserwuj zmiany w zadaniach
watch(tasks, () => {
  // Możesz dodać dodatkowe akcje przy zmianach zadań
}, { deep: true });

onMounted(() => {
  updateTime();
  refreshTasks();
  
  // Aktualizacja zegara co sekundę
  clockInterval = setInterval(updateTime, 1000);
});

onUnmounted(() => {
  clearInterval(clockInterval);
});
</script>

<style scoped>
.task-counter {
  background-color: #f8f9fa;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 20px;
  border: 1px solid #dee2e6;
}
</style>