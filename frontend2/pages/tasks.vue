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
            <button @click="toggleTask(task.id)">Zmień status</button>
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

import { ref, onMounted } from 'vue';
import { useRuntimeConfig } from '#app';
import { useAuth } from '~/composables/useAuth';

const tasks = ref([]);
const config = useRuntimeConfig();
const { isAuthenticated } = useAuth();

const fetchTasks = async () => {
  try {
    const response = await fetch(`${config.public.apiBase}/tasks`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
    });
    if (response.ok) {
      tasks.value = await response.json();
    } else {
      console.error('Błąd podczas pobierania zadań.');
    }
  } catch (error) {
    console.error('Błąd sieci:', error);
  }
};

const toggleTask = async (taskId) => {
  try {
    const response = await fetch(`${config.public.apiBase}/tasks/${taskId}/toggle`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
    });
    if (response.ok) {
      await fetchTasks(); // Odśwież listę zadań
    } else {
      console.error('Błąd podczas zmiany statusu zadania.');
    }
  } catch (error) {
    console.error('Błąd sieci:', error);
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
</style>