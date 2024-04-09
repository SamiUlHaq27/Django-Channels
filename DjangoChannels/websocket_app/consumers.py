from channels.consumer import SyncConsumer, AsyncConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("connection openned...")
        self.send({
            "type":"websocket.accept",
        })
    
    def websocket_receive(self, event):
        print("message reveived...")
        for i in range(10):
            self.send({
                "type":"websocket.send",
                "text":str(i),
            })
            sleep(1)
    
    def websocket_close(self, event):
        print("connection closed...")

class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("connection openned...")
        await self.send({
            "type":"websocket.accept",
        })
    
    async def websocket_receive(self, event):
        print("message reveived...")
        for i in range(10):
            await self.send({
                "type":"websocket.send",
                "text":str(i),
            })
            await asyncio.sleep(1)
    
    async def websocket_close(self, event):
        print("connection closed...")