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
            <button class="delete-button" @click="deleteTask(task.id)">Usuń</button>
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

const deleteTask = async (taskId) => {
  if (confirm('Czy na pewno chcesz usunąć to zadanie?')) {
    try {
      const response = await fetch(`${config.public.apiBase}/tasks/${taskId}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });

      if (response.ok) {
        // Odświeżenie listy zadań po usunięciu
        await fetchTasks();
      } else {
        console.error('Błąd podczas usuwania zadania.');
      }
    } catch (error) {
      console.error('Błąd sieci:', error);
    }
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