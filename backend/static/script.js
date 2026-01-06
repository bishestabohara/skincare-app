console.log("LOADED FROM backend/static/script.js");

function sendAnswer(answer) {
  fetch("/serum", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ answer })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("message").innerText = data.message;
    })
    .catch(err => console.error(err));
}
