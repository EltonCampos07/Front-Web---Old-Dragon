
function salvarPersonagemLocal(data) {
  try {
    localStorage.setItem('personagemData', JSON.stringify(data));
    console.log('Dados salvos no localStorage:', data);
    return true;
  } catch (error) {
    console.error('Erro ao salvar no localStorage:', error);
    return false;
  }
}

document.addEventListener("DOMContentLoaded", function () {

  const btn = document.getElementById("btn-salvar");
  if (!btn) return;

  btn.onclick = function () {
    const data = {
      raca: document.getElementById("raca").value,
      classe: document.getElementById("classe").value,
      atributos: [
        document.getElementById("atributo0").value,
        document.getElementById("atributo1").value,
        document.getElementById("atributo2").value,
        document.getElementById("atributo3").value,
        document.getElementById("atributo4").value,
        document.getElementById("atributo5").value,
      ],
    };

    // Salvar dados no localStorage usando função utilitária
    const salvouLocal = salvarPersonagemLocal(data);
    
    if (!salvouLocal) {
      alert("Aviso: Não foi possível salvar os dados localmente, mas continuaremos com o envio ao servidor.");
    }

    fetch("/salvar_personagem", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        alert(result.message);
      })
      .catch((error) => {
        alert("Erro ao salvar personagem!");
      });
  };
});
