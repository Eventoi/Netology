(() => {
  let wins = 0,
      losses = 0;

  const getHole = index => document.getElementById(`hole${index}`),
        resetGame = (message) => {
          alert(message);
          wins = 0;
          losses = 0;
          updateScore();
        },
        updateScore = () => {
          document.getElementById('wins').textContent = wins;
          document.getElementById('losses').textContent = losses;
        };

  for (let i = 1; i <= 9; i++) {
    getHole(i).onclick = () => {
      if (getHole(i).classList.contains('hole_has-mole')) {
        wins++;
        if (wins === 10) {
          resetGame('Поздравляем! Вы победили!');
        }
      } else {
        losses++;
        if (losses === 5) {
          resetGame('К сожалению, вы проиграли.');
        }
      }
      updateScore();
    };
  }
})();