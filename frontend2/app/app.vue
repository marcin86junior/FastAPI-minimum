<template>
  <div>
    <header>
      <h1>Moja aplikacja</h1>
      <button v-if="!isLoggedIn" @click="goToLogin">Zaloguj</button>
      <button v-else @click="handleLogout">Wyloguj</button>
      <button @click="goToTasks">Lista zadań</button>
    </header>
    <main>
      <NuxtPage />
    </main>
    <footer>
      <p>&copy; 2023 Moja aplikacja</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isLoggedIn = ref(false);

const goToLogin = () => {
  router.push('/login');
};

const handleLogout = () => {
  localStorage.removeItem('access_token');
  isLoggedIn.value = false;
};

const goToTasks = () => {
  router.push('/tasks');
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
header, footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem;
}
main {
  min-height: calc(100vh - 200px);
  padding: 1rem;
}
button {
  margin: 0 5px;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>