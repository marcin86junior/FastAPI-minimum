<template>
  <div>
    <h1>Dodaj nowe zadanie</h1>
    <form @submit.prevent="handleCreateTask">
      <div class="form-group">
        <label for="title">Tytuł:</label>
        <input id="title" v-model="title" type="text" required />
      </div>
      <div class="form-group">
        <label for="description">Opis:</label>
        <textarea id="description" v-model="description" rows="4" required></textarea>
      </div>
      <div class="form-buttons">
        <button type="submit" :disabled="isSubmitting">Dodaj zadanie</button>
        <button type="button" class="cancel-button" @click="goToTasksList">Anuluj</button>
      </div>
    </form>
    <p v-if="createError" class="error">{{ createError }}</p>
    <p v-if="createSuccess" class="success">{{ createSuccess }}</p>
  </div>
</template>

<script setup>
// Dodanie middleware autoryzacji
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

    const response = await fetch(`${config.public.apiBase}/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      },
      body: JSON.stringify({
        title: title.value,
        description: description.value
      }),
    });

    if (response.ok) {
      createSuccess.value = 'Zadanie zostało dodane pomyślnie!';
      // Resetowanie formularza
      title.value = '';
      description.value = '';

      // Przekierowanie po 2 sekundach
      setTimeout(() => {
        router.push('/tasks');
      }, 2000);
    } else {
      const data = await response.json();
      createError.value = data.detail || 'Błąd podczas dodawania zadania.';
    }
  } catch (error) {
    createError.value = 'Błąd połączenia z serwerem.';
    console.error(error);
  } finally {
    isSubmitting.value = false;
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