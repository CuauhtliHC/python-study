text = input("Ingresa un texto a analizar: ")
letters = input("Ingresa 3 letras separadas por espacio: ").split(" ")
textRevers = " ".join(text.split(" ")[::-1])

print(f"""El numero de letras que escogio apareciendo en su texto son los siguientes:
{letters[0]}: {text.lower().count(letters[0].lower())}
{letters[1]}: {text.lower().count(letters[1].lower())}
{letters[2]}: {text.lower().count(letters[2].lower())}

El numero de paralabras en su texto es de: {len(text.split(" "))} 

Primera letra de su texto: {text[0]}

Ultima letra de su texto: {text[-1]}

Su texto invertido es el siguiente: 
{textRevers}

La palabra en python aparace en su texto: {"python" in text}""")