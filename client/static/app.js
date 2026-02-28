
const statusEl = document.getElementById("status");
const msgEl = document.getElementById("msg");
const btn = document.getElementById("btn");

btn.disabled = true;

const ws = new WebSocket(window.WS_URL);

ws.onopen = () => {
  statusEl.textContent = "Соединение WebSocket установлено";
  btn.disabled = false; 
};

ws.onmessage = (event) => {
  msgEl.textContent = "";          
  msgEl.textContent = event.data;  
};

ws.onclose = () => {
  statusEl.textContent = "Соединение закрыто";
  btn.disabled = true;
};

ws.onerror = () => {
  statusEl.textContent = "Ошибка WebSocket";
  btn.disabled = true;
};

btn.addEventListener("click", () => {
  const unique = "uniq-" + (crypto.randomUUID ? crypto.randomUUID() : Date.now());
  ws.send(unique);
});