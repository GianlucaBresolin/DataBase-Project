import random
import string


nomi = [
    "Marco", "Laura", "Giovanni", "Francesca", "Luca", "Chiara", "Alessio", "Sofia",
    "Andrea", "Giulia", "Stefano", "Martina", "Matteo", "Valentina", "Davide", "Emma",
    "Roberto", "Alice", "Simone", "Elisa"
]

cognomi = [
    "Rossi", "Bianchi", "Ferrari", "Esposito", "Romano", "Ricci", "Marino", "Greco",
    "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Rizzo", "Lombardi", "Moretti",
    "Barbieri", "Fontana", "Santoro", "Mariani"
]



def generate_random_birthdate():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1960, 2000)
    return f"{day:02d}/{month:02d}/{year}"

date_di_nascita = []

while len(date_di_nascita) < 30:
    birthdate = generate_random_birthdate()
    date_di_nascita.append(birthdate)

nazionalita = ["Italiana", "Francese", "Spagnola", "Giapponese", "Brasiliana", "Inglese", "Tedesca", "Cinese", "Messicana", "Canadese"]


def generate_random_cf():
    # Genera un codice fiscale casuale composto da 16 caratteri alfanumerici
    characters = string.ascii_uppercase + string.digits
    random_cf = ''.join(random.choices(characters, k=16))
    return random_cf

codici_fiscali = []
for i in range(200):
    cf = generate_random_cf()
    while cf in codici_fiscali:
        cf = generate_random_cf()
    
    codici_fiscali.append(cf)
    



file_name = "tabellaGiocatori.txt"

file_content = []

file_content.append("Giocatori \n")
for i in range(200):
    file_content.append('( "' + codici_fiscali[i] + '" ,  "' + random.choice(nomi) +  '" ,  "' + random.choice(cognomi) + '" ,  "' + random.choice(date_di_nascita) + '" ,  "' + random.choice(nazionalita) +'" )')


file_content.append("\nConto\n")
# Conto 

nomi_banche = [
    "JPMorgan Chase & Co.",
    "Bank of America",
    "Citibank",
    "Wells Fargo & Co.",
    "HSBC Holdings plc",
    "Deutsche Bank AG",
    "Barclays plc",
    "Credit Suisse Group AG",
    "BNP Paribas",
    "Mitsubishi UFJ Financial Group (MUFG)"
]

# Id conto
Codice_Univoco_Conto = []
for i in range(60):
    cf = generate_random_cf()[:10]
    while cf in Codice_Univoco_Conto:
        cf = generate_random_cf()[:10]
    
    Codice_Univoco_Conto.append(cf)
    

for i in range(40):
    file_content.append('( "' + Codice_Univoco_Conto[i] + '" ,  ' + str(round(random.random() + random.randrange(100000,1000000),2)) +  ' ,  "' + random.choice(nomi_banche) +'" )')


with open(file_name, 'w') as file:
    for line in file_content:
        file.write(line + '\n')