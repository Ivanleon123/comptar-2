def comptar_vocals(paraula):
    """Compta el número de vegades que apareix cada vocal en la paraula."""
    # Inicialitzar un diccionari per a les vocals
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recórrer cada caràcter de la paraula
    for caracter in paraula.lower():  # Convertim a minúscules
        if caracter in vocals:
            vocals[caracter] += 1  # Incrementar el comptador de la vocal corresponent

    # Preparar la cadena de resultat
    resultat = f"Hi ha {vocals['a']} a’s, {vocals['e']} e’s, {vocals['i']} i’s, {vocals['o']} o’s i {vocals['u']} u’s."
    
    return resultat

# Prova de la funció
paraula = "Ratapinyada"
resultat = comptar_vocals(paraula)
print(resultat)  # Retorna "Hi ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s."