import pymysql
import config
from const.video_status import PROCESSING, COMPLETED, FAILED

conn = pymysql.connect(host=config.DB_HOST, 
                       port=int(config.DB_PORT),
                       user=config.DB_USER,
                       password=config.DB_PASSWORD,
                       database=config.DB_DATABASE,
                       charset='utf8')
cursor = conn.cursor()

def get_video(
    id: int
):
    sql = 'SELECT * FROM video WHERE id = %s'
    vals = (id,)
    cursor.execute(sql, vals)
    row = cursor.fetchone()
    if row:
        return row
    else:
        raise Exception("Id isn't exists.")

def update_video_status(
    id: int,
    status: PROCESSING | COMPLETED | FAILED
):
    sql = 'UPDATE video SET status = %s WHERE id = %s'
    vals = (id, status,)
    cursor.execute(sql, vals)
    conn.commit()

def update_video_content(
    id: int,
    title: str,
    content: str,
):
    sql = 'UPDATE video SET title = %s, content = %s WHERE id = %s'
    vals = (id, title, content,)
    cursor.execute(sql, vals)
    conn.commit()