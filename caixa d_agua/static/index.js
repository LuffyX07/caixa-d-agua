const btnLigar = document.querySelector('.ligar');
const btnDesligar = document.querySelector('.desligar');
const status = document.querySelector('.status');
const barraverde = document.querySelector('.barra-verde');

btnLigar.addEventListener('click', () => {
      status.textContent = 'LIGADO';
      barraverde.style.background = "#2abb0dff"
      status.classList.remove('desligado');
      status.classList.add('ligado');
});

btnDesligar.addEventListener('click', () => {
      status.textContent = 'DESLIGADO';
      barraverde.style.background = "#bb0d0d"
      status.classList.remove('ligado');
      status.classList.add('desligado');
});

const ctx = document.getElementById('graficoHistorico').getContext('2d');

const grafico = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [], // vai popular depois
    datasets: [{
      label: 'Nível da Água (%)',
      data: [],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 2,
      tension: 0.4,
      fill: true,
      pointBackgroundColor: 'blue'
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        max: 100
      }
    }
  }
});

async function atualizarGrafico() {
  try {
    const response = await fetch('/historico');
    const dados = await response.json();

    // Inverter para ordem cronológica (do mais antigo para o mais novo)
    dados.reverse();

    // Extrair labels e valores
    const labels = dados.map(item => {
      // Formata timestamp para HH:MM (assumindo formato ISO)
      const date = new Date(item.timestamp);
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    });

    const valores = dados.map(item => parseInt(item.valor));

    // Atualiza dados no gráfico
    grafico.data.labels = labels;
    grafico.data.datasets[0].data = valores;
    grafico.update();

  } catch (error) {
    console.error('Erro ao atualizar gráfico:', error);
  }
}

// Atualiza gráfico ao carregar a página
atualizarGrafico();

// Opcional: atualiza gráfico a cada 30 segundos
setInterval(atualizarGrafico, 30000);

async function enviarComando(acao) {
      console.log("Enviando comando:", acao); // <-- VERIFICA se isso aparece
    
      const resposta = await fetch("/comando", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ acao })
      });
    
      const data = await resposta.json();
    
      if (data.acao) {
        document.querySelector(".status").innerText = data.acao.toUpperCase();
      } else if (data.erro) {
        document.querySelector(".status").innerText = "ERRO";
        console.error("Erro:", data.erro);
      }
    }