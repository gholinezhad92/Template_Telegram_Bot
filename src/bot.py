import json
import os

import telebot
from loguru import logger

from src.utils.io import write_json
from src.constants import keyboards



class Bot:
	"""
	Telegram Bot to connect to Strangers to talk randomly
	"""
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
		self.echo_all = self.bot.message_handler(
			func=lambda message: True
		)(self.echo_all)
		#pper Lines are instead of decorated @!!!
		#  we can not place self.bot after @
		#  because self just means in a function not outside it!

	def run(self):
		logger.info("Bot is Running...")
		self.bot.infinity_polling()

	def echo_all(self, message):
		# write_json(message.json, 'message.json')
		self.bot.send_message(
			message.chat.id, message.text,
			reply_markup=leyboards.main)

if __name__ == '__main__':
	logger.info('Bot Started')
	bot = Bot()
	bot.run()
