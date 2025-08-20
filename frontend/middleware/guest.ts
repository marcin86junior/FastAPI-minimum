// frontend/middleware/guest.ts
export default defineNuxtRouteMiddleware((to, from) => {
  const token = localStorage.getItem('token');
  if (token) {
    return navigateTo('/'); // Przekierowanie na stronę główną
  }
});