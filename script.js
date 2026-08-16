const music = document.getElementById('bgMusic');
const musicToggle = document.getElementById('musicToggle');

musicToggle.addEventListener('click', () => {
  if (music.paused) {
    music.volume = 0.5;
    music.play();
    musicToggle.textContent = '🔊';
    musicToggle.classList.add('playing');
  } else {
    music.pause();
    musicToggle.textContent = '🔈';
    musicToggle.classList.remove('playing');
  }
});

/*const form = document.getElementById('runForm');
const input = document.getElementById('userInput');*/
const btn = document.getElementById('runBtn');
const bubble = document.getElementById('outputBubble');
const outputText = document.getElementById('outputText');
const mascot = document.getElementById('mascot');


btn.addEventListener('click', async () => {
  /*e.preventDefault();*/

  btn.disabled = true;
  mascot.textContent = '🐸💭';

  try {
    const res = await fetch('/run', {method: 'POST'});
    const data = await res.json();

    outputText.textContent = data.result;
    bubble.hidden = false;
    // retrigger the pop-in animation each time
    bubble.style.animation = 'none';
    bubble.offsetHeight; // force reflow
    bubble.style.animation = null;

    mascot.textContent = '🐸✨';
  } catch (err) {
    outputText.textContent = "Oops, something went sideways. Try again? 🫧";
    bubble.hidden = false;
    mascot.textContent = '🐸';
  } finally {
    btn.disabled = false;
  }
});
