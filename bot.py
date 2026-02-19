# -*- coding: utf-8 -*-
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===================== НАСТРОЙКИ =====================

BOT_TOKEN = "8586405541:AAGodQrTGk1OS3oAiMH3Ocq1hayZAYd38eU"

SPONSOR_LINKS = [
    "https://t.me/+fr8yTpBkO301MjNi",  # спонсор 1
]

FILM_CHANNEL_LINK = "https://t.me/+L445_HqqdgViNmIy"  # твой канал с фильмами

FILMS = {
     163: "Убийство священного оленя — 8435",
    164: "Враг — 5262",
    165: "Машинист — 2084",
    166: "Темнота — 9173",
    167: "Утопия — 4305",
    168: "ОА — 7629",
    169: "Черное зеркало — 2816",
    170: "Разделение — 6907",
    171: "Остатки — 5081",
    172: "Мистер Робот — 7342",
    173: "Табула Раса — 9152",
    174: "Катла — 3647",
    175: "Архив 81 — 8406",
    176: "Человек с Земли — 2471",
    177: "Фонтан — 6093",
    178: "Стокер — 8250",
    179: "Кожа, в которой я живу — 4902",
    180: "Пленники призрачной земли — 1736",
    181: "Клетка — 7024",
    182: "Личность — 5986",
    183: "Оставайся — 8115",
    184: "Другие — 3680",
    185: "Слабость — 9456",
    186: "Штормовое укрытие — 2519",
    187: "Жук — 7391",
    188: "Приглашение — 8643",
    189: "Деревня — 3208",
    190: "Дар — 5901",
    191: "Туман — 7169",
    192: "Аннигиляция — 4326",
    193: "Солнце — 8214",
    194: "Пандорум — 1648",
    195: "Европейский репорт — 9032",
    196: "Сигнал — 5487",
    197: "Вивариум — 2765",
    198: "Бесконечность — 6918",
    199: "Опоссум — 3845",
    200: "Ночной дом — 7250",

}

# =====================================================

dp = Dispatcher()


def sponsors_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    for link in SPONSOR_LINKS:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(text="📢 Подписаться на спонсора", url=link)]
        )
    kb.inline_keyboard.append(
        [InlineKeyboardButton(text="✅ Я подписался", callback_data="sub_ok")]
    )
    return kb


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Чтобы узнать название фильма 🎬\n"
        "подпишись на спонсора и нажми кнопку ниже 👇",
        reply_markup=sponsors_kb()
    )


@dp.callback_query(lambda c: c.data == "sub_ok")
async def after_sub(callback: types.CallbackQuery):
    await callback.message.answer("✅ Отлично!\n\nВведи код фильма (например: 23)")
    await callback.answer()


@dp.message()
async def handle_code(message: types.Message):
    code = message.text.strip()
    # если человек пишет "Код 23" — вытащим цифры
    code = code.replace("Код", "").replace("код", "").replace("№", "").strip()

    if code in FILMS:
        title = FILMS[code]
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🎥 Перейти в канал с фильмами", url=FILM_CHANNEL_LINK)]
        ])
        await message.answer(f"🎬 {title}\n\nЖми кнопку ниже 👇", reply_markup=kb)
    else:
        await message.answer("❌ Неверный код. Пример: 23")


async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("BOT STARTED SUCCESSFULLY")
    asyncio.run(main())

