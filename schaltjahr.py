#schaltjahrpruefung.py -> Verschachtelte Verzweigung
jahr = int(input("Bitte Jahr eingeben : "))
if jahr % 100 == 0:
	#Anweisungen true
	if jahr % 400 == 0:
		#Anweisungen true
		print("Schaltjahr")
	else:
		#Anweisungen false
		print("Kein Schaltjahr")
else:
	#Anweisungen false
	if jahr % 4 == 0:
		print("Schaltjahr")
	else:
		print("Kein Schaltjahr")
input("Bitte mit Eingabetaste beenden")               