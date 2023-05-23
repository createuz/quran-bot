from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
'Hi 😊'
bot_token = "your bot token"
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

kb1 = types.InlineKeyboardMarkup()
kb1.add(
    types.InlineKeyboardButton("Al-Fatihah", callback_data="fa"),
    types.InlineKeyboardButton("Al-Baqarah", callback_data="ba"),
    types.InlineKeyboardButton("Aali Imran", callback_data="im"),
    types.InlineKeyboardButton("An-Nisa’", callback_data="ni"),
    types.InlineKeyboardButton("Al-Ma’idah", callback_data="ma"),
    types.InlineKeyboardButton("Al-An’am", callback_data="ana"),
    types.InlineKeyboardButton("Al-A’raf", callback_data="ara"),
    types.InlineKeyboardButton("Al-Anfal", callback_data="anf"),
    types.InlineKeyboardButton("At-Taubah", callback_data="ta"),
    types.InlineKeyboardButton("Yunus", callback_data="yun"),
    types.InlineKeyboardButton("Hud", callback_data="hu"),
    types.InlineKeyboardButton("Yusuf", callback_data="yu"),
    types.InlineKeyboardButton("Ar-Ra’d", callback_data="rad"),
    types.InlineKeyboardButton("Ibrahim", callback_data="ib"),
    types.InlineKeyboardButton("Al-Hijr", callback_data="hi"),
    types.InlineKeyboardButton("An-Nahl", callback_data="nah"),
    types.InlineKeyboardButton("Al-Isra’", callback_data="is"),
    types.InlineKeyboardButton("Al-Kahf", callback_data="kaf"),
    types.InlineKeyboardButton("Maryam", callback_data="mar"),
    types.InlineKeyboardButton("Ta-Ha", callback_data="taha"),
    types.InlineKeyboardButton("Next", callback_data="nex1")
)

kb2 = types.InlineKeyboardMarkup()
kb2.add(
    types.InlineKeyboardButton("Al-Anbiya’", callback_data="anb"),
    types.InlineKeyboardButton("Al-Haj", callback_data="haj"),
    types.InlineKeyboardButton("Al-Mu’minun", callback_data="mum"),
    types.InlineKeyboardButton("An-Nur", callback_data="nur"),
    types.InlineKeyboardButton("Al-Furqan", callback_data="fur"),
    types.InlineKeyboardButton("Ash-Shu’ara’", callback_data="shu"),
    types.InlineKeyboardButton("An-Naml", callback_data="nam"),
    types.InlineKeyboardButton("Al-Qasas", callback_data="qa"),
    types.InlineKeyboardButton("Al-Ankabut", callback_data="ank"),
    types.InlineKeyboardButton("Ar-Rum", callback_data="rum"),
    types.InlineKeyboardButton("Luqman", callback_data="luq"),
    types.InlineKeyboardButton("As-Sajdah", callback_data="saj"),
    types.InlineKeyboardButton("Al-Ahzab", callback_data="ah"),
    types.InlineKeyboardButton("Saba’", callback_data="saba"),
    types.InlineKeyboardButton("Al-Fat’h", callback_data="fath"),
    types.InlineKeyboardButton("Al-Hujurat", callback_data="huj"),
    types.InlineKeyboardButton("Qaf", callback_data="qaf"),
    types.InlineKeyboardButton("Adz-Dzariyah", callback_data="zar"),
    types.InlineKeyboardButton("At-Tur", callback_data="tur"),
    types.InlineKeyboardButton("An-Najm", callback_data="naj"),
    types.InlineKeyboardButton("Al-Qamar", callback_data="qam"),
    types.InlineKeyboardButton("Ar-Rahman", callback_data="rah"),
    types.InlineKeyboardButton("Al-Waqi’ah", callback_data="waq"),
    types.InlineKeyboardButton("Al-Hadid", callback_data="had"),
    types.InlineKeyboardButton("Al-Mujadilah", callback_data="muj"),
    types.InlineKeyboardButton("Al-Hashr", callback_data="hash"),
    types.InlineKeyboardButton("Al-Mumtahanah", callback_data="mumt"),
    types.InlineKeyboardButton("Back", callback_data="bk1"),
    types.InlineKeyboardButton("Next", callback_data="nex2")
)

