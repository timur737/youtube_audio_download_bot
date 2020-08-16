from __future__ import unicode_literals
import os
import youtube_dl
import telebot
import glob



bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def wel(message):
    bot.reply_to(message, 'enter link!')


@bot.message_handler(content_types=['text'])
def auu(message):
    bot.send_message(message.chat.id, 'Please wait...')
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{message.text}'])
        audio_name = glob.glob('*.mp3')[0]
        audio = open(audio_name, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        os.remove(audio_name)
    except Exception:
        bot.send_message(message.chat.id, 'Error please enter correct URL')


bot.polling(none_stop=True)

