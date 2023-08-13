import random
import string
from  datetime import *

file_name = "tabellaGiocatori.txt"

file_content = []

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
    return f"{year}/{month:02d}/{day:02d}"

def generate_random_cf():
    # Genera un codice fiscale casuale composto da 16 caratteri alfanumerici
    characters = string.ascii_uppercase + string.digits
    random_cf = ''.join(random.choices(characters, k=16))
    return random_cf

def generate_random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1990, 2022)
    return datetime(year, month,day )

date_di_nascita = []

while len(date_di_nascita) < 50:
    birthdate = generate_random_birthdate()
    date_di_nascita.append(birthdate)

nazionalita = [
    "Italiana",
    "Statunitense",
    "Francese",
    "Spagnola",
    "Canadese",
    "Britannica",
    "Tedesca",
    "Australiana",
    "Austriaca",
    "Portoghese",
    "Giapponese",
    "Cinese",
    "Messicana",
    "Brasiliana",
    "Sudafricana"
]


codici_fiscali = []
for i in range(200):
    cf = generate_random_cf()
    while cf in codici_fiscali:
        cf = generate_random_cf()
    
    codici_fiscali.append(cf)


#----------------------------------------------------------------


file_content.append(";\n\n")
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
for i in range(50):
    cc = generate_random_cf()[:10]
    while cc in Codice_Univoco_Conto:
        cc = generate_random_cf()[:10]   
    Codice_Univoco_Conto.append(cc)



#----------------------------------------------------------------


casino_nomi = [
    "Lucky Spin Casino",
    "Golden Palace",
    "Starlight Casino",
    "Fortune Plaza",
    "Royal Dice",
    "Silver Sands",
    "Emerald Casino",
    "Vegas Lights",
    "Ocean Jewel",
    "Sunrise Casino",
    "Moonlit Cove",
    "Crystal Casino",
    "Palm Grove",
    "Crown Jewel",
    "Pearl Bay",
    "Desert Oasis",
    "Lucky Clover",
    "Neon Nights",
    "Royal Flush",
    "Emerald Isle",
    "Wild West",
    "Sunset Strip",
    "Golden Gate",
    "Treasure Cove",
    "Diamond Edge",
    "Blue Horizon",
    "Red Lantern",
    "Sapphire Sky",
    "Mystic Mirage",
    "Lucky Star",
    "Rainbow Resort",
    "Silver Stream",
    "Crystal Peak",
    "Sunset Sands",
    "Vegas Mirage",
    "Starshine",
    "Dreamland Casino",
    "Skyline Gaming",
    "Crimson Casino",
    "Mystic Oasis",
    "Azure Sands",
    "Treasure Island",
    "Ruby Ridge",
    "Neon Dreams",
    "Golden Arrow",
    "Moonlit Magic",
    "Lucky Charm",
    "Jade Palace",
    "Crystal Cove",
    "Emerald Star",
    "Sunset Plaza"
]



Data_Apertura = []

for i in range(50):
    Data_Apertura.append(generate_random_birthdate())

indirizzi_casino = [
    "Via del Sole",
    "Oak Street",
    "Rue de la Lune",
    "Calle Primavera",
    "Maple Avenue",
    "Elm Drive",
    "Hauptstraße",
    "Via Roma",
    "Fifth Avenue",
    "Champs-Élysées",
    "Calle de la Playa",
    "Birch Lane",
    "Baker Street",
    "Hauptplatz",
    "Piazza San Marco",
    "Central Park West",
    "Seine Quai",
    "La Rambla",
    "Harbour Street",
    "King's Road",
    "Alexanderplatz",
    "Piazza Navona",
    "Broadway",
    "Louvre Rue",
    "Ramblas",
    "Bondi Beach Road",
    "Oxford Street",
    "Kurfürstendamm",
    "San Marco Plaza",
    "Times Square",
    "Champs-Élysées",
    "Las Ramblas",
    "Harbour Bridge Street",
    "Baker Street",
    "Rathausplatz",
    "Colosseum Avenue",
    "Central Park West",
    "Seine Quai",
    "Sagrada Familia Avenue",
    "Bondi Beach Road",
    "Abbey Road",
    "Brandenburg Gate Platz",
    "Piazza di Spagna",
    "Broadway",
    "Eiffel Tower Lane",
    "Park Güell Street",
    "Opera House Avenue",
    "Baker Street",
    "Hofburggasse",
    "Vatican Square",
    "Central Park West"
]


#----------------------------------------------------------------

Codice_Univoco_scommessa = []
for i in range(300):
    cs = generate_random_cf()[:10]
    while cs in Codice_Univoco_Conto:
        cs = generate_random_cf()[:10]   
    Codice_Univoco_scommessa.append(cs)


Data_Apertura_scommessa = []
Data_Chiusura_scommessa = []

for i in range(300):
    data = generate_random_date()
    Data_Apertura_scommessa.append((data.strftime("%Y/%m/%d")))
    Data_Chiusura_scommessa.append((data + timedelta(days=3)).strftime("%Y/%m/%d") )

#----------------------------------------------------------------

Codice_Univoco_scommessa_Cavallo = Codice_Univoco_scommessa[:150]

Codice_Univoco_scommessa_Calcio = Codice_Univoco_scommessa[150:]

