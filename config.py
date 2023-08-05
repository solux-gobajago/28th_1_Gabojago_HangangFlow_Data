import os


aws_db = {
    'user':'solux',
    'password': 'soluxpw00',
    'host': 'solux-server-database.cui0seogsli3.ap-northeast-2.rds.amazonaws.com',
    'port': "3306",
    'database': 'solux'
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{aws_db['user']}:{aws_db['password']}@{aws_db['host']}:{aws_db['port']}/{aws_db['database']}?charset=utf8"