"use strict";

const firstNumber = +document.querySelector("#a").textContent;
const secondNumber = +document.querySelector("#b").textContent;
const operator = document.querySelector("#operator");
const userResult = document.querySelector(".user-input");
const score = document.querySelector(".score-text");
const resultBox = document.querySelector(".result");
const checkBtn = document.querySelector(".check");
const resetBtn = document.querySelector(".reset");

window.addEventListener("load", function () {
  score.textContent = localStorage.getItem("score") ?? 0;
});

function solveEquation() {
  let result;
  switch (operator.textContent) {
    case "+":
      result = firstNumber + secondNumber;
      break;
    case "-":
      result = firstNumber - secondNumber;
      break;
    case "*":
      result = firstNumber * secondNumber;
      break;
    case "/":
      result = firstNumber / secondNumber;
      break;
    default:
      alert("Unexpected error occured");
      break;
  }
  return result;
}

checkBtn.addEventListener("click", function (e) {
  e.preventDefault();
  if (userResult.value.trim() === "") {
    alert("Enter the result you calculated");
    return;
  }
  if (isNaN(+userResult.value)) {
    alert("Enter valid number");
    return;
  }
  const result = solveEquation();
  resultBox.textContent = "";
  if (+userResult.value === result) {
    resultBox.insertAdjacentHTML(
      "beforeend",
      '<div class="correct">Správne!</div>'
    );
    score.textContent = +score.textContent + 1;
    localStorage.setItem("score", score.textContent);
  } else {
    resultBox.insertAdjacentHTML(
      "beforeend",
      '<div class="wrong">Nesprávne!</div>'
    );
  }
});

userResult.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    checkBtn.click();
  }
});

resetBtn.addEventListener("click", function (e) {
  localStorage.removeItem("score");
  score.textContent = 0;
});
