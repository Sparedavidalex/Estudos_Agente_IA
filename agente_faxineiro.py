import os
import shutil
import requests
import psutil
import threading
import time
from flask import Flask

app = Flask(__name__)

# === CONFIGURAÇÕES ===
TELEGRAM_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_id_aqui



LIMITE_TEMP = 80  
LIMITE_RAM = 70   # Seu novo gatilho
LIMITE_SSD = 85   

def obter_dados():
    t, u, l = shutil.disk_usage("/")
    p_ssd = (u / t) * 100
    p_ram = psutil.virtual_memory().percent
    try:
        temp_dict = psutil.sensors_temperatures()
        p_temp = temp_dict['coretemp'][0].current if 'coretemp' in temp_dict else 0
    except:
        p_temp = 0
    return p_ssd, p_ram, p_temp

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": ID_TELEGRAM, "text": mensagem}
    try:
        r = requests.post(url, json=payload, timeout=10)
        print(f"📡 [TELEGRAM] Status {r.status_code}: Mensagem enviada.")
    except Exception as e:
        print(f"❌ [ERRO] Falha ao enviar: {e}")

def vigilancia_automatica():
    print("🕵️ Agente Vigilante Davidflix: ATIVO")
    while True:
        p_ssd, p_ram, p_temp = obter_dados()
        avisos = []
        if p_temp > LIMITE_TEMP: avisos.append(f"🔥 CALOR: {p_temp}°C")
        if p_ram > LIMITE_RAM: avisos.append(f"🧠 RAM: {p_ram}%")
        if p_ssd > LIMITE_SSD: avisos.append(f"💾 SSD: {p_ssd:.1f}%")

        if avisos:
            enviar_telegram("⚠️ ALERTA AUTOMÁTICO ⚠️\n" + "\n".join(avisos))
        
        time.sleep(300) # Verifica a cada 10 segundos para o seu teste

@app.route('/')
def home():
    p_ssd, p_ram, p_temp = obter_dados()
    return f"<h1>Dashboard Davidflix</h1><p>SSD: {p_ssd:.1f}% | RAM: {p_ram}% | Temp: {p_temp}°C</p>"

if __name__ == "__main__":
    # Inicia a vigilância
    t = threading.Thread(target=vigilancia_automatica)
    t.daemon = True
    t.start()
    
    # Inicia o servidor
    app.run(host='0.0.0.0', port=5000)
