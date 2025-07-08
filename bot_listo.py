from telethon.sync import TelegramClient  
from telethon.tl.types import Message
import asyncio
import threading
from flask import Flask

# Datos de tu sesión premium
api_id = 24448076
api_hash = '873d006b19ba8172d87585d58f40e23d'
session_name = 'premium_sender'

# Mensaje origen
grupo_origen_id = 2716599370  # Add Test
mensaje_id = 32

# Lista de grupos destino (excepto Add Test)
grupos_destino_ids = [
    2267868043,  # VENTAS_ELITE
    2374313514,  # MENDIVILIZA CHAT
    2284147408,  # DELUXE CHK
    2188331454,  # LUNA SHoP [ CHAT ]
    2400740384,  # Appfel Chat
    2686224272,  # VaultCrew Chat
    2462045873,  # DARK CHK *CHAT*
    2640258378,  # CNDY CHK [CHAT]
    2482743388,  # Yoshi Chk [Ventas]
    2626207534,  # Cloudflare Shop
    2438580408,  # UMBRLLA_CHK
    2334234976,  # Tomato Chk ( revivido )
    2335238228,  # Sudo team 🧠
    2165842343,  # LEVIATAN CHK
    2312406490   # MENDOZA CHAT
]

TIEMPO_ESPERA = 14400  # ⏱️ 4 horas = 14,400 segundos

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

        for gid in grupos_destino_ids:
            try:
                await client.send_message(gid, message=mensaje)
                print(f"✅ Mensaje enviado a {gid}")
            except Exception as e:
                print(f"❌ Error enviando a {gid}: {e}")

# === BUCLE PRINCIPAL ===
async def main():
    while True:
        print("\n🚀 Enviando mensaje...\n")
        await enviar_mensaje()

        print(f"\n⏳ Próximo envío en 4 horas...\n")
        for i in range(TIEMPO_ESPERA, 0, -1):
            horas = i // 3600
            minutos = (i % 3600) // 60
            segundos = i % 60
            tiempo_formateado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            print(f"⌛ Tiempo restante: {tiempo_formateado}", end="\r")
            await asyncio.sleep(1)

# Ejecutar el bucle
asyncio.run(main())















