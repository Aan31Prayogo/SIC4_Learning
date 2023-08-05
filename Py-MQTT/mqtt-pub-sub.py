import time   
import paho.mqtt.client as mqtt
import random

    
def publish_message(pub_msg,pub_topic,pub_qos):
    try:
        info = mqttClient.publish(
            topic=pub_topic,
            payload=pub_msg.encode('utf-8'),
            qos=pub_qos,
        )
        info.wait_for_publish()
        print("status => ", info.is_published())
    
    except Exception as e:
        print(" failed to pubish message with error " + str(e))
    
def on_message_topic(client, userdata, msg):
    payload = str(msg.payload.decode('utf-8'))
    print("message status = ", payload)
    
host = 'broker.hivemq.com'
port = 1883
topic = 'home/livingroom/lamp1'
    
mqttClient = mqtt.Client()
mqttClient.message_callback_add(topic, on_message_topic)

mqttClient.connect(host, port)
#mqttClient.subscribe(topic)

#mqttClient.loop_forever()
mqttClient.loop_start()

while True:
    suhu = random.uniform(28.0,30.0)
    
    publish_message(str(suhu), "home/garden/temp",2)
    #publish_message(hum,"garden/humidity",0)
    time.sleep(5)
