
import telebot
from telebot import types
import os

# Ton token de bot Telegram ici
bot_token = '7567541541:AAH9pEbAiEfMVjNcVeC70Rmm50VKoJ3gJdE'
bot = telebot.TeleBot(bot_token)

# Chemin du dossier où les ROMs seront sauvegardées
roms_dir = "webretro-master/assets/roms/"

# Commande start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue ! Envoie-moi une ROM de jeu Game Boy pour commencer !")

# Commande pour gérer l'envoi d'une ROM
@bot.message_handler(content_types=['document'])
def handle_rom(message):
    try:
        # Récupérer le fichier
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Sauvegarder la ROM dans le dossier
        rom_name = message.document.file_name
        with open(os.path.join(roms_dir, rom_name), 'wb') as rom_file:
            rom_file.write(downloaded_file)
        
        # Générer le lien pour l'émulateur
        rom_url = f"https://ton-site.netlify.app/assets/roms/{rom_name}"
        bot.reply_to(message, f"ROM uploadée avec succès ! Tu peux jouer en cliquant ici : {rom_url}")

    except Exception as e:
        bot.reply_to(message, "Une erreur est survenue lors du traitement de la ROM.")
        print(e)

bot.polling()
