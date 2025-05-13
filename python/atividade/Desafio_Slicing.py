# String original invertida
cadeia = "acitametaM ,5.8 ,otipeP ordeP"

# Inverter a string
cadeia_invertida = cadeia[::-1]

# Separar os elementos por vírgula
elementos = cadeia_invertida.split(',')

# Extrair nome, nota e matéria
nome_aluno = elementos[2].strip()  # Remove espaços em branco
nota = elementos[1].strip()
materia = elementos[0].strip()

# Mostrar resultado
print(f"{nome_aluno} tirou {nota} em {materia}")