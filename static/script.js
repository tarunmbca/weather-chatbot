function sendMessage() {
  const input = document.getElementById('user-input');
  const message = input.value.trim();
  if (message === '') return;

  addMessage(message, 'user');
  input.value = '';

  fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
    .then(response => response.json())
    .then(data => addMessage(data.reply, 'bot'))
    .catch(() => addMessage('Oops! Something went wrong.', 'bot'));
}

function addMessage(text, sender) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `${sender}-msg`;
  msgDiv.textContent = text;
  document.getElementById('chat-box').appendChild(msgDiv);
  document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
}
