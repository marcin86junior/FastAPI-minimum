<template>
  <div>
    <h2>Logowanie</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Email użytkownika:</label>
        <input id="username" v-model="username" type="text" required />
      </div>
      <div>
        <label for="password">Hasło:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit">Zaloguj</button>
    </form>
    <p v-if="loginError" class="error">{{ loginError }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '~/composables/useAuth';

const username = ref('');
const password = ref('');
const loginError = ref('');
const router = useRouter();
const { login } = useAuth();

const handleLogin = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: username.value, password: password.value }),
    });

    if (response.ok) {
      const data = await response.json();
      login(username.value, data.access_token);
      loginError.value = '';
      router.push('/tasks');
    } else {
      loginError.value = 'Nieprawidłowe dane logowania.';
    }
  } catch (error) {
    loginError.value = 'Błąd podczas logowania.';
  }
};
</script>

<style>
.error {
  color: red;
  margin-top: 1rem;
}
</style>