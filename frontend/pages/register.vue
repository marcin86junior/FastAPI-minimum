<template>
  <div>
    <h2>Rejestracja</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input id="username" v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input id="email" v-model="email" type="email" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit" :disabled="isSubmitting">Zarejestruj się</button>
    </form>
    <p v-if="registerError" class="error">{{ registerError }}</p>
    <p v-if="registerSuccess" class="success">{{ registerSuccess }}</p>
    <p>Masz już konto? <NuxtLink to="/login">Zaloguj się</NuxtLink></p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useRuntimeConfig } from '#app';

const username = ref('');
const email = ref('');
const password = ref('');
const registerError = ref('');
const registerSuccess = ref('');
const isSubmitting = ref(false);
const router = useRouter();
const config = useRuntimeConfig();

const handleRegister = async () => {
  try {
    registerError.value = '';
    registerSuccess.value = '';
    isSubmitting.value = true;

    const response = await fetch(`${config.public.apiBase}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value
      }),
    });

    const data = await response.json();

    if (response.ok) {
      registerSuccess.value = 'Rejestracja udana! Możesz się teraz zalogować.';
      // Przekierowanie po 2 sekundach
      setTimeout(() => {
        router.push('/login');
      }, 2000);
    } else {
      registerError.value = data.detail || 'Błąd podczas rejestracji.';
    }
  } catch (error) {
    registerError.value = 'Błąd połączenia z serwerem.';
    console.error(error);
  } finally {
    isSubmitting.value = false;
  }
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

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  margin-top: 10px;
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