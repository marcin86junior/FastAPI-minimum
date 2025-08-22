<template>
  <div>
    <TaskList />
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