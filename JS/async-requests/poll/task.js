async function loadPollData() {
  try {
    const response = await fetch('https://students.netoservices.ru/nestjs-backend/poll');
    const data = await response.json();

    const pollTitle = document.getElementById('poll__title');
    pollTitle.textContent = data.data.title;

    const pollAnswers = document.getElementById('poll__answers');
    
    pollAnswers.innerHTML = '';

    data.data.answers.forEach(answer => {
      const button = document.createElement('button');
      button.classList.add('poll__answer');
      button.textContent = answer;

      button.addEventListener('click', () => {
        alert('Спасибо, ваш голос засчитан!');
      });

      pollAnswers.appendChild(button);
    });
  } catch (error) {
    console.error('Ошибка загрузки опроса:', error);
  }
}

window.onload = loadPollData;
