import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import DataTicket
from .utils import random_id_ticket
from django.db import connection
from django.db.utils import IntegrityError, ProgrammingError
from .cache_id_ticket import cache_id_ticket
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async



class ChatSaport(AsyncWebsocketConsumer):
    async def connect(self):
        print('1')
        self.roomGroupName = cache_id_ticket[0]
        del cache_id_ticket[0]
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        
        await self.accept()
        
    async def disconnect(self, message):
        print('2')
        username = self.scope["user"]
        print(username)
        check_is_staff = await database_sync_to_async(check_staff)(username)
        print(check_is_staff)
    


    async def receive(self, text_data):
        print('3')
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
                "username" : username ,
            })
        
    async def sendMessage(self, event):
        print('4')
        message = event["message"]
        username = event["username"]
        #делать проверку на пользователя(имя румы). Если его тикет лежит в таблице для закрытых тикетов, то делаем дисконект.
        #и опвещаем о том, что тикет был закрыт
        #Добавить логику добалвяния тикета в бд о закрытых тикетов
        print(username)
        print(message)
        print(event)
        await self.send(text_data = json.dumps({"message":message ,"username":username}))

def check_staff(username):
    return User.objects.get(username=username).is_staff