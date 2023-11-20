import telebot
import download
import convert
import time

# Токен вашего бота
TOKEN = "6757474115:AAFAn7NiaHCCii6Ct8e2wHUACKXWNQLs0B0"

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Состояния беседы
ENTER_VIDEO_URL = 1

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    bot.send_message(message.chat.id, f"Привет, {user.first_name}! Отправьте мне ссылку на видео из Youtube.")

@bot.message_handler(func=lambda message: True)
def handle_video_url(message):
    chat_id = message.chat.id
    user_text = message.text

    if message.text == "/start":
        return

    if message.text.startswith('http'):
        try:
            audio_file_path = "audio/audo.mp3"
            bot.delete_message(chat_id, message.message_id)
            main1 = bot.send_message(chat_id, "Скачиваю")
            main2 = bot.send_message(chat_id, '🚀')
            webm_audio = download.download_audio(user_text)
            bot.delete_message(chat_id, main1.message_id)
            bot.delete_message(chat_id, main2.message_id)
            main3 = bot.send_message(chat_id, "Конвертирую")
            main4 = bot.send_message(chat_id, '🎶')
            mp3_audio = convert.convert_webm_audio_to_mp3(webm_audio, audio_file_path)
            bot.delete_message(chat_id, main3.message_id)
            bot.delete_message(chat_id, main4.message_id)
            with open(audio_file_path, 'rb') as audio:
                bot.send_audio(chat_id, audio)
        except Exception as e:
            print(e)
            bot.send_message(chat_id, "Вы отправили не ту ссылку, но мне нужна ссылка на видео из Youtube. Пожалуйста, отправьте ссылку из Youtube.")

    else:
        bot.send_message(chat_id, "Вы отправили текст, но мне нужна ссылка на видео. Пожалуйста, отправьте ссылку.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
