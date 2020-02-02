const socket = new WebSocket('ws://localhost:9001');

socket.send($('.current-word').innerText);

function simulateKeyPress(character) {
      socket.send(character);
}
