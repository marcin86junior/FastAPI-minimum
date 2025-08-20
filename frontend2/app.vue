<template>
  <div>
    <header>
      <h1>SuperTask</h1>
        <nav>
          <button @click="goTo('/')">Strona główna</button>
          <button v-if="!isAuthenticated" @click="goTo('/login')">Logowanie</button>
          <button v-if="!isAuthenticated" @click="goTo('/register')">Rejestracja</button>
          <button v-if="isAuthenticated" @click="goTo('/tasks')">Lista zadań</button>

          <div v-if="isAuthenticated" class="user-info">
            <span>Zalogowany: {{ username }}</span>
            <button @click="handleLogout">Wyloguj</button>
          </div>
        </nav>
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
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '~/composables/useAuth';

const router = useRouter();
const { isAuthenticated, username, checkAuth, logout } = useAuth();

const goTo = (path) => {
  router.push(path);
};

const handleLogout = () => {
  logout();
  router.push('/');
};

onMounted(() => {
  checkAuth();
});
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
nav {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}
nav button {
  margin: 0 5px;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
nav button:hover {
  background-color: #0056b3;
}
.user-info {
  margin-left: 15px;
  display: flex;
  align-items: center;
}
.user-info span {
  margin-right: 10px;
}
main {
  min-height: calc(100vh - 200px);
  padding: 1rem;
}
</style>