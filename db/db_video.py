from const.video_status import PROCESSING, COMPLETED, FAILED
from db.db import pool, get_con

def get_video(
    id: int
):
    con, cur = get_con()
    try:
        sql = 'SELECT * FROM video WHERE id = %s'
        vals = (id,)
        cur.execute(sql, vals)
        row = cur.fetchone()
        if row:
            return row
        else:
            raise Exception("Id isn't exists.")
    except Exception as e:
        raise Exception(e)
    finally:
        con.close()

def update_video_status(
    id: int,
    status: PROCESSING | COMPLETED | FAILED
):
    con, cur = get_con()
    try:
        sql = 'UPDATE video SET status = %s WHERE id = %s'
        vals = (status, id,)
        cur.execute(sql, vals)
        con.commit()    
    except Exception as e:
        raise Exception(e)
    finally:
        con.close()

def update_video_content(
    id: int,
    title: str,
    content: str,
):
    con, cur = get_con()
    try:
        sql = 'UPDATE video SET title = %s, content = %s WHERE id = %s'
        vals = (title, content, id,)
        cur.execute(sql, vals)
        con.commit()
    except Exception as e:
        raise Exception(e)
    finally:
        con.close()