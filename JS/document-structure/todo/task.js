document.addEventListener('DOMContentLoaded', function() {
  const taskInput = document.getElementById('task__input');
  const tasksList = document.getElementById('tasks__list');

  function addTask(taskText) {
    const task = document.createElement('div');
    task.classList.add('task');

    const taskTitle = document.createElement('div');
    taskTitle.classList.add('task__title');
    taskTitle.textContent = taskText;

    const taskRemove = document.createElement('a');
    taskRemove.href = '#';
    taskRemove.classList.add('task__remove');
    taskRemove.textContent = '×';

    taskRemove.addEventListener('click', function(event) {
      event.preventDefault();
      task.remove();
    });

    task.appendChild(taskTitle);
    task.appendChild(taskRemove);

    tasksList.appendChild(task);
  }

  taskInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && taskInput.value.trim() !== '') {
      addTask(taskInput.value.trim());
      taskInput.value = '';
    }
  });

  document.getElementById('tasks__add').addEventListener('click', function(event) {
    event.preventDefault();
    if (taskInput.value.trim() !== '') {
      addTask(taskInput.value.trim());
      taskInput.value = '';
    }
  });
});
