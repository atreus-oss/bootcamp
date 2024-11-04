<template>
  <div class="task-list container pt-4">
    <h1 class="text-center my-4" style="color: rgba(130, 0, 182, 0.7); text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);">Lista de Tareas</h1>
    <LoadTasksButton @tasksLoaded="updateTasks" class="mb-3" />

    <div class="tasks-container">
      <div v-for="task in tasks" :key="task.id" class="task-item mb-3 p-3 border rounded bg-light">
        <div class="task-content text-center">
          <p :class="{ completed: task.completed }">
            {{ task.todo }}
          </p>
          <div :class="{'status-pending': !task.completed, 'status-completed': task.completed}" class="task-status text-center">
            {{ task.completed ? 'Completada' : 'Pendiente' }}
          </div>
          <div class="d-flex justify-content-between align-items-center">
            <div class="task-buttons ms-auto">
              <button @click="toggleCompletion(task.id)" class="btn btn-outline-primary me-2">
                <i class="fas fa-check"></i> Completar
              </button>
              <button @click="deleteTask(task.id)" class="btn btn-outline-danger">
                <i class="fas fa-trash"></i> Eliminar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="tasks.length === 0" class="no-tasks text-center">
      <p>No hay tareas disponibles</p>
    </div>
  </div>
</template>

<script>
import LoadTasksButton from './LoadTasksButton.vue';

export default {
  name: "TaskList",
  components: {
    LoadTasksButton
  },
  data() {
    return {
      tasks: [] // Estado local para las tareas
    };
  },
  methods: {
    updateTasks(tasks) {
      this.tasks = tasks; // Actualiza las tareas con las cargadas
    },
    toggleCompletion(taskId) {
      const task = this.tasks.find(t => t.id === taskId);
      if (task) {
        task.completed = !task.completed; // Cambia el estado de completado
      }
    },
    deleteTask(taskId) {
      this.tasks = this.tasks.filter(task => task.id !== taskId); // Elimina la tarea
    },
  }
};
</script>

<style scoped>
.icon-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0 10px;
  font-size: 20px;
}

.icon-button:hover {
  opacity: 0.7;
}

/* Estilo para tareas completadas */
.completed {
  text-decoration: line-through;
  color: #888;
}

/* Estilos para el estado de la tarea */
.task-status {
  padding: 5px;
  margin-top: 5px;
  border-radius: 4px;
  display: inline-block;
}

.status-pending {
  background-color: gold;
  color: black;
}

.status-completed {
  background-color: lightgreen;
  color: black;
}
</style>
