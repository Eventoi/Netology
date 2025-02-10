(() => {
  let wins = 0,
      losses = 0,
      kills = 0,
      misses = 0;

  const getHole = index => document.getElementById(`hole${index}`),
        resetGame = (message) => {
          alert(message);
          wins = 0;
          losses = 0;
          kills = 0;
          misses = 0;
          updateScore();
        },
        updateScore = () => {
          document.getElementById('dead').textContent = kills;
          document.getElementById('lost').textContent = misses;
          document.getElementById('wins').textContent = wins;
          document.getElementById('losses').textContent = losses;
        };

  for (let i = 1; i <= 9; i++) {
    getHole(i).onclick = () => {
      if (getHole(i).classList.contains('hole_has-mole')) {
        kills++;
        wins++;
        if (wins === 10) {
          resetGame('Поздравляем! Вы победили!');
        }
      } else {
        misses++;
        losses++;
        if (losses === 5) {
          resetGame('К сожалению, вы проиграли.');
        }
      }
      updateScore();
    };
  }
})();