# config.py

DB = {
    'user': 'jh',
    'password': '1234',
    'host': 'go2play.iptime.org',
    'port': 7906,
    'database': 'my_purpose',
}

DB_URL = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
