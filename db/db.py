import pymysql
import config
import pymysqlpool

pymysqlpool.logger.setLevel('DEBUG')

dbconfig = {
  "host": config.DB_HOST,
  "port": int(config.DB_PORT),
  "database": config.DB_DATABASE,
  "user": config.DB_USER,
  "password": config.DB_PASSWORD
}

pool = pymysqlpool.ConnectionPool(
    size=10, 
    maxsize=100, 
    pre_create_num=10, 
    name='pool', 
    **dbconfig
)

def get_con():
    con = pool.get_connection()
    cur = con.cursor()
    return con, cur