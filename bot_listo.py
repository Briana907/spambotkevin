
from telethon.sync import TelegramClient  
from telethon.tl.types import Message
import asyncio
import threading
from flask import Flask

# Datos de tu sesión premium
api_id = 24448076
api_hash = '873d006b19ba8172d87585d58f40e23d'
session_name = 'premium_sender'

# IDs del grupo y mensaje
grupo_origen_id = 2716599370
mensaje_id = 32
grupo_destino_id = 2716599370

TIEMPO_ESPERA = 120  # ⏱️ 2 minutos = 120 segundos

# === FLASK PARA RENDER ===
app = Flask('')

@app.route('/')
def home():
    return '✅ Bot activo'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Iniciar Flask en segundo plano
threading.Thread(target=run_flask).start()

# === FUNCIÓN DE ENVÍO ===
async def enviar_mensaje():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        mensaje = await client.get_messages(grupo_origen_id, ids=mensaje_id)

        if not mensaje:
            print("❌ No se encontró el mensaje con ese ID.")
            return

        await client.send_message(grupo_destino_id, message=mensaje)
        print("✅ Mensaje enviado exitosamente.")

# === BUCLE PRINCIPAL ===
async def main():
    while True:
        print(f"\n⏳ Próximo envío en 2 minutos...\n")
        for i in range(TIEMPO_ESPERA, 0, -1):
            minutos = i // 60
            segundos = i % 60
            tiempo_formateado = f"{minutos:02d}:{segundos:02d}"
            print(f"⌛ Tiempo restante: {tiempo_formateado}", end="\r")
            await asyncio.sleep(1)

        print("\n🚀 Enviando mensaje...\n")
        await enviar_mensaje()

# Ejecutar el bucle
asyncio.run(main())













