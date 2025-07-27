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
            labels: ['08:00', '10:00', '12:00', '14:00', '16:00'],
            datasets: [{
                    label: 'Nível da Água (%)',
                    data: [70, 60, 55, 65, 60],
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