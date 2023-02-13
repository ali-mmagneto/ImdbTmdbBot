from PyMovieDb import IMDB
from pyrogram import Client, filters
from googletrans import Translator
import json

@Client.on_message(filters.command('start'))
async def start_mesaj(bot, message):
    await bot.send_photo(
        chat_id = message.chat.id,
        photo = "https://telegra.ph/file/8582e32294e469d699a48.jpg",
        caption = "Benim aracılığımla Tmdb ve Imdb'den veri alabilirsin iyi kullanımlar :)\n\n/tmdb >>> veriler Tmdb'den (The Movie Database)\n/imdb >>> veriler Imdb'den (İnternet Movie Database)")