kb3 = types.InlineKeyboardMarkup()
kb3.add(
    types.InlineKeyboardButton("Fusilat", callback_data="fus"),
    types.InlineKeyboardButton("Ash-Shura", callback_data="shur"),
    types.InlineKeyboardButton("Az-Zukhruf", callback_data="zuk"),
    types.InlineKeyboardButton("Ad-Dukhan", callback_data="duk"),
    types.InlineKeyboardButton("Al-Jathiyah", callback_data="jat"),
    types.InlineKeyboardButton("Al-Ahqaf", callback_data="ahq"),
    types.InlineKeyboardButton("Muhammad", callback_data="mum"),
    types.InlineKeyboardButton("Al-Fat’h", callback_data="fath"),
    types.InlineKeyboardButton("Al-Hujurat", callback_data="huj"),
    types.InlineKeyboardButton("Qaf", callback_data="qaf"),
    types.InlineKeyboardButton("Adz-Dzariyah", callback_data="zar"),
    types.InlineKeyboardButton("At-Tur", callback_data="tur"),
    types.InlineKeyboardButton("An-Najm", callback_data="naj"),
    types.InlineKeyboardButton("Al-Qamar", callback_data="qam"),
    types.InlineKeyboardButton("Ar-Rahman", callback_data="rah"),
    types.InlineKeyboardButton("Al-Waqi’ah", callback_data="waq"),
    types.InlineKeyboardButton("Al-Hadid", callback_data="had"),
    types.InlineKeyboardButton("Al-Mujadilah", callback_data="muj"),
    types.InlineKeyboardButton("Al-Hashr", callback_data="hash"),
    types.InlineKeyboardButton("Al-Mumtahanah", callback_data="mumt"),
    types.InlineKeyboardButton("Back", callback_data="bk2"),
    types.InlineKeyboardButton("Next", callback_data="nex3")
)

kb4 = types.InlineKeyboardMarkup()
kb4.add(
    types.InlineKeyboardButton("As-Saf", callback_data="saf"),
    types.InlineKeyboardButton("Al-Jum’ah", callback_data="juma"),
    types.InlineKeyboardButton("Al-Munafiqun", callback_data="muna"),
    types.InlineKeyboardButton("At-Taghabun", callback_data="taga"),
    types.InlineKeyboardButton("At-Talaq", callback_data="tala"),
    types.InlineKeyboardButton("At-Tahrim", callback_data="tahr"),
    types.InlineKeyboardButton("Al-Mulk", callback_data="mul"),
    types.InlineKeyboardButton("Al-Qalam", callback_data="qal"),
    types.InlineKeyboardButton("Al-Haqqah", callback_data="haq"),
    types.InlineKeyboardButton("Al-Ma’arij", callback_data="maar"),
    types.InlineKeyboardButton("Nuh", callback_data="nuh"),
    types.InlineKeyboardButton("Al-Jinn", callback_data="jin"),
    types.InlineKeyboardButton("Al-Muzammil", callback_data="muzam"),
    types.InlineKeyboardButton("Al-Mudaththir", callback_data="muda"),
    types.InlineKeyboardButton("Al-Qiyamah", callback_data="qi"),
    types.InlineKeyboardButton("Al-Insan", callback_data="ins"),
    types.InlineKeyboardButton("Al-Mursalat", callback_data="murs"),
    types.InlineKeyboardButton("An-Naba'", callback_data="nab"),
    types.InlineKeyboardButton("An-Nazi’at", callback_data="nazi"),
    types.InlineKeyboardButton("Abasa", callback_data="aba"),
    types.InlineKeyboardButton("Back", callback_data="bk3"),
    types.InlineKeyboardButton("Next", callback_data="nex4")
)

