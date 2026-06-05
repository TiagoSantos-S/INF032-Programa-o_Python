# 10. sabendo-se que somente os municípios que possuem mais de 20 mil eleitores
# aptos tem segundo turno nas eleições para prefeito caso o primeiro colocado
# não tenha mais do que 50% DOS VOTOS. FAZER UM PROGRAMA QUE LEIA O NOME do município, a
# quantidade de eleitores aptos, o número de votos do candidato mais votado e informar se ele terá ou não
# segundo turno.


municipio_nome = input("Insira o nome do município: ")
eleitores_aptos = int(input("Insira a quantidade de eleitores aptos: "))
votos_candidato = int(input("Insira a votação do candidato mais votado: "))


metade = eleitores_aptos / 2


if eleitores_aptos > 20000:
    
    if votos_candidato <= metade:
        print(f"Em {municipio_nome} TERÁ segundo turno.")
    else:
        print(f"Em {municipio_nome} NÃO terá segundo turno (Candidato eleito com mais de 50%).")
else:
    print(f"Em {municipio_nome} NÃO terá segundo turno (Município com 20 mil eleitores ou menos).")

