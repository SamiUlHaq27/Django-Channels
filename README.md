  # Django-Channels
    A python library for managing websockets. It is the only module maintained by python officially. It provides two-way data communicatoin b/w server and client.

        It is really helpful in realtime data transmission. It is used in chat, stock market and many other applications.

# Installation
Django channels can be installed using pip package manager as follows:  
### `pip install channels`  
additionally the latest version of django channels required another package called daphne to run asgi server which can be installed by using  
### `pip install daphne`
or you can use this command to install both of them at same time.  
### `pip install channels daphne`

# Configuration
- First of all go to `setting.py` file in you main project directory
- Write both packages in installed_apps as follows:
```
INSTALLED_APPS = [
    'daphne',
    'channels',
]
```
- Change the line:
```
WSGI_APPLICATION = 'DjangoChannels.wsgi.application'
```
to
```
ASGI_APPLICATION = 'DjangoChannels.asgi.application'
```

## Routing
It the same as defining urls for views.  
- For defining routes create a `routing.py` file in your app cotaining routes as follows:
```
from django.urls import path
from . import consumers


url_patterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
    path("ws/ac/", consumers.MyAsyncConsumer.as_asgi()),
]
```
- Then target it from `asgi.py` file in your main project directory as follows:
```
import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from websocket_app.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChannels.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
```
or we can write the list of patterns directly in `URLRouter`  

# Creating Consumers
A consumer in websocket work as a view in regular django. To create a consumer follow these steps:
- Create a `consumers.py` file in your app or main project directory:
- Import consumers by using `from channels.consumer import SyncConsumer, AsyncConsumer`
- There are two types of consumers `SyncConsumer` and `AsyncConsumer`.
  - Sync Consumer handles only one request at a time and process next request after reponding previous request.
  - Async Consumer can handle multiple reqeusts at the same time.
### SyncConsumer can be created as follows:
```
class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("connection openned...")
    
    def websocket_receive(self, event):
        print("message reveived...")
    
    def websocket_close(self, event):
        print("connection closed...")
```
### AsyncConsumer can be created as follows:
```
class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("connection openned...")
    
    async def websocket_receive(self, event):
        print("message reveived...")
    
    async def websocket_close(self, event):
        print("connection closed...")
```
additionaly `await` keyword is required for calling any function in AsyncConsumer.  
## Accept request
the connection will not be created because we didn\'t accepted it to accept the connect write this in `websocket_connect` function:
```
self.send({
            "type":"websocket.accept",
        })
```
## websocket_connect
This function is executed when client requests for connection.
## websocket_receive
This function is executed when client sends the message.
## websocket_close
This function is executed when connections is terminated either by server or by client.

# Sending messges
A message can be sent to the client by using send functions as follows:
```
self.send({
                "type":"websocket.send",
                "text":"this is server sending message to you",
            })
```
## Serialization
As only text data is permitted to be transmitted so we can use `json` library to convert python dictionary to string by using `json.dumps(<type:dict>)`  
