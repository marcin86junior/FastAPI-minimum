<template>
  <div>
    <h1> </h1>
    <TaskForm />
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['auth']
});

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useRuntimeConfig } from '#app';

const title = ref('');
const description = ref('');
const createError = ref('');
const createSuccess = ref('');
const isSubmitting = ref(false);
const router = useRouter();
const config = useRuntimeConfig();

const handleCreateTask = async () => {
  try {
    createError.value = '';
    createSuccess.value = '';
    isSubmitting.value = true;

    const token = localStorage.getItem('access_token');
    console.log('Token:', token); // Sprawdź czy token istnieje

    if (!token) {
      createError.value = 'Brak tokenu autoryzacji. Zaloguj się ponownie.';
      return;
    }

    const response = await fetch(`${config.public.apiBase}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        title: title.value,
        description: description.value
      }),
    });

    console.log('Response status:', response.status);

    if (response.ok) {
      // reszta kodu bez zmian
    } else {
      const data = await response.json().catch(() => ({}));
      createError.value = data.detail || 'Błąd podczas dodawania zadania.';
      console.error('Error response:', data);
    }
  } catch (error) {
    // reszta kodu bez zmian
  }
};

const goToTasksList = () => {
  router.push('/tasks');
};
</script>

<style scoped>
.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

.form-buttons {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

button {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.cancel-button {
  background-color: #9e9e9e;
}

button:hover {
  opacity: 0.9;
}

button:disabled {
  background-color: #cccccc;
}

.error {
  color: red;
  margin-top: 10px;
}

.success {
  color: green;
  margin-top: 10px;
}
</style>