import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import DataClosedTicket
from .cache_id_ticket import cache_id_ticket
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
        print(self.roomGroupName)
        try:
            check_id_ticket_delete =  await database_sync_to_async(check_delete_id)(self.roomGroupName)
            await self.send(text_data = json.dumps({
                "message":'Этот тикет был закрыт админом. Если у вас есть вопросы, то создайте новый тикет.',
                "username":'System'
                }))
            return
        except DataClosedTicket.DoesNotExist:
            pass
        message = event["message"]
        username = event["username"]

        print(username)
        print(message)
        print(event)
        await self.send(text_data = json.dumps({"message":message ,"username":username}))

def check_delete_id(id_ticket):
    return DataClosedTicket.objects.get(id_ticket=id_ticket).id_ticket