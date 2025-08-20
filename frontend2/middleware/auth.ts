export default defineNuxtRouteMiddleware((to, from) => {
  // Sprawdź, czy użytkownik jest zalogowany (czy jest token)
  if (process.client) {
    const token = localStorage.getItem('access_token');
    if (!token) {
      // Jeśli nie ma tokenu, przekieruj na stronę logowania
      return navigateTo('/login');
    }
  }
});