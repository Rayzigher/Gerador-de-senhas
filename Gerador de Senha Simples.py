# Gerador de senhas simples.
import random
import string

# Variaveis do Modulo String
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Organizar padrões da senha
def gerar_senha(length, include_lowercase, include_uppercase, include_digits, include_special_characters):
    # Solicitar preferencias do usuario
    allowed_characters = ""
    if include_lowercase:
        allowed_characters += lowercase
    if include_uppercase:
        allowed_characters += uppercase
    if include_digits:
        allowed_characters += digits
    if include_special_characters:
        allowed_characters += special_characters
    # Verificar se pelo menos um caractere foi selecionado

    if not allowed_characters:
        raise ValueError("Você deve selecionar pelo menos um tipo de caractere")

# Gerar a senha
    password = "".join((random.choice(allowed_characters)) for _ in range(length))
    return password


# Comprimento da senha
length = int(input("Digite qual vai ser o comprimento da senha: "))

# Checar se tem pelo menos 4 digitos
if length < 4:
    raise ValueError("O comprimento deve ser maior ou igual a 4 digitos")

# Solicitar preferências do usuário
include_lowercase = input("Incluir letras minúsculas? (sim ou não): ").strip().lower() == "sim"
include_uppercase = input("Incluir letras maiúsculas? (sim ou não): ").strip().lower() == "sim"
include_digits = input("Incluir números? (sim ou não): ").strip().lower() == "sim"
include_special_characters = input("Incluir caracteres especiais? (sim ou não): ").strip().lower() == "sim"

# Exibir a senha
try:
    password = gerar_senha(length, include_lowercase, include_uppercase, include_digits, include_special_characters)
    print(f"sua senha é {password}")
except ValueError as e:
    print(e)







    


    

    
    


        
        
   

    
    


