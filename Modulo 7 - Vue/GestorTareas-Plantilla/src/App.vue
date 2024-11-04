<template>
  <div id="app">
    <header class="d-flex justify-content-between align-items-center p-3 bg-purple text-white w-100">
      <router-link to="/" class="d-flex align-items-center text-white text-decoration-none ms-3"> <!-- Añadido margen a la izquierda -->
        <div class="logo d-flex align-items-center">
          <img src="@/assets/logo.png" alt="Logo de V Gestor de Tareas" class="vue-logo me-2" />
          <span class="logo-text">Gestor de Tareas</span>
        </div>
      </router-link>
      <nav class="d-flex gap-3 me-3">
        <router-link to="/addtask" class="nav-link text-white">
          <i class="fas fa-plus"></i> Añadir Tarea
        </router-link>
        <router-link to="/loadTasks" class="nav-link text-white">
          <i class="fas fa-list"></i> Lista de Tareas
        </router-link>
        <router-link to="/tasks" class="nav-link text-white">
          <i class="fas fa-th"></i> Vista Combinada
        </router-link>
      </nav>
    </header>

    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #333;
  text-align: center;
  background-color: #f4f4f9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.bg-purple {
  background-color: #8200b6; /* Color del fondo del header */
}

.vue-logo {
  width: 50px;
  height: auto;
}

nav a:hover {
  color: #e225c9;
}

nav a.router-link-exact-active {
  color: #ff00dd;
}
</style>
