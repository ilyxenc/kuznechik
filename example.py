import main as gh #grasshopper

textInput = "Hello, мир" # Ввод исходного текста
password = "strongPassword" # Ввод пароля

# Получение ключей для шифрования и расшифрования
K = gh.getKeys(password)

# Шифрование
textEncrypt = gh.encrypt(textInput, K)

# Расшифрование
textDecrypt = gh.decrypt(textEncrypt, K)

print(textEncrypt, textDecrypt)
