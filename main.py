from __future__ import unicode_literals
import os
import youtube_dl
import telebot
import glob



class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


bot = telebot.TeleBot('1116367497:AAEwFdWbQmBfkPCJFaUo_27igRjW8cGgjzg')

@bot.message_handler(commands=['start'])
def wel(message):
    bot.reply_to(message, 'enter link!')


@bot.message_handler(content_types=['text'])
def auu(message):
    bot.send_message(message.chat.id, 'Please wait...')
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'{message.text}'])
    audio_name = glob.glob('*.mp3')[0]
    audio = open(audio_name, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_audio')
    bot.send_audio(message.from_user.id, audio)
    audio.close()
    os.remove(audio_name)


bot.polling(none_stop=True)

