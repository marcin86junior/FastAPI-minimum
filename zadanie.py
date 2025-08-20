Dzień dobry,

w nawiązaniu do rozmowy przesyłam zadanie do wykonania.


# Zadanie rekrutacyjne - Full Stack Developer
Stwórz aplikację do zarządzania listą zadań z autentykacją użytkowników.

### Backend (FastAPI)
- Autoryzacja za pomoca JWT (rejestracja, logowanie)
- CRUD operacje na zadaniach
- Endpoints: `/auth/register`, `/auth/login`, `/tasks` (GET, POST, PUT, DELETE)
- Middleware do weryfikacji tokenów

### Frontend (Nuxt3)
Wymagane elementy do sprawdzenia:

**Composables:**
- `useAuth()` - zarządzanie autentykacją
- `useTasks()` - zarządzanie zadaniami

**Middleware:**
- `auth.ts` - ochrona tras
- `guest.ts` - przekierowanie zalogowanych

**Komponenty z watch/onMounted:**
- Lista zadań z automatycznym odświeżaniem
- Formularz z walidacją w czasie rzeczywistym
- Licznik zadań

**Strony:**
- `/` - lista zadań (chroniona)
- `/login` - logowanie
- `/register` - rejestracja

## Ważne - Problem do rozwiązania

Przeanalizuj poniższy kod i odpowiedz na pytanie: **Dlaczego ten kod spowoduje hydration error i jak można to naprawić?**

```vue
<template>
 <div class="task-counter">
   <p>Aktualny czas: {{ currentTime }}</p>
   <p>Zadania: {{ completedTasks }}/{{ totalTasks }}</p>
   <p>Jesteś online od: {{ onlineTime }}</p>
 </div>
</template>

<script setup>
const currentTime = ref(new Date().toLocaleTimeString())
const onlineTime = ref(new Date().toLocaleTimeString())

onMounted(() => {
 setInterval(() => {
   currentTime.value = new Date().toLocaleTimeString()
 }, 1000)
})

const { tasks } = useTasks()
const completedTasks = computed(() => tasks.value.filter(t => t.completed).length)
const totalTasks = computed(() => tasks.value.length)
</script>
```

## Do oddania

1. **Kod źródłowy** (link do repozytorium GitHub)
2. **README.md** z instrukcjami uruchomienia
3. **Odpowiedź na pytanie o hydration error** (w README lub osobnym pliku)

