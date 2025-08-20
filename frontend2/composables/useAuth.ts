// composables/useAuth.js
import { ref, readonly } from 'vue';

const isAuthenticated = ref(false);
const username = ref('');

export function useAuth() {
  const checkAuth = () => {
    const token = localStorage.getItem('access_token');
    isAuthenticated.value = !!token;
  };

  const login = (user, token) => {
    localStorage.setItem('access_token', token);
    username.value = user;
    isAuthenticated.value = true;
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    username.value = '';
    isAuthenticated.value = false;
  };

  return {
    isAuthenticated: readonly(isAuthenticated),
    username: readonly(username),
    checkAuth,
    login,
    logout
  };
}