document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".btn-group.raca button").forEach((btn) => {
    btn.addEventListener("click", function () {
      document
        .querySelectorAll(".btn-group.raca button")
        .forEach((b) => b.classList.remove("selected"));
      btn.classList.add("selected");
      document.getElementById("input-raca").value = btn.value;
    });
  });

  document.querySelectorAll(".btn-group.classe button").forEach((btn) => {
    btn.addEventListener("click", function () {
      document
        .querySelectorAll(".btn-group.classe button")
        .forEach((b) => b.classList.remove("selected"));
      btn.classList.add("selected");
      document.getElementById("input-classe").value = btn.value;
    });
  });

  document
    .getElementById("form-escolha")
    .addEventListener("submit", function (e) {
      if (
        !document.getElementById("input-raca").value ||
        !document.getElementById("input-classe").value
      ) {
        alert("Selecione uma raça e uma classe!");
        e.preventDefault();
      }
    });
});
