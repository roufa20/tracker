from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['bigdata2.ip-188-165-248.eu:9092','bigdata3.ip-188-165-248.eu:9092','bigdata4.ip-188-165-248.eu:9092'])

# Asynchronous by default
future = producer.send('facebook', b'test python producer')
