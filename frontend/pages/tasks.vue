<template>
  <div>
    <h1>Lista zadań</h1>
    <table v-if="tasks.length > 0" border="1">
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
            <button class="delete-button" @click="handleDeleteTask(task.id)">Usuń</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>Brak zadań do wyświetlenia.</p>
  </div>
</template>

<script setup>
// Dodanie middleware autoryzacji
definePageMeta({
  middleware: ['auth']
});

import { onMounted } from 'vue';
import { useAuth } from '~/composables/useAuth';
import { useTasks } from '~/composables/useTasks';

const { isAuthenticated } = useAuth();
const { tasks, fetchTasks, deleteTask } = useTasks();

const handleDeleteTask = async (taskId) => {
  if (confirm('Czy na pewno chcesz usunąć to zadanie?')) {
    await deleteTask(taskId);
  }
};

onMounted(() => {
  // Sprawdź czy użytkownik jest zalogowany
  if (isAuthenticated.value) {
    fetchTasks();
  }
});
</script>

<style>
.completed {
  text-decoration: line-through;
  color: gray;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
th, td {
  padding: 0.5rem;
  text-align: left;
}
th {
  background-color: #f4f4f4;
}
.delete-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 3px;
}
.delete-button:hover {
  background-color: #d32f2f;
}
</style>