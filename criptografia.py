
texto_simples = str(input("Por favor, digite seu texto: "))
chave = int(input("Por favor, digite o número da chave de segurança: "))

texto_cifrado = ''
for i in range(len(texto_simples)):
    char = texto_simples[i]

    if char.isalpha() and char.isupper():
        texto_cifrado += chr((ord(char) + chave - 65) % 26 + 65)

    else:
        texto_cifrado += chr((ord(char) + chave - 97) % 26 + 97)
print(f'''
TEXTO SIMPLES: {texto_simples}
CHAVE FORNECIDA: {chave}
TEXTO CIFRADO: {texto_cifrado}''')

# ord - recebe a letra como código ASCII e retorna o número da mesma
# chr - recebe o número como código ASCII e retorna a letra/símbolo correspondente
