def calcolatore_medie():
    print("Benvenuto nel Calcolatore di Medie!")
    num_materie = int(input("Quante materie vuoi calcolare? "))

    medie = {}
    for _ in range(num_materie):
        materia = input("Inserisci il nome della materia: ")
        num_voti = int(input(f"Inserisci il numero di voti per {materia}: "))

        voti = []
        for i in range(num_voti):
            voto = int(input(f"Inserisci il voto {i + 1} per {materia}: "))
            voti.append(voto)

        media = sum(voti) / num_voti
        medie[materia] = media

    print("Risultati:")
    for materia, media in medie.items():
        print(f"{materia} = {media}")
    print("Grazie per aver usato questo tool!")

calcolatore_medie()
