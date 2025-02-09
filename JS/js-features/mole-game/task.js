let score = 0;
let defeats = 0;
let moleVisible = false;
let moleHidden = true;

function getHole(index) {
  return document.getElementById('hole' + index);
}

function showMole() {
  if (!moleHidden) return;

  for (let i = 1; i <= 9; i++) {
    getHole(i).classList.remove('hole_has-mole');
  }

  const randomIndex = Math.floor(Math.random() * 9) + 1;
  const moleHole = getHole(randomIndex);
  moleHole.classList.add('hole_has-mole');
  
  moleVisible = true;
  moleHidden = false;

  setTimeout(() => {
    moleHole.classList.remove('hole_has-mole');
    moleVisible = false;
    moleHidden = true;

    if (moleHidden) {
      showMole();
    }
  }, 1000);
}

function resetGame() {
  score = 0;
  defeats = 0;
  alert("Игра началась! Для победы: убить 10 кротов. 5 поражений для окончания игры");
  startGame();
}

function onHoleClick(event) {
  if (event.target.classList.contains('hole_has-mole')) {
    score++;
    alert("Вы убили крота! Текущий счёт: " + score);
  } else {
    defeats++;
    alert("Мимо! Не попали " + defeats + " раз(-а)");
  }

  if (score >= 10) {
    alert("Поздравляем, вы победили! Ваш счёт: " + score);
    resetGame();
  } else if (defeats >= 5) {
    alert("Вы проиграли :( Ваш счёт: " + score);
    resetGame();
  }
}

function startGame() {
  for (let i = 1; i <= 9; i++) {
    getHole(i).addEventListener('click', onHoleClick);
  }
  
  showMole();
}

startGame();