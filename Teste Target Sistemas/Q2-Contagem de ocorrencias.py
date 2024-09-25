def contar_as(texto):
    return texto.lower().count('a')

texto = input("Digite um texto: ")
qtd_as = contar_as(texto)
print(f"A letra 'a' aparece {qtd_as} vezes no texto.")

#Explicação
#A função 'contar_as' converte todo o texto para minúsculo e utiliza o método 'count' para contar as ocorrências da letra 'a'.