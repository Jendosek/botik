import wikipedia, re
import telebot

wikipedia.set_lang('uk')
bot = telebot.TeleBot("6134715132:AAFhSOr25h_Um6ESixvvPi3JUSzHL9xAI4g")
def get_wiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikitext[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if (len((x.strip()))>3):
                    wikitext2 = wikitext2 + x + "."
                    return wikitext2
                return wikimas
        wikitext2 = re.sub("\([^()]*\)", '', wikitext2)
        wikitext2 = re.sub("\([^()]*\)", '', wikitext2)
        wikitext2 = re.sub("\{[\{\}]*\)", '', wikitext2)
        return wikitext2
    except Exception as e:
        return "такого немає"

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki(message.text))

bot.polling()