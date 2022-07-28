import logging
from aiogram.dispatcher.filters import Text
import sql_auto
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5108712864:AAETzTF2_VWjJktj1F2paW7bOmNFc_zbPRM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    buttons = ["բոլոր մակնիշները", "փնտրել գնով", "փնտրել մակնիշով"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.reply(f"Բարև {message.chat.full_name}\nես մեքենաներ որոնող բոտ եմ\nփնտրիր քո մեքենան իմ օգնությաբ.")
    await message.answer("ընտրեք որոնումը ", reply_markup=keyboard)
    print(message.chat.full_name)



# @dp.message_handler(commands=['help'])
# async def help(message:types.Message):
#     await message.reply("")
@dp.message_handler(Text(equals="բոլոր մակնիշները"))
async def oll_marks(message:types.message):
    marks = set(sql_auto.d.select_all_mark())
    for i in marks:
        mark = hbold(i)
        # print(mark)
        await message.answer(mark)

@dp.message_handler(Text(equals="փնտրել մակնիշով"))
async def search_type(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)\

    await message.answer("գրեք մակնիշը")


@dp.message_handler(Text(equals="փնտրել գնով"))
async def search_type(message: types.Message):

    # await bot.send_message(message.chat.id, message.text)\

    await message.answer("գրեք որ գնային սահմանում լինի մեքենան\nՕրինակ 3000 6000")




# async def serach_by_price(text):
#     search_price =
#     return search_price

def search_model(text):
    search = sql_auto.d.search_by_model(text)
    return search

@dp.message_handler()
async def search_car(message:types.message):
    search = sql_auto.d.search_by_mark(text=message.text)
    search1 = search_model(text=message.text)
    if '0' and ' ' in message.text:
        search4 = sql_auto.d.min_and_max_price(min_price=int(message.text.split()[0]), max_price=int(message.text.split()[1]))
        if len(search4) > 0:
            for j in search4:
                await message.answer(j)
        elif len(search4) == 1:
            await message.answer(search4)
    if ' ' in message.text:
        search3 = search_model(text=str(message.text).split()[1])
        if len(search3) > 1:
            for j in search3:
                await message.answer(j)
        elif len(search3) == 1:
            await message.answer(search3)
    if len(search) > 0:
        for i in search:
            await message.answer(i)
    elif len(search) == 1:
        await message.answer(search)
    if len(search1) > 0:
        for j in search1:
            await message.answer(j)
    elif len(search1) == 1:
        await message.answer(search1)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)