kb5 = types.InlineKeyboardMarkup()
kb5.add(
    types.InlineKeyboardButton("At-Takwir", callback_data="tawk"),
    types.InlineKeyboardButton("Al-Infitar", callback_data="inf"),
    types.InlineKeyboardButton("Al-Mutaffifin", callback_data="muta"),
    types.InlineKeyboardButton("Al-Inshiqaq", callback_data="inshi"),
    types.InlineKeyboardButton("Al-Buruj", callback_data="bur"),
    types.InlineKeyboardButton("At-Tariq", callback_data="tari"),
    types.InlineKeyboardButton("Al-A’la", callback_data="ala"),
    types.InlineKeyboardButton("Al-Ghashiyah", callback_data="gash"),
    types.InlineKeyboardButton("Al-Fajr", callback_data="faj"),
    types.InlineKeyboardButton("Al-Balad", callback_data="bala"),
    types.InlineKeyboardButton("Ash-Shams", callback_data="sham"),
    types.InlineKeyboardButton("Al-Layl", callback_data="layl"),
    types.InlineKeyboardButton("Adh-Dhuha", callback_data="duha"),
    types.InlineKeyboardButton("Al-Inshirah", callback_data="inshir"),
    types.InlineKeyboardButton("At-Tin", callback_data="tin"),
    types.InlineKeyboardButton("Al-‘Alaq", callback_data="alaq"),
    types.InlineKeyboardButton("Al-Qadar", callback_data="qad"),
    types.InlineKeyboardButton("Al-Bayinah", callback_data="bayi"),
    types.InlineKeyboardButton("Az-Zalzalah", callback_data="zal"),
    types.InlineKeyboardButton("Al-‘Adiyah", callback_data="adi"),
    types.InlineKeyboardButton("Back", callback_data="bk4"),
    types.InlineKeyboardButton("Next", callback_data="nex5")
)

kb6 = types.InlineKeyboardMarkup()
kb6.add(
    types.InlineKeyboardButton("Al-Qari’ah", callback_data="qari"),
    types.InlineKeyboardButton("At-Takathur", callback_data="taka"),
    types.InlineKeyboardButton("Al-‘Asr", callback_data="asr"),
    types.InlineKeyboardButton("Al-Humazah", callback_data="huma"),
    types.InlineKeyboardButton("Al-Fil", callback_data="fil"),
    types.InlineKeyboardButton("Quraish", callback_data="qur"),
    types.InlineKeyboardButton("Al-Ma’un", callback_data="mau"),
    types.InlineKeyboardButton("Al-Kauthar", callback_data="kau"),
    types.InlineKeyboardButton("Al-Kafirun", callback_data="kafi"),
    types.InlineKeyboardButton("An-Nasr", callback_data="nasr"),
    types.InlineKeyboardButton("Al-Masad", callback_data="masad"),
    types.InlineKeyboardButton("Al-Ikhlas", callback_data="ik"),
    types.InlineKeyboardButton("Al-Falaq", callback_data="fala"),
    types.InlineKeyboardButton("An-Nas", callback_data="nas"),
    types.InlineKeyboardButton("Page1", callback_data="p1"),
    types.InlineKeyboardButton("Page2", callback_data="p2"),
    types.InlineKeyboardButton("Page3", callback_data="p3"),
    types.InlineKeyboardButton("Page4", callback_data="p4"),
    types.InlineKeyboardButton("Back", callback_data="bk5")
)

pages = types.InlineKeyboardMarkup()
pages.add(
    types.InlineKeyboardButton("Page1", callback_data="pg1"),
    types.InlineKeyboardButton("Page2", callback_data="pg2"),
    types.InlineKeyboardButton("Page3", callback_data="pg3"),
    types.InlineKeyboardButton("Page4", callback_data="pg4"),
    types.InlineKeyboardButton("Page5", callback_data="pg5"),
    types.InlineKeyboardButton("Page6", callback_data="pg6")
)


