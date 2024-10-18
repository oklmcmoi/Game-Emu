from telethon import TelegramClient, events

# Remplacez par vos informations appropriées
api_id = '20978790'
api_hash = 'b4df337d80faa487e8bbd2d12253f515'
bot_token = '7567541541:AAH9pEbAiEfMVjNcVeC70Rmm50VKoJ3gJdE'

# Créer une instance du bot
client = TelegramClient('new_gameboy_bot_session', api_id, api_hash).start(bot_token=bot_token)

# Commande /start pour rediriger l'utilisateur vers l'émulateur en ligne
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Bienvenue ! 🎮 Cliquez ici pour accéder à l'émulateur Game Boy : [Cliquez ici](https://game-emu.vercel.app)\n"
        "Envoyez une ROM pour commencer à jouer !"
    )

# Commande /help pour fournir des instructions supplémentaires
@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond(
        "Commandes disponibles :\n"
        "/start - Pour commencer et obtenir le lien vers l'émulateur.\n"
        "/help - Pour voir les instructions.\n"
        "Envoyez une ROM Game Boy (.gb, .gbc) pour jouer directement dans l'émulateur."
    )

# Commande pour gérer l'envoi de ROMs
@client.on(events.NewMessage)
async def handle_rom(event):
    if event.message.file and (event.message.file.name.endswith('.gb') or event.message.file.name.endswith('.gbc')):
        await event.respond("ROM reçue ! ⏳ Veuillez patienter pendant l'émulation...")

        # Vous pouvez ici étendre le code pour gérer l'émulation côté serveur ou donner des instructions supplémentaires.
    elif event.message.text:
        await event.respond("Je ne comprends pas ce message 🤔. Utilisez /help pour voir ce que je peux faire.")

# Lancer le bot
client.run_until_disconnected()
