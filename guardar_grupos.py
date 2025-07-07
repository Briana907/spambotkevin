from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat

# Reemplaza por los tuyos
api_id = 20298803
api_hash = '0946f8cf922b14896130366ca76684b7'
session = 'premium_session'

with TelegramClient(session, api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    with open("grupos_guardados.txt", "w", encoding="utf-8") as archivo:
        archivo.write("📋 Lista de grupos disponibles:\n\n")
        for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, (Channel, Chat)) and getattr(entity, 'megagroup', False):
                nombre = entity.title
                chat_id = entity.id
                archivo.write(f"📌 {nombre} | chat_id: {chat_id}\n")
                print(f"📌 {nombre} | chat_id: {chat_id}")
