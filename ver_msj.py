from telethon.sync import TelegramClient
import asyncio

# Datos de tu sesión
api_id = 24448076
api_hash = '873d006b19ba8172d87585d58f40e23d'
session_name = 'premium_sender'

# Grupo del cual quieres ver mensajes (puedes usar el ID o username)
grupo_id = -1002716599370  # Ejemplo: "Add Test"

async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        mensajes = await client.get_messages(grupo_id, limit=20)  # Cambia el número si quieres más

        for m in mensajes:
            print(f"\n🆔 ID: {m.id}")
            print(f"📩 Contenido:\n{m.message}")

asyncio.run(main())
