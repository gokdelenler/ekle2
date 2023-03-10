import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
 #add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1847194093/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1847194093')
   open(f"Users/1847194093/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = "24864975"
API_HASH = "73251b7458f360ace1c92adaf8d8ac16"
BOT_TOKEN = "5910247282:AAEjy9j-Pn2FFvzf1t52eTJkRYSai15vVpU"
UPDATES_CHANNEL = "iyiolmayolunda"
OWNER = [1940508871,]
PREMIUM = [1940508871,]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))



with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="??zg??n??m efendim, yasakland??n??z. ??leti??im [Destek Grubu](https://t.me/mutluuolun).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**L??tfen Beni Kullanmak ????in G??ncel Kanal??ma Kat??l??n!\n ve Kontrol etmek i??in t??klay??n /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("???? G??ncelleme Kanal??na Kat??l??n ????", url=f"https://t.me/iyiolmayolunda")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**Bir ??eyler ters gitti. ??leti??im [Destek Grubu](https://t.me/mutluuolun).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1




# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Login ???", callback_data="Login"), InlineKeyboardButton("Gruba Ekle ????", callback_data="Adding") ],[InlineKeyboardButton("Telefon Ekle ??????", callback_data="Edit"), InlineKeyboardButton("Telefonlar ????", callback_data="Ish")],[InlineKeyboardButton("Telefon Kald??r ??????", callback_data="Remove"), InlineKeyboardButton("Y??netim paneli", callback_data="Admin")]])
   await message.reply_text(f"**Merhaba** `{message.from_user.first_name}` **!\n\nBen @tweety6r taraf??ndan  ??ye ??ekimi i??in tasarlanm???? botum. \n??cretli veya ??cretsiz ??ye ??ekmek i??in tasarland??m,\nSizler i??in en iyisi.\n\n???? Sohbet ve ticari Grubumuz @mutluuolun**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return 
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Art??k Premium Kullan??c?? De??ilsiniz\nL??tfen bir Alt Yaz??ya Sahip Olun\n200rs ayda\nPm @tweety6r**")
      return'''
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**Giri?? yapmak i??in hesap say??s??n?? girin (1, 2, 3, 4 ,5)\n\nBilgi @tweety6r**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**Ge??ersiz Bi??im 1'den az Yeniden deneyin\n\n??leti??im @tweety6r**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**Yaln??zca ??unlar?? ekleyebilirsiniz: {100-a} Telefon no \n\nSohbet destek ?????? @mutluuolun**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**??imdi Telegram Hesab??n??z??n Telefon Numaras??n?? Uluslararas?? Bi??imde G??nderin. \nDahil **??lke Kodu**. \n??rnek: **+14154566376 = 14154566376 i??aret olmadan +**\n\nDestek ???????? @mutluuolun**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**Alan kodu  + dahil de??ildir.\n\nBilgi i??in ?????? @tweety6r**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). Telefon: {phone} Ba??ar??l?? oldu ???\n\nBilgi i??in @tweety6r**")
         else:
            await app.send_message(message.chat.id, """**Ge??ersiz Say?? Bi??imi Yeniden deneyin\n\nBilgi i??in ???????? @tweety6r**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nBilgi @tweety6r**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return 
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Art??k Premium Kullan??c?? De??ilsiniz\nL??tfen bir Alt Yaz??ya Sahip Olun\n200rs ayda\nPm @tweety6r\n\nResmi Grup @mutluuolun**")
      return'''
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"Kanka Flood {e.x} Saniye")
            return
         except PhoneNumberInvalidError:
            await message.reply("Telefon Numaran??z Ge??ersiz.\n\nBas??n /start yeniden ba??lamak i??in!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} Yasakland??")
            continue
         try:
            otp = await app.ask(message.chat.id, ("Telefon numaran??za bir Kod g??nderilir, \nL??tfen Kodu `1 2 3 4 5` gibi yazal??m. __(Her say?? aras??ndaki bo??luk!)__ \n\nBot Kod g??ndermiyorsa, deneyin /restart ve G??revi yeniden ba??lat??n /start Bot'a komut.\nBas??n /cancel iptal etmek i??in."), timeout=300)
         except TimeoutError:
            await message.reply("5 Dakikal??k Ula????lan S??re S??n??r??.\nBas??n /start yeniden ba??lamak i??in!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("Ge??ersiz Kod.\n\nBas??n /start yeniden ba??lamak i??in!")
            return
         except PhoneCodeExpiredError:
            await message.reply("Kodun S??resi Doldu.\n\nPress /start yeniden ba??lamak i??in!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Hesab??n??zda iki ad??ml?? do??rulama var.\nL??tfen ??ifrenizi Girin.",timeout=300)
            except TimeoutError:
               await message.reply("`5 Dakikal??k Ula????lan S??re S??n??r??.\n\nBas??n /start yeniden ba??lamak i??in!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/1847194093/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/1847194093/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="??yi haber, ??u anda hesab??n??za herhangi bir s??n??r uygulanm??yor. Bir ku?? gibi ??zg??rs??n!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"Ba??ar??yla Giri?? Yap??n ??? Yap??lm????.\n\n**??sim:** {me.first_name}\n**Kullan??c?? ad??:** {me.username}\n**Telefon:** {phone}\n**SpamBot ??statistikleri:** {stats}\n\n**??rtibat @tweety6r**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**Telefon numaras??n?? girmediniz \nl??tfen Bilgileri ?????? d??zenleyiniz. /start.\n\nYard??m i??in @tweety6r**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Hata: {e}\n\nYard??m i??in @tweety6r**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**T??m Kay??tl?? Numara Giri??leri {s} Kullan??labilir Hesap {po} \n\nBilgi i??in @tweety6r**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nSahibim ???????? @tweety6r**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Art??k Premium Kullan??c?? De??ilsiniz\nL??tfen Ara ara ??ekim yap??n??z.**")
      return'''
   number = await app.ask(chat_id=message.chat.id, text="**??imdi ??ye Al??nacak Grubun Kullan??c?? Ad??n?? G??nderin")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**??imdi Kendi Grubunun Kullan??c?? Ad??n?? G??nder**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Ka?? Hesap Eklediysen. (Say??s??n?? yaz??n. 1 2 3 4 5 gibi) Hadi ??ye ??ekelim.**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**??yeleri ??al??yorum hocam....**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nBotdestek @DarkCloudUnderground**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Hata: {phone} Baz?? Hatalar Nedeniyle Sonrakine Ta????n??yor**")
                     break
                  if dad>40:
                     r+="**\nPm ???? @tweety6r**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**ekleme ba??lad??**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nPm ???? @tweety6r**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError i??in {s.seconds} sec\nSonraki Numaraya Ge??me**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Giri??te Hatavar"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**??ok Fazla PeerFloodError\nSonraki Numaraya Ge??me**")
                     break
                  status = 'Hata... Tekrar deneyiniz.'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ???   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Hata: {e} n\n\ @mutluuolun")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nBilgi i??in @tweety6r**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Art??k Premium Kullan??c?? De??ilsiniz\nL??tfen bir Alt Yaz??ya Sahip Olun\n200rs ayda tahmini ortalama\nPm ???? @tweety6r**")
      return'''
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Telefon Numaralar??n??z**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\n??leti??im ?????? By @tweety6r**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Your Phone Numbers are**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\n??leti??im ?????? By @tweety6r**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Art??k Premium Kullan??c?? De??ilsiniz\nL??tfen bir Alt Yaz??ya Sahip Olun\n200rs ortalama\nPm ???? @tweety6r**")
      return'''
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**Kald??r??lacak Numaray?? G??nder\n\n??leti??im i??in Sahibime yaz??n @tweety6r**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="Ba??ar??yla Tamamland??")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nSahibim ???????? @tweety6r**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Kullan??c?? ???", callback_data="Users")], [InlineKeyboardButton("Broadcast ????", callback_data="Broadcast")],[InlineKeyboardButton("Kullan??c?? Ekle", callback_data="New")], [InlineKeyboardButton("Kullan??c??lar?? Kontrol Et", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**Hi** `{message.from_user.first_name}` **!\n\nDark Cloud Bot ??LE TEKNOLOJ??N??N Y??netici Paneline Ho?? Geldiniz\n\n??leti??im ?????? By @tweety6r**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**Bot'un sahibi de??ilsiniz\n\nBotun Sahibi ???????? By @tweety6r**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /login Giri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /phonesee Giri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in.**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /remove Giri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in.**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /adding Giri??'ten eklemeye ba??lamak i??in ???**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /phone Giri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in.**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yard??m i??in burday??m..!\nSadece t??klay??n /start Eve Gitmek i??in.**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"L??tfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Yeni Kullan??c??n??n Kullan??c?? Kimli??ini G??nderiniz.**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="Ba??ar??yla Tamamland??")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Pm i??in  ???? By @tweety6r**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Kullan??c?? ???", callback_data="Users")], [InlineKeyboardButton("Broadcast ????", callback_data="Broadcast")],[InlineKeyboardButton("Kullan??c?? Ekle", callback_data="New")], [InlineKeyboardButton("Kullan??c??lar?? Kontrol Et", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**DARK Cloud Bot ??LE TEKNO Y??netici Paneline Ho?? Geldiniz**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**Bot'un sahibi de??ilsiniz \n\nSahibime yaz??n. By @tweety6r**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**??imdi bana Yay??n i??in mesaj verin**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"Ba??ar??yla Yay??nland?? {a} Sohbet\nBa??ar??s??z - {b} Sohbet !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Hata: {e}\n\nYard??m i??in @DarkCloudUnderground**")






print("??ye Ekleme botu  Ba??ar??l?? Bir ??ekilde Ba??lad??........")
app.run()
 
