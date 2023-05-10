import telebot
from PIL import Image, ImageDraw

bot = telebot.TeleBot('6020132205:AAHO0YzVwrTp8F8V6dc11Oc3m2PiJjunyXs');


@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as image:
        image.write(downloaded_file)
        foto = Image.open("image.jpg")
        draw = ImageDraw.Draw(foto)
        width = foto.size[0]
        height = foto.size[1]
        pix = foto.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        bot.send_photo(message.chat.id, foto)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Я не понимаю текст. Лучше отправьте картинку.")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправьте картинку.")

bot.polling(none_stop=True, interval=0)