nomi_cavallo = [
    "Thunderbolt",
    "Midnight Shadow",
    "Silver Arrow",
    "Golden Hoof",
    "Rapid Runner",
    "Moonlight Majesty",
    "Dashing Dare",
    "Starstruck",
    "Whispering Wind",
    "Firestorm",
    "Galactic Gait",
    "Mystic Mirage",
    "Crimson Comet",
    "Royal Racer",
    "Velvet Vortex",
    "Sapphire Sprint",
    "Emerald Express",
    "Wild Mustang",
    "Bolted Beauty",
    "Sleek Stallion",
    "Graceful Gallop",
    "Knight Rider",
    "Pegasus Pride",
    "Stormy Sky",
    "Dreamcatcher",
    "Marble Majesty",
    "Silver Streak",
    "Amber Blaze",
    "Golden Gallop",
    "Silent Serenity",
    "Swift Spirit",
    "Moonlit Marvel",
    "Scarlet Speedster",
    "Victory Verve",
    "Majestic Mane",
    "Phoenix Flight",
    "Ebon Echo",
    "Jade Jumper",
    "Copper Charge",
    "Whirlwind Wonder",
    "Diamond Dash",
    "Quicksilver",
    "Enchanted Equine",
    "Cosmic Canter",
    "Rustic Rocket",
    "Aurora Borealis",
    "Brilliant Blaze",
    "Radiant Runner",
    "Galaxy Glide",
    "Lunar Lope",
    "Crimson Canter"
]


nomi_gare = [
    "Swift Sprint",
    "Golden Derby",
    "Silver Stakes",
    "Crystal Classic",
    "Emerald Run",
    "Ruby Rumble",
    "Moonlit Mile",
    "Sunset Showdown",
    "Thunder Trot",
    "Dusk Dash",
    "Dawn Derby",
    "Mystic Marathon",
    "Starshine Sprint",
    "Crimson Challenge",
    "Velvet Victory",
    "Azure Affair",
    "Royal Rumble",
    "Galactic Gala",
    "Diamond Dash",
    "Amber Ascend",
    "Whirlwind Whisk",
    "Sapphire Stampede",
    "Neon Nudge",
    "Jade Jamboree",
    "Lunar Lope",
    "Firefly Fling",
    "Rustic Race",
    "Pegasus Pursuit",
    "Ebon Encounter",
    "Silent Sweep",
    "Scarlet Showcase",
    "Aurora Affair",
    "Bolted Blaze",
    "Enchanted Endurance",
    "Copper Canter",
    "Quicksilver Quest",
    "Stormy Stride",
    "Marble March",
    "Majestic Mayhem",
    "Whispering Whisk",
    "Wild Wager",
    "Phoenix Phantasm",
    "Dreamland Duel",
    "Rapid Rally",
    "Treasure Trot",
    "Graceful Gallop",
    "Knightly Knockout",
    "Rapidfire Run",
    "Daring Dash",
    "Sleek Scurry",
    "Meadow Marathon",
    "Lively Lope",
    "Moonbeam Maneuver",
    "Firelight Flight",
    "Golden Glide",
    "Silent Showdown",
    "Ebon Echelon",
    "Stellar Stakes",
    "Starstruck Stride",
    "Crimson Canter",
    "Velvet Victory",
    "Amber Ambush",
    "Neon Nimble",
    "Pegasus Pursuit",
    "Sapphire Sprint",
    "Mystic Marathon",
    "Emerald Escapade",
    "Diamond Derby",
    "Quicksilver Quest",
    "Scarlet Showdown",
    "Golden Gallop",
    "Silver Sprint",
    "Royal Rumble",
    "Stormy Stride",
    "Lunar Lap",
    "Majestic Mile",
    "Dusk Dash",
    "Dawn Derby",
    "Crystal Challenge",
    "Firelight Fling",
    "Moonlit Marathon",
    "Sleek Sweep",
    "Copper Canter"
]


#Giocatore
file_content.append("INSERT INTO Giocatore(Codice_Fiscale, Nome, Cognome, Data_di_Nascita, Nazionalita) VALUES ")
for i in range(200):
    file_content.append('( "' + codici_fiscali[i] + '" ,  "' + random.choice(nomi) +  '" ,  "' + random.choice(cognomi) + '" ,  "' + random.choice(date_di_nascita) + '" ,  "' + random.choice(nazionalita) +'" )')
    if i != 199:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")


#CONTO
file_content.append("INSERT INTO Conto(ID_Conto, Importo, Banca) VALUES ")
for i in range(50):
    file_content.append('( "' + Codice_Univoco_Conto[i] + '" ,  ' + str(round(random.uniform(800000, 8000000), 2)) +  ' ,  "' + random.choice(nomi_banche) +'" )')
    if i != 49:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

# Casino
file_content.append("INSERT INTO Casino(ID_Casino, Indirizzo, Nazionalita, Data_Apertura, Conto) VALUES ")
for i in range(50):
    file_content.append('( "' + casino_nomi[i] + '" ,  "' + indirizzi_casino[i] +  '" ,  "' + random.choice(nazionalita) +  '" ,  "' + random.choice(Data_Apertura) +'" ,  "' + Codice_Univoco_Conto[i]+'")')
    if i != 49:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Scommessa 
file_content.append("INSERT INTO Scomessa(ID_Scommessa, Quota, Data_Apertura, Data_Chiusura, Casino) VALUES ")
for i in range(300):
    file_content.append('( "' + Codice_Univoco_scommessa[i] + '" ,  ' + str(round(random.uniform(0.5, 20.0), 2)) +  ' ,  "' + Data_Apertura_scommessa[i]+  '" ,  "' + Data_Chiusura_scommessa[i] +'" ,  "' + random.choice(casino_nomi) +'")')
    if i != 79:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Scommessa_Cavallo
file_content.append("INSERT INTO Scomessa_Cavallo(ID_Scommessa, Cavallo, Gara) VALUES ")
for i in range(150):
    file_content.append('( "' + Codice_Univoco_scommessa_Cavallo[i] + '" ,  "' + random.choice(nomi_cavallo) +  '" ,  "' + random.choice(nomi_gare) +  '")')
    if i != 79:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")



with open(file_name, 'w') as file:
    for line in file_content:
        file.write(line)