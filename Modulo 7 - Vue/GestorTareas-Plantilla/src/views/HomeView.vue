<template>
  <div class="home text-center">
    <h1 class="mb-4">Bienvenido a la Aplicación de Tareas con Vue</h1>
    <p class="mb-4">
      Esta aplicación te permite gestionar tus tareas de manera eficiente. Puedes añadir nuevas tareas
      manualmente o extraerlas desde una API.
    </p>
    <div class="logo-container mb-4">
      <div class="logo-hover">
        <img src="@/assets/logo.png" alt="Vue Logo" class="vue-logo img-fluid" />
      </div>
    </div>
    <section class="app-sections">
      <h2 class="text-success mb-3">Secciones de la Aplicación</h2>
      <ul class="list-unstyled">
        <li class="mb-2">
          <strong>Añadir Tarea:</strong> Permite ingresar nuevas tareas manualmente.
        </li>
        <li class="mb-2">
          <strong>Lista de Tareas:</strong> Muestra todas las tareas extraídas desde la API, permitiendo marcarlas como completadas o eliminarlas.
        </li>
        <li class="mb-2">
          <strong>Vista Combinada:</strong> Combina las funcionalidades de añadir tareas manualmente y ver las tareas de la API al mismo tiempo.
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
};
</script>

<style scoped>
.vue-logo {
  width: 150px;
  height: 150px;
  margin: 20px auto;
  transition: transform 0.3s ease;
  border-radius: 50%;
  box-shadow: 0 4px 15px rgba(130, 0, 182, 0.7);
}

.logo-container {
  display: inline-block;
}

.logo-hover:hover .vue-logo {
  transform: scale(1.1);
}

.app-sections {
  margin-top: 30px;
}

.app-sections h2 {
  color: #42b983;
}
</style>
