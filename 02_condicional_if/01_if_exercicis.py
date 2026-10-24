###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
print("\nExercici 1:")
numero1= int(input("Introdueix el primer nombre enter: "))
numero2 = int(input("Introdueix el segon nombre enter: "))

if numero1 > numero2:
    print(f"{numero1} és més gran que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} és més petit que {numero2}")
else:
    print("Els numeros que has introduiït son iguals.")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
print("\nExercici 2:")
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ").strip()

if operacio == "/" and num2 == 0:
    print("Error: no es pot dividir per zero.")
elif operacio == "+":
    calcul = num1 + num2 
    print(f"El resultat de la suma és: {calcul}")
elif operacio == "-":
    calcul = num1 - num2
    print(f"El resultat de la resta és: {calcul}")
elif operacio == "*":
    calcul = num1 * num2
    print(f"El resultat de la multiplicació és: {calcul}")
elif operacio == "/":
    calcul = num1 / num2
    print(f"El resultat de la divisió és: {calcul}")
else:
    print(f"Aquesta no és una operació vàlida.")


# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
print("\nExercici 3:")
any = int(input("Introdueix un any: "))
if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:
    print(f"L'any {any} és un any de traspàs.")
else:
    print(f"L'any {any} no és un any de traspàs.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
print("\nExercici 4:")
edat = int(input("Introdueix una edat: "))
if edat < 0:
    print("Edat no vàlida.")
elif edat >= 0 and edat <= 2:
    print(f"L'edat introduïda ({edat}) pertany a un nadó (0-2 anys)")
elif edat > 2 and edat <= 13:
    print(f"L'edat introduïda ({edat}) pertany a un infant (3-12 anys)")
elif edat > 13 and edat <= 17:
    print(f"L'edat introduïda ({edat}) pertany a un adolescent (13-17 anys)")
elif edat > 17 and edat <= 64:
    print(f"L'edat introduïda ({edat}) pertany a un adult (18-64 anys)")
else:
    print(f"L'edat introduïda ({edat}) pertany a una persona gran (65 anys o més)")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
print("\nExercici 5:")
senyal = float(input("Introdueix el nivell de senyal rebut (RSSI) en dBm: "))

if senyal >= -50:
    print(f"La qualitat de la cobertura és excel·lent.")
elif senyal >= -67:
    print("Cobertura bona.")
elif senyal >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
print("\nExercici 6:")


# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
print("\nExercici 13:")


# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
print("\nExercici 14:")
servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Quants usuaris estan afectats? "))

if usuaris < 0:
    print("El nombre d'usuaris no pot ser negatiu.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n): ").strip().lower()

    if (servei_critic == "s" and alternativa != "s") or (usuaris >= 50 and alternativa != "s"):
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")