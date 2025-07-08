from telethon.sync import TelegramClient  
from telethon.tl.types import Message
import asyncio
import threading
from flask import Flask

# === DATOS DE TU CUENTA TELEGRAM PREMIUM ===
api_id = 24448076
api_hash = '873d006b19ba8172d87585d58f40e23d'
session_name = 'premium_sender'

# === MENSAJE ORIGEN (Add Test) ===
grupo_origen_id = 2716599370
mensaje_id = 32

# === LISTA DE GRUPOS DESTINO (con nombres al lado de los IDs) ===
grupos_destino_ids = [
    -1002267868043,  # VENTAS_ELITE
    -1002374313514,  # MENDIVILIZA CHAT
    -1002284147408,  # DELUXE CHK
    -1002188331454,  # LUNA SHoP [ CHAT ]
    -1002400740384,  # Appfel Chat
    -1002686224272,  # VaultCrew Chat
    -1002462045873,  # DARK CHK *CHAT*
    -1002640258378,  # CNDY CHK [CHAT]
    -1002482743388,  # Yoshi Chk [Ventas]
    -1002626207534,  # Cloudflare Shop
    -1002438580408,  # UMBRLLA_CHK
    -1002334234976,  # Tomato Chk ( revivido )
    -1002335238228,  # Sudo team 🧠
    -1002165842343,  # LEVIATAN CHK
    -1002312406490   # MENDOZA CHAT
]

# Espera de 4 horas (en segundos)
TIEMPO_ESPERA = 14400

# === FLASK PARA MANTENER VIVO EN RENDER ===
app = Flask('')

@app.route('/')
def home():
    return '✅ Bot activo'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask).start()

# === FUNCIÓN PARA ENVIAR MENSAJE ===
async def enviar_mensaje():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        mensaje = await client.get_messages(grupo_origen_id, ids=mensaje_id)
        if not mensaje:
            print("❌ No se encontró el mensaje con ese ID.")
            return

        for gid in grupos_destino_ids:
            try:
                entidad = await client.get_entity(gid)
                nombre_grupo = entidad.title
                await client.send_message(gid, message=mensaje)
                print(f"✅ Mensaje enviado a {nombre_grupo} (ID: {gid})")
            except Exception as e:
                print(f"❌ Error enviando a {gid}: {e}")

# === BUCLE PRINCIPAL: ESPERA 4 HORAS ANTES DEL PRIMER ENVÍO ===
async def main():
    while True:
        print(f"\n⏳ Próximo envío en 4 horas...\n")
        for i in range(TIEMPO_ESPERA, 0, -1):
            horas = i // 3600
            minutos = (i % 3600) // 60
            segundos = i % 60
            tiempo_formateado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            print(f"⌛ Tiempo restante: {tiempo_formateado}", end="\r")
            await asyncio.sleep(1)

        print("\n🚀 Enviando mensaje...\n")
        await enviar_mensaje()

# === EJECUTAR BOT ===
asyncio.run(main())






















