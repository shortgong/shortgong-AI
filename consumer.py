from pika import BlockingConnection, BasicProperties
import pika
import json

from api.gemini import make_video_content
from const.video_status import COMPLETED, FAILED
from db.db_video import get_video, update_video_content, update_video_status

def on_message(channel, method_frame, header_frame, body):
    try:
        data = json.loads(body)
        
        video_id = data['id']
        video = get_video(video_id)
        video_draft = video[4]
        print(video_draft)
        
        try:
            title, content = make_video_content(video_draft)
            update_video_content(video_id, title, content)
            update_video_status(video_id, COMPLETED)
        except Exception as e:
            print(f"Inner Error: {e}")
            update_video_status(video_id, FAILED)
            channel.basic_reject(delivery_tag=method_frame.delivery_tag, requeue=False)
        else:
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        
    except Exception as e:
        channel.basic_reject(delivery_tag=method_frame.delivery_tag, requeue=False)
        print(f"Outer Error: {e}")

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    'localhost',
    5672,
    '/',
    credentials,
    retry_delay=10,
    heartbeat=1000000
)

connection = BlockingConnection()
channel = connection.channel()
channel.basic_consume(queue='q.create_video', on_message_callback=on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()