from typing import Final


# TODO: link to instagram
START: Final[str] = r"""<b>🌟 Приветствую!</b>
Меня зовут Ильнара <a href="https://www.instagram.com/ilnara_cc">instagram</a>, и вот уже более 6 лет я изучаю юг Турции.
Я знаю самые крутые места и локации и хочу поделиться этими знаниями с вами через гайд.
🌟 Гайд будет хорошим помощником для тех, кто едет на Средиземноморское побережье Турции самостоятельно, а особенно для тех, кто едет впервые.
"""  # fmt: skip

MENU: Final[str] = r"""<b>Вы можете выбрать один из двух вариантов:</b>
✔️ Гайд по Кашу: подходит тем, кто планирует отдыхать только в Каше.
✔️ Полный гайд по югу Турции: Каш, Фетхие, Олюдениз, Даламан, Дальян + бонусные локации: Мармарис, Датча, Бодрум, Алачаты.

✔️Формат гайда: закрытый телеграм-канал, доступ к которому остаётся у вас навсегда.
🗺 К каждому гайду для вашего удобства прилагается карта со всеми локациями в google maps.
"""  # fmt: skip

KAS: Final[str] = r"""✔️Общая информация
✔️Схема города и карта с отметками
✔️Как бронировать жильё и список проверенных отелей
✔️Аренда авто, трансферы, обществ.транспорт
✔️29 кафе и ресторанов
✔️20 пляжей
✔️Чем заняться в Каше: развлечения
✔️Прямые контакты подрядчиков, осуществляющих прогулки на кораблях, джип-туры, дайвинг и др.
✔️Маршруты Ликийской тропы

И много другой полезной информации, которая поможет тебе в отпуске!
"""  # fmt: skip

PHOTO_PROBLEM: Final[str] = "Problem with send PHOTO"

SOUTH: Final[str] = r"""✔️Аренда жилья и авто в Турции
✔️Обмен валюты, сотовая связь
✔️Подробная информация о городах: Каш, Фетхие, Олюдениз, Даламан, Дальян
➕Бонус: Мармарис, Бодрум, Датча, Алачаты
✔️78 проверенных кафе и ресторанов
✔️59 пляжей: от самых известных до секретных
✔️11 смотровых площадок
✔️Водопады, каньоны
✔️Амфитеатры
✔️Активности: джип-сафари, дайвинг, параглайдинг, морские прогулки - прямые контакты всех подрядчиков, которые оказывают эти услуги.
✔️Маршруты Ликийской тропы

И много другой полезной информации, которая поможет тебе в отпуске!
"""  # fmt: skip

PRICE_KAS: Final[str] = """<b>Стоимость гайда по Кашу:</b>
20$/ 1900₽/ 550 лир
"""  # fmt: skip

PRICE_SOUTH: Final[str] = """<b>Стоимость гайда по югу Турции:</b>
40$/ 3900₽/ 1100 лир
"""  # fmt: skip

PAYMENTS_INFO: Final[str] = """{price}
<b>Оплату можно произвести:</b>
💰 для РФ: в рублях переводом на карту Тинькофф.
💰 для Турции: в лирах по IBAN на карту Vakif.
💰 для Казахстана: в лирах на турецкую карту международным переводом с Каспия.
💰 USDT на крипто-кошелёк.
💰 Для оплаты из других стран, нажмите кнопку «Другое»
"""  # fmt: skip

PAID_INFO: Final[str] = """
Проверка оплаты занимает до ~30 мин (в ночные часы до ~6 часов).
<b>После оплаты нажмите «оплачено».</b>
"""  # fmt: skip

CRYPTO_INFO: Final[str] = r"""<b>Сеть: TRON (TRC20)</b>
Адрес: <strong>`TCKxbUijJqVJnB8cscxpakymJFGtsPiYkw`</strong>

«чтобы скопировать адрес,просто нажмите на него»
"""  # fmt: skip

