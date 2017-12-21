pikacung
========
Pika wrapper for simple publisher and consumer helper.

Requirements
------------
 - Python >= 3.5

Installation
------------
 - Create virtual env `python -m venv env`
 - Activate env `source env/bin/activate`
 - Install pikacung `pip install pikacung`

Example Usage
-------------
 - Example publisher
```
from pikacung import Publish


publisher = Publish()
publisher.publish('EX_PING', 'ping', {'pong': 1}, type='direct')
```
 - Example consumer
```
from pikacung import Consume


consumer = Consume(lambda ch, method, properties, body: print(body.decode('utf-8')))
consumer.before_consuming = lambda: print('Ready for consuming!')
consumer.consume('EX_PING', 'ping', type='direct')
```
