<template>
  <div>
    <h2>Logowanie</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Email użytkownika:</label>
        <input id="email" v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit" :disabled="isSubmitting">Zaloguj</button>
    </form>
    <p v-if="loginError" class="error">{{ loginError }}</p>
    <p v-if="loginSuccess" class="success">{{ loginSuccess }}</p>
    <p>Nie masz jeszcze konta? <NuxtLink to="/register">Zarejestruj się</NuxtLink></p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '~/composables/useAuth';
import { useRuntimeConfig } from '#app';

const username = ref('');
const password = ref('');
const loginError = ref('');
const loginSuccess = ref('');
const isSubmitting = ref(false);
const router = useRouter();
const { login } = useAuth();
const config = useRuntimeConfig();

const handleLogin = async () => {
  try {
    loginError.value = '';
    loginSuccess.value = '';
    isSubmitting.value = true;

    const response = await fetch(`${config.public.apiBase}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: username.value, password: password.value }),
    });

    if (response.ok) {
      const data = await response.json();
      login(username.value, data.access_token);
      loginSuccess.value = 'Logowanie udane!';
      router.push('/tasks');
    } else {
      loginError.value = 'Nieprawidłowe dane logowania.';
    }
  } catch (error) {
    loginError.value = 'Błąd podczas logowania.';
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