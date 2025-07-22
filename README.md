# 💧 Monitoramento de Caixa d'Água com Arduino

Este projeto utiliza um **Arduino Uno**, um **sensor ultrassônico HC-SR04** e uma **bomba d'água** para medir o nível de água em uma caixa e exibir essas informações em uma **página web simples**, gerada por um programa em Python no computador.

## 📋 Funcionalidades

- Medição contínua do nível de água com sensor HC-SR04.
- Controle automático de bomba d’água com relé.
- Interface web para visualização do nível da água.
- Atualização dos dados em tempo real via serial + Python.
- Sistema simples, sem necessidade de Wi-Fi ou módulos extras.

## 🧰 Componentes Utilizados

- 1x Arduino Uno
- 1x Sensor Ultrassônico HC-SR04
- 1x Módulo Relé 5V
- 1x Bomba d'água (5V–12V)
- Jumpers, protoboard e fonte de alimentação
- 1x Computador para rodar o servidor Python local
- 1x Cabo USB (conecta Arduino ao computador)

## ⚙️ Como Funciona

1. O sensor HC-SR04 mede a distância do topo da caixa até a superfície da água.
2. O Arduino calcula o nível em porcentagem baseado na altura total da caixa.
3. Se o nível estiver abaixo de um limite mínimo, o Arduino aciona a bomba via relé.
4. O Arduino envia os dados via porta serial para o computador.
5. Um script Python coleta esses dados e exibe em uma página web simples.

## 🌐 Interface Web

A página web mostra:

- Porcentagem do nível de água
- Estado da bomba (ligada/desligada)
- Atualização automática a cada 5 segundos

## 🔧 Instalação e Configuração

### 1. Montagem do Circuito

- Conecte o sensor HC-SR04 nas portas digitais do Arduino.
- Conecte o módulo relé ao pino de controle e à bomba d’água.
- Verifique o esquema elétrico em `docs/diagrama.png`.

### 2. Upload do Código no Arduino

- Use o **Arduino IDE** para carregar o código localizado em `src/main.ino`.

### 3. Executar o Servidor Web

- Instale Python 3 no computador.
- Instale a biblioteca Flask:
  ```bash
  pip install flask pyserial
