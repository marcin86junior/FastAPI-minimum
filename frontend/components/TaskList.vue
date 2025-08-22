<template>
  <div>
    <h2>Lista zadań</h2>
    <p v-if="loading">Ładowanie...</p>
    <table v-else-if="tasks.length > 0" border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Tytuł</th>
          <th>Opis</th>
          <th>Akcje</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.id }}</td>
          <td>{{ task.title }}</td>
          <td>{{ task.description }}</td>
          <td>
            <button class="delete-button" @click="deleteTask(task.id)">Usuń</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>Brak zadań do wyświetlenia.</p>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useTasks } from '~/composables/useTasks';

const { tasks, fetchTasks, updateTask, deleteTask } = useTasks();
const loading = ref(true);
let refreshInterval;

const updateTaskStatus = async (task) => {
  await updateTask(task.id, { completed: task.completed });
};

onMounted(() => {
  fetchTasks().finally(() => loading.value = false);

  // Automatyczne odświeżanie co 30 sekund
  refreshInterval = setInterval(() => {
    fetchTasks();
  }, 30000);
});

onUnmounted(() => {
  clearInterval(refreshInterval);
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 8px;
  text-align: left;
}
.delete-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}
</style>