<template>
  <div class="task-list container pt-3">
    <h1 class="text-center my-4" style="color: rgba(130, 0, 182, 0.7); text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);">Lista de Tareas</h1>

    <div class="add-task-container mb-3 d-flex">
      <input
        v-model="newTask"
        placeholder="Añadir nueva tarea"
        @keyup.enter="addTask"
        class="task-input form-control"
        style="border-radius: 20px 0 0 20px;"
      />
      <button @click="addTask" class="add-button btn btn-success" style="border-radius: 0 10px 10px 0;">Añadir</button>
    </div>

    <div class="tasks-container">
      <div v-for="task in tasks" :key="task.id" class="task-item mb-3 p-3 border rounded bg-light">
        <div class="task-content text-center">
          <p :class="{ completed: task.completed }">{{ task.todo }}</p>
          <div :class="{'status-pending': !task.completed, 'status-completed': task.completed}" class="task-status text-center">
            {{ task.completed ? 'Completada' : 'Pendiente' }}
          </div>
          <div class="task-buttons d-flex justify-content-end mt-2">
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

    <div v-if="tasks.length === 0" class="no-tasks text-center">
      <p>No hay tareas disponibles</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "TaskList",
  data() {
    return {
      tasks: [],
      newTask: '',
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await axios.get('https://dummyjson.com/todos');
        this.tasks = response.data.todos;
      } catch (error) {
        console.error('Error al cargar las tareas:', error);
      }
    },
    addTask() {
      if (this.newTask.trim() === '') return;
      const newTask = {
        id: Date.now(),
        todo: this.newTask,
        completed: false,
      };
      this.tasks.unshift(newTask);
      this.newTask = '';
    },
    toggleCompletion(taskId) {
      const task = this.tasks.find(t => t.id === taskId);
      if (task) task.completed = !task.completed;
    },
    deleteTask(taskId) {
      this.tasks = this.tasks.filter(task => task.id !== taskId);
    },
    updateTasks(tasks) {
      this.tasks = tasks;
    }
  },
  mounted() {
    this.fetchTasks();
  },
};
</script>

<style scoped>
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
