from channels.generic.websocket import WebsocketConsumer


class GameData(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send('All good')
