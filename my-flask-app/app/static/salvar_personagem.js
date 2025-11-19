// Funções utilitárias para localStorage
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

function carregarPersonagemLocal() {
  try {
    const data = localStorage.getItem('personagemData');
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('Erro ao carregar do localStorage:', error);
    return null;
  }
}

function limparPersonagemLocal() {
  try {
    localStorage.removeItem('personagemData');
    localStorage.removeItem('personagemInfo');
    console.log('Dados do personagem removidos do localStorage');
    return true;
  } catch (error) {
    console.error('Erro ao limpar localStorage:', error);
    return false;
  }
}

// Função para preencher o formulário com dados salvos (opcional)
function preencherFormulario(data) {
  try {
    if (data.raca) {
      const racaElement = document.getElementById("raca");
      if (racaElement) racaElement.value = data.raca;
    }
    
    if (data.classe) {
      const classeElement = document.getElementById("classe");
      if (classeElement) classeElement.value = data.classe;
    }
    
    if (data.atributos && Array.isArray(data.atributos)) {
      data.atributos.forEach((valor, index) => {
        const atributoElement = document.getElementById(`atributo${index}`);
        if (atributoElement) atributoElement.value = valor;
      });
    }
    
    console.log('Formulário preenchido com dados salvos');
  } catch (error) {
    console.error('Erro ao preencher formulário:', error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  // Carregar dados salvos do localStorage (opcional)
  const dadosSalvos = carregarPersonagemLocal();
  if (dadosSalvos) {
    console.log('Dados encontrados no localStorage:', dadosSalvos);
    // Opcional: preencher os campos automaticamente
    // preencherFormulario(dadosSalvos);
  }

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
        // Também podemos salvar a resposta do servidor se necessário
        localStorage.setItem('personagemInfo', result.message);
      })
      .catch((error) => {
        alert("Erro ao salvar personagem!");
      });
  };
});
