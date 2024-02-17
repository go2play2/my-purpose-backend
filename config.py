# config.py

# Database
DB = {
    'user': 'jh',
    'password': '1234',
    'host': 'go2play.iptime.org',
    'port': 7906,
    'database': 'my_purpose',
}

DB_URL = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"


# JWT
JWT_SECRET_KEY = 'jaehoon'


# S3 Bucket
S3_BUCKET_NAME = 'my-purpose-bucket'
S3_ACCESS_KEY_ID_P1 = 'AKIAZQ3DT'
S3_ACCESS_KEY_ID_P2 = 'XGROWKJN6HI'
S3_ACCESS_KEY_ID = f"{S3_ACCESS_KEY_ID_P1}{S3_ACCESS_KEY_ID_P2}"
S3_SECRET_KEY_P1 = '5+tVNWPbHIMxrDLhA1'
S3_SECRET_KEY_P2 = '5s620KT4IfjiARQLphfc1Z'
S3_SECRET_KEY = f"{S3_SECRET_KEY_P1}{S3_SECRET_KEY_P2}"
S3_BUCKET_URL = f"http://{S3_BUCKET_NAME}.s3.amazoneaws.com"
