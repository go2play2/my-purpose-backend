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
S3_ACCESS_KEY_ID = 'AKIAZQ3DTXGROWKJN6HI'
S3_SECRET_KEY = '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'
S3_BUCKET_URL = f"http://{S3_BUCKET_NAME}.s3.amazoneaws.com"
