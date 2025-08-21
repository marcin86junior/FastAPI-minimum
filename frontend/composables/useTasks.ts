// frontend/composables/useTasks.ts
import { ref, onMounted } from 'vue';
import { useRuntimeConfig } from '#app';

export function useTasks() {
  const tasks = ref([]);
  const config = useRuntimeConfig();

  const fetchTasks = async () => {
    try {
      const response = await fetch(`${config.public.apiBase}/tasks`, {
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });
      if (response.ok) {
        tasks.value = await response.json();
      } else {
        console.error('Błąd podczas pobierania zadań');
      }
    } catch (error) {
      console.error('Błąd sieci:', error);
    }
  };

  const addTask = async (task) => {
    try {
      const response = await fetch(`${config.public.apiBase}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
        body: JSON.stringify(task),
      });

      if (response.ok) {
        await fetchTasks(); // Odświeżenie listy po dodaniu
        return true;
      } else {
        console.error('Błąd podczas dodawania zadania');
        return false;
      }
    } catch (error) {
      console.error('Błąd sieci:', error);
      return false;
    }
  };

  const updateTask = async (taskId, taskData) => {
    try {
      const response = await fetch(`${config.public.apiBase}/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
        body: JSON.stringify(taskData),
      });

      if (response.ok) {
        await fetchTasks(); // Odświeżenie listy po aktualizacji
        return true;
      } else {
        console.error('Błąd podczas aktualizacji zadania');
        return false;
      }
    } catch (error) {
      console.error('Błąd sieci:', error);
      return false;
    }
  };

  const deleteTask = async (taskId) => {
    try {
      const response = await fetch(`${config.public.apiBase}/tasks/${taskId}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });

      if (response.ok) {
        await fetchTasks(); // Odświeżenie listy po usunięciu
        return true;
      } else {
        console.error('Błąd podczas usuwania zadania');
        return false;
      }
    } catch (error) {
      console.error('Błąd sieci:', error);
      return false;
    }
  };

  // Opcjonalnie możesz wywołać fetchTasks podczas montowania komponentu
  // Ale lepiej wywoływać to w komponentach, gdy już wiemy, że użytkownik jest zalogowany

  return {
    tasks,
    fetchTasks,
    addTask,
    updateTask,
    deleteTask
  };
}