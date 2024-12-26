# Startguthaben
konto = 1000

print("Ihr aktuelles Guthaben beträgt: {konto} EURO")
aktion = input("Möchten Sie 'einzahlen' oder 'abheben'? ").strip().lower()

if aktion == "einzahlen":
    betrag = int(input("Wie viel möchten Sie einzahlen? "))
    konto += betrag

elif aktion == "abheben":
    betrag = int(input("Wie viel möchten Sie abheben? "))
    konto -= betrag

print("Ihr aktuelles Guthaben beträgt jetzt: {konto} EURO")