PAYMENTS_CRYPTO_INFO: Final[str] = CRYPTO_INFO + PAID_INFO

RUS_INFO: Final[str] = r"""<b>Вы выбрали перевод на карту Тинькофф.</b>
Получатель: Валиахметова Ильнара Рифатовна
Перевод по номеру телефона: <strong>`+79638579694`</strong>

«чтобы скопировать номер, просто нажмите на него»
"""  # fmt: skip

PAYMENTS_RUS_INFO: Final[str] = RUS_INFO + PAID_INFO


TRY_INFO: Final[str] = """<b>Вы выбрали перевод на турецкую карту.</b>
Получатель: <strong>`ILNARA VALIAKHMETOVA`</strong>
IBAN: <strong>TR`72 0001 5001 5800 7318 7774 62`</strong>

«чтобы скопировать имя и IBAN, просто нажмите на него»
"""  # fmt: skip

PAYMENTS_TRY_INFO: Final[str] = f"{TRY_INFO}{PAID_INFO}"

OTHER_INFO: Final[str] = """<b>Свяжитесь со мной @ilnara174</b>
"""  # fmt: skip

PAYMENTS_OTHER_INFO: Final[str] = f"{OTHER_INFO}"

PAYMENTS_U_MONEY_INFO: Final[str] = r"""<b>👋 PAYMENTS_U_MONEY_INFO! 🌍✨</b>

<b>! 🤝🌟</b>

🏄‍♂️🎲 . 🌊🍽️

<b>Here's how it works:</b>
1️⃣ .
2️⃣ .
3️⃣ .
4️⃣ . 🗣️🤩

🌐✈️ ! 🌟🌍🍴

🤖🙌 <b>Happy adventuring!</b>
"""  # fmt: skip

PAID: Final[str] = r"""<b>Благодарю за покупку!</b>
Проверка оплаты займёт до ~30 мин (в ночные часы до ~6 часов).

Пришлите скриншот/квитанцию сюда.
"""  # fmt: skip

ADMIN: Final[str] = r"""<b>👋 Пользователь нажал кнопку заплатить! 🌍✨</b>
"""  # fmt: skip

# START_OLD = r"""<b>👋 Funny Body text! 🌍✨</b>

# <b>! 🤝🌟</b>

# 🏄‍♂️🎲 . 🌊🍽️

# <b>Here's how it works:</b>
# 1️⃣ .
# 2️⃣ .
# 3️⃣ .
# 4️⃣ . 🗣️🤩

# 🌐✈️ ! 🌟🌍🍴

# 🤖🙌 <b>Happy adventuring!</b>
# """

# SPECIAL_OFFER = r"""<b>👋 SPECIAL_OFFER! 🌍✨</b>

# <b>! 🤝🌟</b>

# 🏄‍♂️🎲 . 🌊🍽️

# <b>Here's how it works:</b>
# 1️⃣ .
# 2️⃣ .
# 3️⃣ .
# 4️⃣ . 🗣️🤩

# 🌐✈️ ! 🌟🌍🍴

# 🤖🙌 <b>Happy adventuring!</b>
# """

# CATALOG = r"""<b>👋 CATALOG text! 🌍✨</b>

# <b>! 🤝🌟</b>

# 🏄‍♂️🎲 . 🌊🍽️

# <b>Here's how it works:</b>
# 1️⃣ .
# 2️⃣ .
# 3️⃣ .
# 4️⃣ . 🗣️🤩

# 🌐✈️ ! 🌟🌍🍴

# 🤖🙌 <b>Happy adventuring!</b>
# """

# DELIVERY_INFO = r"""<b>👋 DELIVERY_INFO! 🌍✨</b>

# <b>! 🤝🌟</b>

# 🏄‍♂️🎲 . 🌊🍽️

# <b>Here's how it works:</b>
# 1️⃣ .
# 2️⃣
# 3️⃣
# 4️⃣ . 🗣️🤩

# 🌐✈️
# 🤖🙌 <b>Happy adventuring!</b>
# """
