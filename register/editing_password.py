import hashlib


def password_to_hash(password: str):
    # Преобразуем пароль в байтовую строку
    password_bytes = password.encode('utf-8')
    
    # Создаем объект хеша типа SHA-256
    hash_object = hashlib.sha256()
    
    # Обновляем хеш с байтами пароля
    hash_object.update(password_bytes)
    
    # Получаем хеш в виде шестнадцатеричной строки
    password_hash = hash_object.hexdigest()
    
    return password_hash

# def dell_spaces_password(password: str):
#     print(password.lstrip())

