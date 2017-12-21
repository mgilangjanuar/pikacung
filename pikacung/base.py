import pika


class Base():
    
    def __init__(self, host='localhost', port=5672, username='guest', password='guest'):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self.create_pika()

    def create_pika(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                credentials=pika.PlainCredentials(self._username, self._password)
            )
        )
        self.channel = self.connection.channel()
