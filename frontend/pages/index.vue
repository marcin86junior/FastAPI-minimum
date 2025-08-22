<template>
  <div>
    <h1>Panel zadań</h1>
    <TaskCounter />
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['auth']
});
</script>