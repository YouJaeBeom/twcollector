import jwt
token = "7d65a6ac19c21cef946f3483f8d32e044a60a609"

user_id = jwt.decode(token,'wecode', algorithms=['HS256'])

print(user_id)