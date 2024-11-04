import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AddTask from '../components/AddTask.vue';
import CombinedView from '../components/CombinedView.vue';
import TaskList from '@/components/TaskList.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/loadTasks',
    name: 'LoadTasks',
    component: TaskList
  },
  {
    path: '/addtask',
    name: 'AddTask',
    component: AddTask
  },
  {
    path: '/tasks',
    name: 'CombinedView',
    component: CombinedView
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;