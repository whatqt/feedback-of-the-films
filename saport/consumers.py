import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import InfoTicket
from .utils import random_id_ticket
from django.db import connection



class ChatSaport(AsyncWebsocketConsumer):
    async def connect(self):
        print('1')
        id_ticket = random_id_ticket()
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         INSERT INTO 
        #     """)     
        self.roomGroupName = id_ticket
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        print('2')
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_layer 
        )

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
        
    async def sendMessage(self , event):
        print('4')
        message = event["message"]
        username = event["username"]
        print(username)
        print(message)
        print(event)
        await self.send(text_data = json.dumps({"message":message ,"username":username}))