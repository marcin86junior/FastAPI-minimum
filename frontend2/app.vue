<template>
  <div>
    <header>
      <h1>Moja aplikacja</h1>
      <nav>
        <button @click="goTo('/')">Strona główna</button>
        <button @click="goTo('/login')">Logowanie</button>
        <button @click="goTo('/tasks')">Lista zadań</button>
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
const goTo = (path) => {
  window.location.href = path;
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
main {
  min-height: calc(100vh - 200px);
  padding: 1rem;
}
</style>