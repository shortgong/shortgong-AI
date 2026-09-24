from pika import BlockingConnection, BasicProperties
import json

from db.db import get_video

def on_message(channel, method_frame, header_frame, body):
    try:
        data = json.loads(body)
        get_video(data['id'])
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    except Exception as e:
        print(e)

connection = BlockingConnection()
channel = connection.channel()
channel.basic_consume(queue='create_video', on_message_callback=on_message)

print("메시지 수신 대기 중")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()