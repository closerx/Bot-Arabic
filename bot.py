import  requests
import telebot


def text_to_voice(text):
	if True:
		url=f"https://freetts.com/Home/PlayAudio?Language=ar-XA&Voice=Zeina_Female&TextMessage={text}&id=Zeina&type=1"
		get =requests.get(url)
		myid=get.json()["id"]
		
		url_don="https://freetts.com/audio/"
		down=requests.get(url_don+myid)
	
		with open("sound.mp3","wb") as f:
			f.write(down.content)
			return True
	else:
		return False
		


token="add token here"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def hello(msg):
	bot.reply_to(msg,
	text="""
	أهلا وسهلا بكم
	انا بوت اقوم بتحويل النص الي صوت باللغة العربية
	
	""")

@bot.message_handler(commands=["config"])
def config(msg):
	bot.reply_to(msg,text="قم بوضع النص المراد تحويلة")
	
	bot.register_next_step_handler(msg,fuc)
	
def fuc(msg):
	text=msg.text
	bot.reply_to(msg,text="انتظر...")
	
	if text_to_voice(text) ==True:
		bot.send_audio(chat_id=msg.chat.id,
		audio=open("sound.mp3","rb"))
	else:
		bot.reply_to(msg,text="حاول موة اخرى")
	
bot.polling()
