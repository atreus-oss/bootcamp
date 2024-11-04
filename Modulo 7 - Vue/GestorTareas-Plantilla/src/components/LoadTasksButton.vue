<template>
  <div class="load-tasks-button text-center">
    <button @click="fetchTasks" class="btn btn-success d-flex justify-content-center align-items-center mx-auto">
      <i class="fas fa-sync-alt me-2"></i> Cargar Tareas
    </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoadTasksButton',
  methods: {
    async fetchTasks() {
      try {
        const response = await axios.get('https://dummyjson.com/todos');
        const tasks = response.data.todos;
        this.$emit('tasksLoaded', tasks);
      } catch (error) {
        console.error('Error al cargar las tareas:', error);
      }
    }
  }
};
</script>

<style scoped>
.load-tasks-button .btn {
  border-radius: 4px 4px 4px 4px;
}
.load-tasks-button .btn:hover {
  background-color: #169159;
}
</style>
