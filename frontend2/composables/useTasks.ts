// frontend/composables/useTasks.ts
import { ref, onMounted } from 'vue';

const tasks = ref([]);

export function useTasks() {
  const fetchTasks = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/tasks/', {
        headers: { accept: 'application/json' },
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

  onMounted(fetchTasks);

  return { tasks, fetchTasks };
}