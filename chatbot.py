from pyrogram.types import ChatAction, Message

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re


API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"
SESSION_NAME = os.environ.get("SESSION_NAME", "BQC6kfsAEXjwLZLVZa4U9dZLVc1lnYLjaP_VCkKFfkT1LIKILi1rcJVLsabFAC06vBefLbuuuBqdqKBQLa7d0NkJxx0b0Bodv4f1w_W8loMF3mBft3Vyq0jjYQZ-TfhJbTdrwBBTWpvrTsKMSuXxoa24bO99fZ8apTkhUAhqzWI4y8nHjjyleWH-Txg75kO8p1pp-6mYqOKsTMzB5Q5aRswQ8H9jk2kLr54c3pkX4VyzsobKj9Zv0D3YFxCh07ZvoNawGmxkLf6UqoPYVE6wcMkmBNEdIpMpza3FAwXclnM69fXa8Pu5CZKJhE3uTwnvQVgwVB403JGahOjbCNh77xwKkX1HgwAAAAGJWJDZAA")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority")


client = Client(SESSION_NAME, API_ID, API_HASH)





@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"** ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")
    
    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       if not is_Daxx:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Daxx:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       if not is_Daxx:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Daxx:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
