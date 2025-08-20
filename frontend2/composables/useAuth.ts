// frontend/composables/useAuth.ts
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const user = ref(null);
const token = ref(localStorage.getItem('token') || '');

export function useAuth() {
  const router = useRouter();

  const login = async (credentials: { username: string; password: string }) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
      });
      if (response.ok) {
        const data = await response.json();
        token.value = data.access_token;
        localStorage.setItem('token', token.value);
        router.push('/');
      } else {
        throw new Error('Błąd logowania');
      }
    } catch (error) {
      console.error(error);
    }
  };

  const logout = () => {
    token.value = '';
    localStorage.removeItem('token');
    router.push('/login');
  };

  return { user, token, login, logout };
}