@dp.message_handler(commands=["start"])
async def welcome_message(message: types.Message):
    user_id = message.from_user.id
    text = "feel free to listen and download audios\n \t\t Choose Surah"
    await bot.send_message(user_id, text, reply_markup=kb1)


@dp.message_handler(content_types=["photo", "video", "text", "document", "sticker", "audio", "video_note"])
async def send_quran(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, "Assalamu Aleykum")


@dp.callback_query_handler(lambda c: c.data)
async def handle_callback_query(call: types.CallbackQuery):
    data = call.data
    if data == "pg1":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb1)
    elif data == "pg2":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
    elif data == "pg3":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb3)
    elif data == "pg4":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb4)
    elif data == "pg5":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb5)
    elif data == "pg6":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb6)
    elif data == "fa":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/4", reply_markup=pages)
    elif data == "ba":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/5", reply_markup=pages)
    elif data == "im":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/6", reply_markup=pages)
    elif data == "ni":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/7", reply_markup=pages)
    elif data == "ma":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/8", reply_markup=pages)
    elif data == "ana":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/9", reply_markup=pages)
    elif data == "ara":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/10", reply_markup=pages)
    elif data == "anf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/11", reply_markup=pages)
    elif data == "ta":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/12", reply_markup=pages)
    elif data == "yun":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/13", reply_markup=pages)
    elif data == "hu":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/14", reply_markup=pages)
    elif data == "yu":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/15", reply_markup=pages)
    elif data == "rad":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/16", reply_markup=pages)
    elif data == "ib":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/17", reply_markup=pages)
    elif data == "hi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/18", reply_markup=pages)
    elif data == "nah":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/19", reply_markup=pages)
    elif data == "is":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/20", reply_markup=pages)
    elif data == "kaf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/21", reply_markup=pages)
    elif data == "mar":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/22", reply_markup=pages)
    elif data == "taha":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/23", reply_markup=pages)
    elif data == "nex1":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)

    elif data == "anb":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/24", reply_markup=pages)
    elif data == "haj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/25", reply_markup=pages)
    elif data == "mum":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/26", reply_markup=pages)
    elif data == "nur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/27", reply_markup=pages)
    elif data == "fur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/28", reply_markup=pages)
    elif data == "shu":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/29", reply_markup=pages)
    elif data == "nam":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/30", reply_markup=pages)
    elif data == "qa":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/31", reply_markup=pages)
    elif data == "ank":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/32", reply_markup=pages)
    elif data == "rum":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/33", reply_markup=pages)
    elif data == "luq":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/34", reply_markup=pages)
    elif data == "saj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/35", reply_markup=pages)
    elif data == "ah":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/36", reply_markup=pages)
    elif data == "saba":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/37", reply_markup=pages)
    elif data == "fat":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/38", reply_markup=pages)
    elif data == "yas":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/39", reply_markup=pages)
    elif data == "saff":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/40", reply_markup=pages)
    elif data == "sad":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/41", reply_markup=pages)
    elif data == "zum":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/42", reply_markup=pages)
    elif data == "gaf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/43", reply_markup=pages)
    elif data == "bk1":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb1)
    elif data == "nex2":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb3)

    elif data == "fus":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/44", reply_markup=pages)
    elif data == "shur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/45", reply_markup=pages)
    elif data == "zuk":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/46", reply_markup=pages)
    elif data == "duk":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/47", reply_markup=pages)
    elif data == "jat":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/48", reply_markup=pages)
    elif data == "ahq":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/49", reply_markup=pages)
    elif data == "muh":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/50", reply_markup=pages)
    elif data == "fath":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/51", reply_markup=pages)
    elif data == "huj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/52", reply_markup=pages)
    elif data == "qaf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/53", reply_markup=pages)
    elif data == "zar":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/54", reply_markup=pages)
    elif data == "tur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/55", reply_markup=pages)
    elif data == "naj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/56", reply_markup=pages)
    elif data == "qam":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/57", reply_markup=pages)
    elif data == "rah":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/58", reply_markup=pages)
    elif data == "waq":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/59", reply_markup=pages)
    elif data == "had":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/60", reply_markup=pages)
    elif data == "muj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/61", reply_markup=pages)
    elif data == "hash":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/62", reply_markup=pages)
    elif data == "mumt":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/63", reply_markup=pages)
    elif data == "bk2":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
    elif data == "nex3":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb4)

    elif data == "saf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/64", reply_markup=pages)
    elif data == "juma":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/65", reply_markup=pages)
    elif data == "muna":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/66", reply_markup=pages)
    elif data == "taga":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/67", reply_markup=pages)
    elif data == "taha":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/68", reply_markup=pages)
    elif data == "tahr":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/69", reply_markup=pages)
    elif data == "mul":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/70", reply_markup=pages)
    elif data == "qal":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/71", reply_markup=pages)
    elif data == "haq":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/72", reply_markup=pages)
    elif data == "maar":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/73", reply_markup=pages)
    elif data == "nuh":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/74", reply_markup=pages)
    elif data == "jin":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/75", reply_markup=pages)
    elif data == "muzam":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/76", reply_markup=pages)
    elif data == "muda":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/77", reply_markup=pages)
    elif data == "qi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/78", reply_markup=pages)
    elif data == "ins":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/79", reply_markup=pages)
    elif data == "murs":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/80", reply_markup=pages)
    elif data == "nab":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/81", reply_markup=pages)
    elif data == "nazi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/82", reply_markup=pages)
    elif data == "aba":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/83", reply_markup=pages)
    elif data == "bk3":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb3)
    elif data == "nex4":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb5)

    elif data == "tawk":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/84", reply_markup=pages)
    elif data == "inf":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/85", reply_markup=pages)
    elif data == "muta":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/86", reply_markup=pages)
    elif data == "inshi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/87", reply_markup=pages)
    elif data == "bur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/88", reply_markup=pages)
    elif data == "tari":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/89", reply_markup=pages)
    if data == "ala":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/90", reply_markup=pages)
    elif data == "gash":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/91", reply_markup=pages)
    elif data == "faj":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/92", reply_markup=pages)
    elif data == "bala":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/93", reply_markup=pages)
    elif data == "sham":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/94", reply_markup=pages)
    elif data == "layl":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/95", reply_markup=pages)
    elif data == "duha":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/96", reply_markup=pages)
    elif data == "inshir":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/97", reply_markup=kb5)
    elif data == "tin":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/98", reply_markup=pages)
    elif data == "alaq":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/99", reply_markup=pages)
    elif data == "qad":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/100", reply_markup=pages)
    elif data == "bayi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/101", reply_markup=pages)
    elif data == "zal":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/102", reply_markup=pages)
    elif data == "adi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/103", reply_markup=pages)
    elif data == "bk4":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb4)
    elif data == "nex5":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb6)

    elif data == "qari":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/104", reply_markup=pages)
    elif data == "taka":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/105", reply_markup=pages)
    elif data == "asr":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/106", reply_markup=pages)
    elif data == "huma":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/107", reply_markup=pages)
    elif data == "fil":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/108", reply_markup=pages)
    elif data == "qur":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/109", reply_markup=pages)
    elif data == "mau":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/110", reply_markup=pages)
    elif data == "kau":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/111", reply_markup=pages)
    elif data == "kafi":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/112", reply_markup=pages)
    elif data == "nasr":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/113", reply_markup=pages)
    elif data == "masad":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/114", reply_markup=pages)
    elif data == "ik":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/115", reply_markup=pages)
    elif data == "fala":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/116", reply_markup=pages)
    elif data == "nas":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        await bot.send_audio(call.message.chat.id, "https://t.me/QarimSiddiq/117", reply_markup=pages)
    elif data == "p1":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb1)
    elif data == "p2":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
    elif data == "p3":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb3)
    elif data == "p4":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb4)
    elif data == "bk5":
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb5)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
