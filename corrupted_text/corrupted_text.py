corrupted_text = "ZadsadUasdasKsadAxzcvbert234awdsffMsad123Asad3wq24GasdasdAsadasdRasc3w24kiisadIasdsadasAa"
secret_message = ""
for char in corrupted_text:
    if char.isupper():
        secret_message += char
print (secret_message)
