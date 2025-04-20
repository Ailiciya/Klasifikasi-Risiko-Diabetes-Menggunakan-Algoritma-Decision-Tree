document.getElementById("predictionForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const age = parseInt(document.getElementById("age").value);
    const bmi = parseFloat(document.getElementById("bmi").value);
    const glucose = parseFloat(document.getElementById("glucose").value);
    const resultText = document.getElementById("resultText");
  
    // Contoh logic decision tree sederhana
    let result = "";
  
    if (glucose > 125) {
      result = "Risiko Tinggi Diabetes";
    } else if (bmi > 30 && age > 45) {
      result = "Risiko Sedang Diabetes";
    } else {
      result = "Risiko Rendah Diabetes";
    }
  
    resultText.innerHTML = `Hasil: <strong>${result}</strong>`;
  });
  