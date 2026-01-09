console.log("LOADED FROM backend/static/script.js");

// STEP 1: SERUM
function sendSerum(answer) {
  fetch("/serum", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("message").innerText = data.message;

      // Only move forward if serum is done
      if (answer === "y") {
        showMoisturizerStep();
      }
    })
    .catch(err => console.error(err));
}

// UI transition to STEP 2
function showMoisturizerStep() {
  document.getElementById("step").innerText = "Step 2: Moisturizer";
  document.getElementById("message").innerText =
    "Did you apply moisturizer?";

  document.getElementById("yesBtn").onclick = () => sendMoisturizer("y");
  document.getElementById("noBtn").onclick = () => sendMoisturizer("n");
}

// STEP 2: MOISTURIZER
function sendMoisturizer(answer) {
  fetch("/moisturizer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("message").innerText = data.message;
    })
    .catch(err => console.error(err));
}
