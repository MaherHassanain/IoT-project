import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost',1883) #as Broker



while True:
    client.publish("topic/test", input('Message : '))
