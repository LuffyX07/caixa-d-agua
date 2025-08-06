import serial
import requests
import time

porta_serial = 'COM11'
baud_rate = 9600
url_flask = 'http://localhost:5000/nivel'

try:
    ser = serial.Serial(porta_serial, baud_rate, timeout=1)
    print(f"Conectado na porta {porta_serial}")
    time.sleep(2)  # espera Arduino resetar
    ser.reset_input_buffer()  # limpa o buffer
except Exception as e:
    print(f"Erro ao abrir porta serial: {e}")
    exit(1)

while True:
    try:
        linha = ser.readline().decode('utf-8', errors='ignore').strip()
        if linha:
            print(f"Raw linha: '{linha}'")
            if linha.isdigit():
                nivel = int(linha)
                print(f"Nível lido: {nivel}")

                response = requests.post(url_flask, json={"valor": nivel})
                if response.ok:
                    print("Enviado para Flask com sucesso")
                else:
                    print(f"Erro ao enviar para Flask: {response.status_code}")
            else:
                print("Linha recebida não é número válido")
        time.sleep(1)
    except Exception as e:
        print(f"Erro no loop: {e}")
