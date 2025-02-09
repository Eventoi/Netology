let timeRemaining = 10; // Начальное время в секундах
const timerElement = document.getElementById('timer'); // Получаем элемент для отображения времени

// Обновление времени
function updateTimer() {
  let hours = Math.floor(timeRemaining / 3600);
  let minutes = Math.floor((timeRemaining % 3600) / 60);
  let seconds = timeRemaining % 60;

  // Обновление текста таймера
  timerElement.textContent = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  if (timeRemaining > 0) {
    timeRemaining--;
  } else {
    alert("Вы победили в конкурсе!");

    // Загрузка файла
    startFileDownload();

    // Останавливаем таймер, чтобы не было лишних вызовов
    clearInterval(interval);
  }
}

// Загрузка файла
function startFileDownload() {
  const link = document.createElement('a');
  link.href = 'https://resf.ru/about/documentation/103/';
  link.download = '';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Запуск таймера каждую секунду
let interval = setInterval(updateTimer, 1000);
