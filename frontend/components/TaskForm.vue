<template>
  <div class="task-form">
    <h2>Dodaj nowe zadanie</h2>
    <form @submit.prevent="submitTask">
      <div class="form-group">
        <label for="title">Tytuł:</label>
        <input
          type="text"
          id="title"
          v-model="taskData.title"
          @input="validateTitle"
        />
        <p v-if="errors.title" class="error">{{ errors.title }}</p>
      </div>

      <div class="form-group">
        <label for="description">Opis:</label>
        <textarea
          id="description"
          v-model="taskData.description"
          @input="validateDescription"
        ></textarea>
        <p v-if="errors.description" class="error">{{ errors.description }}</p>
      </div>

      <button type="submit" :disabled="!isFormValid">Dodaj zadanie</button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useTasks } from '~/composables/useTasks';

const { addTask } = useTasks();

const taskData = ref({
  title: '',
  description: '',
  completed: false
});

const errors = ref({
  title: '',
  description: ''
});

const validateTitle = () => {
  if (!taskData.value.title) {
    errors.value.title = 'Tytuł jest wymagany';
  } else if (taskData.value.title.length < 3) {
    errors.value.title = 'Tytuł musi mieć co najmniej 3 znaki';
  } else {
    errors.value.title = '';
  }
};

const validateDescription = () => {
  if (taskData.value.description.length > 200) {
    errors.value.description = 'Opis nie może przekraczać 200 znaków';
  } else {
    errors.value.description = '';
  }
};

// Walidacja w czasie rzeczywistym
watch(() => taskData.value.title, validateTitle);
watch(() => taskData.value.description, validateDescription);

const isFormValid = computed(() => {
  return taskData.value.title.length >= 3 &&
         taskData.value.description.length <= 200 &&
         !errors.value.title &&
         !errors.value.description;
});

const submitTask = async () => {
  if (isFormValid.value) {
    await addTask(taskData.value);
    taskData.value = {
      title: '',
      description: '',
      completed: false
    };
  }
};
</script>

<style scoped>
.task-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

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
  border: 1px solid #ddd;
  border-radius: 3px;
}

.error {
  color: red;
  font-size: 14px;
  margin-top: 5px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style>