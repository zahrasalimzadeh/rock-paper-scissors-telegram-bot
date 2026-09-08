# ✂️ 📄 🗿 ROCK PAPER SCISSORS TELEGRAM BOT

# ✂️ 📄 🗿 ربات سنگ کاغذ قیچی تلگرام

A Telegram bot that lets users play Rock-Paper-Scissors against the bot, built with Python and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

ربات تلگرامی برای بازی سنگ کاغذ قیچی در مقابل ربات، ساخته‌شده با پایتون و کتابخانه‌ی pyTelegramBotAPI.

---

## 📌 Features

- ✅ Play Rock-Paper-Scissors against the bot with inline buttons
- ✅ Custom illustrated icons for Rock, Paper, and Scissors
- ✅ Random bot move on every round
- ✅ Sends photo results for both the user's and bot's choice
- ✅ Dedicated win image shown for the round's winner
- ✅ Instant rematch — a new keyboard appears after every round
- ✅ Secure token handling via `.env` / environment variables

## 📌 امکانات

- ✅ بازی سنگ کاغذ قیچی در مقابل ربات با دکمه‌های اینلاین
- ✅ آیکون‌های اختصاصی برای سنگ، کاغذ و قیچی
- ✅ انتخاب تصادفی ربات در هر دور
- ✅ ارسال عکس انتخاب کاربر و انتخاب ربات
- ✅ نمایش تصویر اختصاصی برای برنده‌ی هر دور
- ✅ امکان بازی دوباره بلافاصله بعد از هر دور
- ✅ مدیریت امن توکن با فایل `.env`

> ℹ️ این نسخه از ربات دکمه‌ی دعوت دوستان داخل کد ندارد. تصویر «جمع دوستان.jpg» به‌عنوان عکس پروفایل ربات در تلگرام استفاده شده است.

---

## 🎮 Game Rules

Each round, the user picks Rock, Paper, or Scissors and the bot picks randomly. The result is decided as:

- 🗿 Rock beats ✂️ Scissors
- 📄 Paper beats 🗿 Rock
- ✂️ Scissors beats 📄 Paper
- Same choice → it's a tie 🤝

## 🎮 قوانین بازی

در هر دور کاربر یکی از گزینه‌های سنگ، کاغذ یا قیچی را انتخاب می‌کند و ربات به‌صورت تصادفی انتخاب می‌کند:

- 🗿 سنگ، ✂️ قیچی را می‌برد
- 📄 کاغذ، 🗿 سنگ را می‌برد
- ✂️ قیچی، 📄 کاغذ را می‌برد
- انتخاب یکسان → نتیجه مساوی است 🤝

---

## 🛠 Technologies Used

- Python
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) (`telebot`)
- python-dotenv (environment variable management)

## 🛠 تکنولوژی‌های استفاده‌شده

- Python
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) (`telebot`)
- python-dotenv (مدیریت متغیرهای محیطی)

---

## 🔐 Bot Token Setup

Create a `.env` file in the project root with your Telegram bot token:

```
TOKEN=your_telegram_bot_token_here
```

The bot reads it in `bot.py` via:

```python
load_dotenv()
TOKEN = os.getenv("TOKEN")
```

> ⚠️ Make sure `.env` and `token.txt` are listed in `.gitignore` so your token stays private.

## 🔐 تنظیم توکن ربات

یک فایل `.env` در ریشه‌ی پروژه بسازید و توکن ربات تلگرام خود را در آن قرار دهید:

```
TOKEN=your_telegram_bot_token_here
```

> ⚠️ مطمئن شوید فایل‌های `.env` و `token.txt` در `.gitignore` قرار دارند تا توکن شما فاش نشود. هرگز این فایل‌ها را در گیت‌هاب منتشر نکنید.

---

## 📂 Project Structure

```
telegram_bot/
│
├── bot.py               # Main bot logic
├── requirements.txt      # Project dependencies
├── .env                  # Bot token (not committed to git)
├── .gitignore
│
├── سنگ.png               # Rock icon
├── کاغذ.png              # Paper icon
├── قیچی.png              # Scissors icon
├── برد_سنگ.png            # Rock-wins result image
├── برد_کاغذ.png           # Paper-wins result image
├── برد_قیچی.png           # Scissors-wins result image
└── جمع دوستان.jpg         # Used as the bot's Telegram profile photo
```

## 📂 ساختار پروژه

```
telegram_bot/
│
├── bot.py               # منطق اصلی ربات
├── requirements.txt      # وابستگی‌های پروژه
├── .env                  # توکن ربات (در گیت کامیت نمی‌شود)
├── .gitignore
│
├── سنگ.png               # آیکون سنگ
├── کاغذ.png              # آیکون کاغذ
├── قیچی.png              # آیکون قیچی
├── برد_سنگ.png            # تصویر نتیجه برد سنگ
├── برد_کاغذ.png           # تصویر نتیجه برد کاغذ
├── برد_قیچی.png           # تصویر نتیجه برد قیچی
└── جمع دوستان.jpg         # عکس پروفایل ربات در تلگرام
```

---

## 🚀 How To Run

Clone the repository:

```
git clone https://github.com/zahrasalimzadeh/rock-paper-scissors-telegram-bot.git
```

Open the project folder:

```
cd rock-paper-scissors-telegram-bot
```

Install dependencies:

```
pip install -r requirements.txt
```

Add your bot token to `.env`, then run the bot:

```
python bot.py
```

Start a chat with your bot on Telegram and send `/start`.

## 🚀 نحوه اجرا

کلون کردن مخزن:

```
git clone https://github.com/zahrasalimzadeh/rock-paper-scissors-telegram-bot.git
```

ورود به پوشه‌ی پروژه:

```
cd rock-paper-scissors-telegram-bot
```

نصب وابستگی‌ها:

```
pip install -r requirements.txt
```

توکن ربات را در `.env` قرار دهید و سپس ربات را اجرا کنید:

```
python bot.py
```

با ربات خود در تلگرام چت کنید و دستور `/start` را ارسال کنید.

---

## 🎥 Demo | دمو

*(Add a screenshot or GIF of the bot in action here)*

---

## 👩‍💻 Developer | توسعه‌دهنده

**Zahra Salimzadeh**

- LinkedIn: <https://www.linkedin.com/in/zahra-salimzadeh-5767582ab/>
- Email: <zahrasalimzadeh7@gmail.com>
