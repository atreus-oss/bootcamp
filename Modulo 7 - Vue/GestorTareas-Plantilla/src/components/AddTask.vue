<template>
  <div class="container pt-5">
    <h1 class="text-center mb-4" style="color: rgba(130, 0, 182, 0.7); text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);">Añadir Tarea</h1>
    <div class="add-task-container mb-4">
      <div class="input-group">
        <input
          v-model="newTask"
          placeholder="Añadir nueva tarea"
          @keyup.enter="addTask"
          class="form-control task-input"
          style="border-radius: 20px 0 0 20px;"
        />
        <button @click="addTask" class="btn btn-success add-button" style="border-radius: 0 10px 10px 0;">Añadir Tarea</button>
      </div>
    </div>
    <div class="recent-tasks">
      <h2>Tareas Añadidas:</h2>
      <div v-if="tasks.length === 0" class="no-tasks text-center">
        <p>No hay tareas añadidas</p>
      </div>
      <div v-for="task in tasks" :key="task.id" class="recent-task-box mb-3 p-3 border rounded bg-light">
        <div class="task-content text-center">
          <p :class="{ completed: task.completed }">{{ task.todo }}</p>
        </div>
        <div class="task-status-container text-center mt-2">
          <div :class="task.completed ? 'status-completed' : 'status-pending'" class="task-status">
            {{ task.completed ? 'Completada' : 'Pendiente' }}
          </div>
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
</template>

<script>
export default {
  name: "AddTask",
  data() {
    return {
      newTask: "",
      tasks: [],
    };
  },
  methods: {
    addTask() {
      if (this.newTask.trim() === "") return;
      const newTask = {
        todo: this.newTask,
        completed: false,
        id: Date.now(),
      };
      this.tasks.push(newTask);
      this.$emit('taskAdded', newTask);
      this.newTask = "";
    },
    toggleCompletion(taskId) {
      const task = this.tasks.find(t => t.id === taskId);
      if (task) {
        task.completed = !task.completed;
      }
    },
    deleteTask(taskId) {
      this.tasks = this.tasks.filter(task => task.id !== taskId);
    },
  },
};
</script>

<style scoped>
.task-input {
  border-radius: 20px 0 0 20px;
  font-size: 14px;
}

.add-button {
  border-radius: 0 4px 4px 0;
  font-size: 14px;
  width: 120px;
}

.recent-task-box {
  background-color: #f9f9f9;
}

.task-status {
  padding: 5px;
  margin-top: 5px;
  border-radius: 4px;
  display: inline-block;
}

.status-completed {
  background-color: lightgreen;
  color: black;
}

.status-pending {
  background-color: gold;
  color: black;
}

.completed {
  text-decoration: line-through;
  color: #888;
}

.no-tasks {
  margin-top: 10px;
  color: #777;
}
</style>
