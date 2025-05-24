import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ThreadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.room_group_name = f'thread_{self.thread_id}'
        print(f"[CONNECT] Intento de conexión WebSocket al hilo {self.thread_id} (grupo: {self.room_group_name})")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f"[CONNECT] Conexión aceptada para {self.channel_name}")

    async def disconnect(self, close_code):
        print(f"[DISCONNECT] Desconectando {self.channel_name} del grupo {self.room_group_name}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(f"[RECEIVE] Mensaje recibido en WebSocket: {text_data}")
        data = json.loads(text_data)
        message = data['message']
        user = self.scope["user"].username
        print(f"[RECEIVE] Usuario: {user} | Mensaje: {message}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        )
        print(f"[RECEIVE] Mensaje enviado al grupo {self.room_group_name}")

    # Receive message from room group
    async def chat_message(self, event):
        print(f"[GROUP] Mensaje recibido del grupo: {event}")
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user'],
        }))
        print(f"[GROUP] Mensaje enviado al WebSocket del cliente")

    @database_sync_to_async
    def save_message(self, thread_id, sender_id, message):
        thread = Thread.objects.get(id=thread_id)
        sender = User.objects.get(id=sender_id)

        # validación opcional de seguridad
        if sender not in thread.users.all():
            raise Exception("Usuario no pertenece a este hilo.")

        Message.objects.create(thread=thread, user=sender, content=message)
