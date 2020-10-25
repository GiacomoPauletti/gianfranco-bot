import twitter
import json

"""api = twitter.Api(consumer_key="8Y1q5KLzMgjPqyivfLCl3Y81h",
                  consumer_secret="gMM7hrk5uW32ofb4OvxqZpw1E8RiEGN0aJTWfeHYFCxiq8FfMG",
                  access_token_key="702854261705711616-nr2uorCbOVh84sKeLJB67kjNLP9MFSj",
                  access_token_secret="YeIA1X4KKNWnb4dJwwsfLNN7mO1ZHa4KcblMtkqf63y0z")
"""

"""GetUserTimeline è un metodo dell'api che permette di prendere al massimo 200 tweets per volta
   di un determianto utente

   PARAMETRI:
   		-user_id (int) e screen_name (str) servono a riconoscere l'utente da cui prendere i tweets
   				-user_id sarà l'id numerico dell'utente
   				-screen_name sarà il nome dell'utente (quello che di solito viene preceduto da @)
   				uno dei due è obbligatorio
   		-since_id serve per dire fino a che id (di un tweet e non di un utente) arriva a 
   		    selezionare i tweet (di default è l'ID più recente, ovvero l'ultimo tweet postato)
   		-max_id è l'ID da cui si parte (se il since ID è la fine questo è l'inizio')
   		-count (da 0 a 200) serve per indicare il numero di tweet da prendere in un unica richiesta
   		-exclude_replies serve a includere o meno le risposte ai tweets
   		-include_rts

   		N.B:
   		since e max sono invertiti rispetto a come si interpreterebbe solitamente: 
   			-since indica fino a quale tweet id si arriva
   			-max indica da quale tweet id si parte

"""


#first random sentence:
#RT @ElliottHulse: Hey, I'm looking forward to meet you this summer! http://t.co/50u2B32g0h
#Doitforthewristbands


class TwitterScraperBot:

	def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
		self.api = twitter.Api(consumer_key=consumer_key,
	                  consumer_secret=consumer_secret,
	                  access_token_key=access_token_key,
	                  access_token_secret=access_token_secret)



	def GetUserTweets(self,user_id, limit=False):
		"""
		WHAT DOES IT DO?
			It returns a list with all the tweets of a certain user, eventually with a limit of
			tweets taken

		PARAMETERS
			user_id: è l'ID numerico di un certo utente
			limit: è il limite di tweets che vanno raccolti dalll'utente
		"""
		if type(user_id) == str:
			user_id=int(user_id)
		tweets_list=[]
		id_list=[]
		i=0

		tll1 = 0	#tweets list length 1 / 2
		tll2 = 0

		isScanning=True

		while isScanning:
			if i >0:
				tweets = self.api.GetUserTimeline(user_id=user_id, exclude_replies=True,trim_user=False,count=200, max_id=tweets_list[-1].id)
			else:
				tweets = self.api.GetUserTimeline(user_id=user_id, exclude_replies=True,trim_user=False,count=200)
			
			for index,tweet in enumerate(tweets):
				if tweet.id in id_list:
					pass

				else:
					if not limit or len(tweets_list) < limit:
						id_list.append(tweet.id)
						tweets_list.append(tweet)
					else:
						isScanning=False
						break

			if tll1== tll2 and tll1 != 0:
				isScanning=False

			tll1 = len(tweets_list)
			tll1, tll2 = tll2, tll1

			i +=1

		return tweets_list


	def GetRandomID(self):
		from random import randint
		"""
		WHAT DOES IT DO?
			It generate a random ID which length is between 8 and 18.

		DISCLAIMER: the ID could not correspond to a user ID, in case tcall again this function
					 untiil you get a user ID
		"""

		user_id=[]
		for _ in range(randint(7,18)):
			user_id.append(str(randint(0,9)))

		return int("".join(user_id))


	def GetRandomUser(self):
		"""
		WHAT DOES IT DO?
			It calls the GetRandomID function to generate an ID and it uses this ID as a user
			ID. If it correspond to a real user ID of twitter then it returns the user class,
			otherwise it keeps generating random IDs until one of them match with a real user
			ID
		"""
		while True:
			user_id=self.GetRandomID()

			try:
				random_user=api.GetUser(user_id)
				return random_user
			except:
				continue


	def GetRandomTweet(self):
		"""
		WHAT DOES IT DO?
			It calls GetRandomUser funtion to find a random twitter user and then it calls 
			GetUserTweets to get all the tweets of the user previously found. Then one of 
			the tweets will be randomly selected
		"""
		from random import randint
		user=self.GetRandomUser()
		user_tweets=self.GetUserTweets(user_id=user.id)

		random_tweet=user_tweets[randint(0, len(user_tweets)-1)]

		return random_tweet



#DA SISTEMARE
"""
def FindWordsUsage(n_texts):
	#DISCLAIMER: this operation takes a lot of time (the complexity is 0(n))
	if type(n_texts) != int:
		n_texts=int(input('Your input is not an int, please insert it again --> '))

	words_dict = dict()
	for i in range(n_texts):
		if 22.0 <= i/n_texts <= 28.0:
			print('-----------------------------------25-----------------------------------')

		if 47.0 <= 8/n_texts <= 53.0:
			print('-----------------------------------50-----------------------------------')

		if 72.0 <= i/n_texts <= 78.0:
			print('-----------------------------------75-----------------------------------')

		words = CleanTextContent(GetRandomTweet().text, rem_stop_words=True, repl_tag="giacomopauletti", repl_link="https://www.wikipedia.org")

		for word in words:
			try:
				if word in words_dict.keys():
					words_dict[word] +=1
				else:
					words_dict[word] = 1
			except:
				pass

	return words_dict
"""

