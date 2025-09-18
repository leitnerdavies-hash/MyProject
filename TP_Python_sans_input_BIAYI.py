date_heure = "2025-09-10 14:00:00"
expediteur = "Daniel Shongo"
tel_expediteur = "+243970000000"
destinataire = "Rosaline"
tel_destinataire = "+243820000000"
montant = 25000.00
reference = "TEST-001"


frais = max(montant * 0.01, 100)
total_debite = montant + frais

# Affichage avec f-strings
print("=== REÇU (f-string) ===")
print(f"Date/Heure : {date_heure}")
print(f"Expéditeur : {expediteur} ({tel_expediteur})")
print(f"Destinataire : {destinataire} ({tel_destinataire})")
print(f"Montant : {montant:.2f} CDF")
print(f"Frais : {frais:.2f} CDF")
print(f"Total débité : {total_debite:.2f} CDF")
print(f"Référence : {reference}")
print()

# Affichage avec str.format()
print("=== REÇU (str.format) ===")
print("Date/Heure : {}".format(date_heure))
print("Expéditeur : {} ({})".format(expediteur, tel_expediteur))
print("Destinataire : {} ({})".format(destinataire, tel_destinataire))
print("Montant : {:.2f} CDF".format(montant))
print("Frais : {:.2f} CDF".format(frais))
print("Total débité : {:.2f} CDF".format(total_debite))
print("Référence : {}".format(reference))
print()

# Affichage avec l'opérateur %
print("=== REÇU (% operator) ===")
print("Date/Heure : %s" % date_heure)
print("Expéditeur : %s (%s)" % (expediteur, tel_expediteur))
print("Destinataire : %s (%s)" % (destinataire, tel_destinataire))
print("Montant : %.2f CDF" % montant)
print("Frais : %.2f CDF" % frais)
print("Total débité : %.2f CDF" % total_debite)
print("Référence : %s" % reference)