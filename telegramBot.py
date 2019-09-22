import pyowm
import telebot

owm = pyowm.OWM('225059cc35fda5fdf9b159d482d76f5d', language="ru")  # You MUST provide a valid API key
bot = telebot.TeleBot("847402338:AAEbqZBREs-IkE8tNFmsKpXCD-AIy2Cs2KY")

@bot.message_handler(content_types=["text"])
def send_echo(message):
    observation = owm.weather_at_place( 'Kharkiv, UA' )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    wind = w.get_wind()["speed"] 
    humidity = w.get_humidity()

    if wind < 0.15:
        storm = "Безветренно"
    elif 0.15 < wind < 2.7:
        storm = "Тихий ветер"
    elif 2.7 < wind < 3.6:
        storm = "Легкий ветер"
    elif 3.6 < wind < 7.2:
        storm = "Слабый ветер"
    elif 7.2 < wind < 8.9:
        storm = "Умеренный ветер"
    elif 8.9 < wind < 12.5:
        storm = "Свежий ветер"
    elif 12.5 < wind < 14.5:
        storm = "Сильный ветер"
    elif 14.5 < wind < 20:
        storm = "Умеренная Буря"
    elif 20 < wind < 22:
        storm = "Буря"
    elif 22 < wind < 28:
        storm = "Сильная Буря!"
    elif 28 < wind < 31:
        storm = "Шторм!!"
    elif 31 < wind < 37:
        storm = "Сильный Шторм!!!"
    else:
        storm  = "!!! - Ураган - !!!"
 
    answer = 'В Харькове сейчас:  ' + str(w.get_detailed_status()) + "\n" 
    answer += 'Температура ' + str(temp) + "C" + "\n\n"
    answer += "Влажность воздуха - " + str(humidity)  + "%" + "\n"
    answer += 'Ветер ' + str(wind) + "м/с   "  + storm

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop = True)