import jwt
from app import create_app


data_to_encode = {'some': 'payload'}

enc_secret = 'my-secret'
algorithm = 'HS256'
encodeded = jwt.encode(data_to_encode, enc_secret, algorithm=algorithm)

print(encodeded)

decoded = jwt.decode(encodeded, enc_secret, algorithms=[algorithm])
print("-" * 30)
print(decoded)


app = create_app()
