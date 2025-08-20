// frontend/middleware/auth.ts
export default defineNuxtRouteMiddleware((to, from) => {
  const token = localStorage.getItem('token');
  if (!token) {
    return navigateTo('/login'); // Przekierowanie na stronę logowania
  }
});