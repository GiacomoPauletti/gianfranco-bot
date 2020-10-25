from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from threading import Thread
from TwitterScraper import TwitterScraperBot
from random import randint

TOKEN = "1360292155:AAHujQoJ_bYR8NTwZNf-R20WEXFNZGcDoic"

start_description= None
def start(update, *context):
	"""prints this message OwO"""
	global functions
	global x
	reply_message = ["Hey welcome to Gianfranco Bot, here is a list of commands that you can use:"]

	#append to the reply the description of each function
	for function in functions:
		to_append=function.upper()
		try:
			exec(f"global start_description\nstart_description={function}.__doc__")
			to_append += f": {start_description}"
		finally:
			reply_message.append(to_append)

	reply_message = "\n".join(reply_message)
	update.message.reply_text(f"{reply_message}")


def text(update, context):
	"""chat with the bot but he will act like you"""
	print('Answering...')
	user_message = ' '.join([word for index, word in enumerate(update.message.text.split()) if index != 0])
	update.message.reply_text(f'{user_message}')


tsb = TwitterScraperBot(consumer_key="8Y1q5KLzMgjPqyivfLCl3Y81h",
                  consumer_secret="gMM7hrk5uW32ofb4OvxqZpw1E8RiEGN0aJTWfeHYFCxiq8FfMG",
                  access_token_key="702854261705711616-nr2uorCbOVh84sKeLJB67kjNLP9MFSj",
                  access_token_secret="YeIA1X4KKNWnb4dJwwsfLNN7mO1ZHa4KcblMtkqf63y0z")
tsb_random_tweets = []



def cit(update, *context):
	"""return a random tweet from one of @alessandroagazz tweets"""
	global tsb_random_tweets
	if not tsb_random_tweets:
		tsb_random_tweets = [tweet.text for tweet in tsb.GetUserTweets(938162457780121600)]

	update.message.reply_text(str(tsb_random_tweets[randint(0,len(tsb_random_tweets))]))

def update_cit(update, *context):
	"""updates speak command such that there are also newer @alessandroagazz tweets"""
	tsb_random_tweets= [tweet.text for tweet in tsb.GetUserTweets(938162457780121600)]




def stop(update, *context):
	"""shut down the bot"""
	global tsb_random_tweets
	Thread(target=shutdown, args=(update,)).start()


#list of function above this line (used by the start function)
functions = dir()
functions = [function for function in functions[dir().index('__spec__')+1:] if function not in ("start_description", "functions", "TOKEN", "tsb", "tsb_random_tweets", "randint")]


def shutdown(update):
	update.message.reply_text("Gianfranco is getting shutted down :(")
	upd.stop()
	upd.is_idle = False

def main():
	global upd
	upd = Updater(TOKEN, use_context=True)
	disp=upd.dispatcher


	#aggiunge comandi che l'utente può utilizzare
	disp.add_handler(CommandHandler("start", start))
	disp.add_handler(CommandHandler("text", text))
	disp.add_handler(CommandHandler("stop", stop))
	disp.add_handler(CommandHandler("cit", cit))
	disp.add_handler(CommandHandler("update_cit", update_cit))

	#prende le risposte dall'utente
	upd.start_polling()

	#la linea sotto serve per bloccare il bot finchè non riceve un altro comando
	upd.idle()


if __name__ == '__main__':
	main()