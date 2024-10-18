from telethon import TelegramClient, events
import os
import subprocess
import time
import pyautogui  # Utilisé pour prendre une capture d'écran

# Remplacez par vos informations appropriées
api_id = '20978790'  # Votre API ID Telegram
api_hash = 'b4df337d80faa487e8bbd2d12253f515'  # Votre API Hash Telegram
bot_token = '7567541541:AAH9pEbAiEfMVjNcVeC70Rmm50VKoJ3gJdE'  # Votre token de bot

# Créer une instance du bot
client = TelegramClient('new_gameboy_bot_session', api_id, api_hash).start(bot_token=bot_token)

# Commande /start pour accueillir l'utilisateur
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Bienvenue sur GameBoy Emulator Bot ! 🎮\n"
        "Envoyez une ROM Game Boy (.gb ou .gbc) pour commencer à jouer. Utilisez /help pour plus d'informations."
    )

# Commande /help pour expliquer les fonctionnalités du bot, y compris où trouver des ROMs
@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond(
        "/start - Pour démarrer le bot.\n"
        "/help - Pour voir cette aide.\n"
        "Envoyez une ROM Game Boy (.gb ou .gbc) pour jouer.\n\n"
        "Vous pouvez trouver des ROMs Game Boy et Game Boy Advance compatibles gratuitement sur :\n"
        "- [Vimm's Lair](https://vimm.net/?p=vault)\n\n"
        "Veuillez vérifier les lois sur la propriété intellectuelle dans votre pays avant de télécharger des ROMs."
    )

# Gérer l'envoi d'une ROM
@client.on(events.NewMessage)
async def handle_rom(event):
    if event.message.file and (event.message.file.name.endswith('.gb') or event.message.file.name.endswith('.gbc')):
        await event.respond("ROM reçue ! ⏳ Veuillez patienter pendant l'émulation...")

        try:
            # Téléchargez la ROM envoyée
            rom_path = await event.message.download_media()

            # Lancer RetroArch avec le cœur Gambatte pour émuler la ROM
            subprocess.Popen([
                "C:/RetroArch-Win64/retroarch.exe", "-L", "C:/RetroArch-Win64/cores/gambatte_libretro.dll", rom_path
            ])

            # Attendre quelques secondes pour laisser le jeu démarrer
            time.sleep(10)  # Attendre 10 secondes (vous pouvez ajuster selon la vitesse de démarrage)

            # Prendre une capture d'écran du bureau
            screenshot_path = "screenshot.png"
            pyautogui.screenshot(screenshot_path)

            # Envoyer la capture d'écran à l'utilisateur
            if os.path.exists(screenshot_path):
                await client.send_file(event.chat_id, screenshot_path)

                # Supprimer les fichiers temporaires
                os.remove(rom_path)
                os.remove(screenshot_path)
            else:
                await event.respond("Échec de l'émulation : la capture d'écran n'a pas été générée.")
        except Exception as e:
            await event.respond(f"Une erreur s'est produite lors de l'émulation : {e}")
    elif event.message.text:
        await event.respond("Je ne comprends pas ce message 🤔. Utilisez /help pour voir ce que je peux faire.")

# Lancer le bot
client.run_until_disconnected()
