import random
import string
from  datetime import *


#Cambiare virgolette e mettere le date virgolettate

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

def generate_random_casino():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1960, 2014)
    return f"{year}/{month:02d}/{day:02d}"

def generate_random_birthdate():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1960, 2001)
    return f"{year}/{month:02d}/{day:02d}"

def generate_random_cf():
    # Genera un codice fiscale casuale composto da 16 caratteri alfanumerici
    characters = string.ascii_uppercase + string.digits
    random_cf = ''.join(random.choices(characters, k=16))
    return random_cf

def generate_random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(2015, 2022)
    return datetime(year, month,day )


def generate_random_date_btw(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date



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
    Data_Apertura.append(generate_random_casino())

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
    while cs in Codice_Univoco_scommessa:
        cs = generate_random_cf()[:10]   
    Codice_Univoco_scommessa.append(cs)


Data_Apertura_scommessa = []
Data_Chiusura_scommessa = []
data_effettuazione = []
for i in range(500):
    data = generate_random_date()
    data_chiusura = (data + timedelta(days=3))
    data_effettuazione.append(generate_random_date_btw(data, data_chiusura).strftime("%Y/%m/%d"))
    Data_Apertura_scommessa.append((data.strftime("%Y/%m/%d")))
    Data_Chiusura_scommessa.append(data_chiusura.strftime("%Y/%m/%d") )

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

match_names = [
    "Milan vs Inter",
    "Barcelona vs Real",
    "Liverpool vs ManUtd",
    "Juventus vs Napoli",
    "Bayern vs Dortmund",
    "Chelsea vs Arsenal",
    "PSG vs Marseille",
    "City vs Spurs",
    "Atletico vs Real",
    "Roma vs Lazio",
    "Ajax vs Feyenoord",
    "Benfica vs Porto",
    "Boca vs River",
    "Flamengo vs Fluminense",
    "Celtic vs Rangers",
    "Galatasaray vs Fenerbahce",
    "Everton vs Liverpool",
    "Palmeiras vs SaoPaulo",
    "Lyon vs Marseille",
    "Borussia vs Schalke",
    "Sevilla vs Betis",
    "Milan vs Roma",
    "Barcelona vs Atletico",
    "Liverpool vs Everton",
    "Inter vs Juventus",
    "Dortmund vs Schalke",
    "ManUtd vs ManCity",
    "Chelsea vs Tottenham",
    "Real vs Sevilla",
    "Napoli vs Fiorentina",
    "Boca vs Independiente",
    "Flamengo vs Botafogo",
    "River vs SanLorenzo",
    "Celtic vs Hearts",
    "Porto vs Sporting",
    "Ajax vs PSV",
    "Benfica vs Braga",
    "Rangers vs Aberdeen",
    "Fenerbahce vs Besiktas",
    "Palmeiras vs Corinthians",
    "SaoPaulo vs Santos",
    "Lyon vs PSG",
    "Borussia vs Leverkusen",
    "Milan vs Napoli",
    "Barcelona vs Valencia",
    "Liverpool vs Chelsea",
    "Inter vs Lazio",
    "Dortmund vs Bayern",
    "ManUtd vs Arsenal",
    "Real vs Atletico",
    "Tottenham vs City",
    "Sevilla vs Valencia",
    "Roma vs Inter",
    "Juventus vs Milan",
    "Schalke vs Leverkusen",
    "Barcelona vs Sevilla",
    "Liverpool vs Tottenham",
    "Chelsea vs ManCity",
    "Atletico vs Valencia",
    "Napoli vs Juventus",
    "Boca vs SanLorenzo",
    "Flamengo vs Vasco",
    "River vs Racing",
    "Celtic vs Hibernian",
    "Porto vs RioAve",
    "Ajax vs Feyenoord",
    "Benfica vs Sporting",
    "Rangers vs Celtic",
    "Besiktas vs Galatasaray",
    "Santos vs Corinthians",
    "Palmeiras vs Flamengo",
    "Lyon vs Bordeaux",
    "Borussia vs Frankfurt",
    "Milan vs Lazio",
    "Barcelona vs RealSociedad",
    "Liverpool vs Newcastle",
    "Inter vs Roma",
    "Dortmund vs Leipzig",
    "ManUtd vs Chelsea",
    "Real vs Villarreal",
    "Napoli vs Inter",
    "Boca vs Racing",
    "Flamengo vs Gremio",
    "River vs Independiente",
    "Celtic vs Aberdeen",
    "Porto vs Benfica",
    "Ajax vs Utrecht",
    "Sporting vs Braga",
    "Rangers vs Hearts",
    "Fenerbahce vs Trabzonspor",
    "Palmeiras vs Santos",
    "SaoPaulo vs Flamengo",
    "Lyon vs Nice",
    "Borussia vs Wolfsburg"
]
#----------------------------------------------------------------



# Id saldo
Codice_Univoco_Saldo = []
for i in range(250):
    sc = generate_random_cf()[:10]
    while sc in Codice_Univoco_Saldo:
        sc = generate_random_cf()[:10]   
    Codice_Univoco_Saldo.append(sc)

#----------------------------------------------------------------

# 
Codice_Univoco_ID_Gioco = []
for i in range(280):
    cg = generate_random_cf()[:10]
    while cg in Codice_Univoco_ID_Gioco:
        cg = generate_random_cf()[:10]   
    Codice_Univoco_ID_Gioco.append(cg)


Codice_Univoco_scommessa_Effetuazione = []
codici_fiscali_effettuazione = []
Codice_Univoco_ID_Gioco_giocata = []
codici_fiscali_giocata = []

##DA RIVEDERE
def trova_indici_elemento_eff(elemento):
    indici = []
    for indice, valore in enumerate(Codice_Univoco_scommessa_Effetuazione):
        if valore == elemento:
            indici.append(indice)

    tmp = []
    for indice in indici:
        tmp.append(codici_fiscali_effettuazione[indice])
    return tmp

def trova_indici_elemento_gioca(elemento):
    indici = []
    for indice, valore in enumerate(Codice_Univoco_ID_Gioco_giocata):
        if valore == elemento:
            indici.append(indice)

    tmp = []
    for indice in indici:
        tmp.append(codici_fiscali_giocata[indice])
    return tmp

for i in range(500):
    Codice_Univoco_scommessa_Effetuazione.append(random.choice(Codice_Univoco_scommessa))
    codici_fiscali_effettuazione_tmp = random.choice(codici_fiscali)
    while codici_fiscali_effettuazione_tmp in trova_indici_elemento_eff(Codice_Univoco_scommessa_Effetuazione[i]):
        codici_fiscali_effettuazione_tmp = random.choice(codici_fiscali)
    codici_fiscali_effettuazione.append(random.choice(codici_fiscali))

for i in range(500):
    Codice_Univoco_ID_Gioco_giocata.append(random.choice(Codice_Univoco_ID_Gioco))
    codici_fiscali_giocata_tmp = random.choice(codici_fiscali)
    while codici_fiscali_giocata_tmp in trova_indici_elemento_gioca(Codice_Univoco_ID_Gioco_giocata[i]):
        codici_fiscali_giocata_tmp = random.choice(codici_fiscali)
    codici_fiscali_giocata.append(random.choice(codici_fiscali))
##DA RIVEDERE

Codice_Univoco_ID_Gioco_poker = Codice_Univoco_ID_Gioco[:70]
Codice_Univoco_ID_Gioco_blackjack = Codice_Univoco_ID_Gioco[70:140]
Codice_Univoco_ID_Gioco_Roulette = Codice_Univoco_ID_Gioco[140:210]
Codice_Univoco_ID_Gioco_Slot = Codice_Univoco_ID_Gioco[210:280]

numeri_jackpot = [
    50000,
    100000,
    250000,
    300000,
    450000,
    500000,
    750000,
    800000,
    900000,
    950000,
    0
]

Data_giocata = []
for i in range(500):
    Data_giocata.append(generate_random_date())



#----------------------------------------------------------------

#Giocatore
file_content.append("INSERT INTO Giocatore(Codice_Fiscale, Nome, Cognome, Data_di_Nascita, Nazionalita) VALUES \n")
for i in range(200):
    file_content.append('( "' + codici_fiscali[i] + '" ,  "' + random.choice(nomi) +  '" ,  "' + random.choice(cognomi) + '" ,  "' + random.choice(date_di_nascita) + '" ,  "' + random.choice(nazionalita) +'" )')
    if i != 199:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")


#CONTO
file_content.append("INSERT INTO Conto(ID_Conto, Importo, Banca) VALUES \n")
for i in range(50):
    file_content.append('( "' + Codice_Univoco_Conto[i] + '" ,  ' + str(round(random.uniform(800000, 8000000), 2)) +  ' ,  "' + random.choice(nomi_banche) +'" )')
    if i != 49:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

# Casino
file_content.append("INSERT INTO Casino(ID_Casino, Indirizzo, Nazionalita, Data_Apertura, Conto) VALUES \n")
for i in range(50):
    file_content.append('( "' + casino_nomi[i] + '" ,  "' + indirizzi_casino[i] +  '" ,  "' + random.choice(nazionalita) +  '" ,  "' + random.choice(Data_Apertura) +'" ,  "' + Codice_Univoco_Conto[i]+'")')
    if i != 49:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Scommessa 
file_content.append("INSERT INTO Scomessa(ID_Scommessa, Quota, Data_Apertura, Data_Chiusura, Casino) VALUES \n")
for i in range(300):
    file_content.append('( "' + Codice_Univoco_scommessa[i] + '" ,  ' + str(round(random.uniform(0.5, 20.0), 2)) +  ' ,  "' + Data_Apertura_scommessa[i]+  '" ,  "' + Data_Chiusura_scommessa[i] +'" ,  "' + random.choice(casino_nomi) +'")')
    if i != 299:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Scommessa_Cavallo
file_content.append("INSERT INTO Scomessa_Cavallo(ID_Scommessa, Cavallo, Gara) VALUES \n")
for i in range(150):
    file_content.append('( "' + Codice_Univoco_scommessa_Cavallo[i] + '" ,  "' + random.choice(nomi_cavallo) +  '" ,  "' + random.choice(nomi_gare) +  '")')
    if i != 149:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Scommessa_Calcio
file_content.append("INSERT INTO Scomessa_Calcio(ID_Scommessa, Risultato, Partita) VALUES \n")
for i in range(150):
    file_content.append('( "' + Codice_Univoco_scommessa_Calcio[i] + '" ,  "' + str(random.randint(0, 4)) + " " + str(random.randint(0, 4))  + '" ,  "' + random.choice(match_names) +  '")')
    if i != 149:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Effettuazione 
file_content.append("INSERT INTO Effettuazione(ID_Scommessa, CF_Giocatore, Importo, Esito, Data_Effettuazione) VALUES \n")
for i in range(500):
    file_content.append('( "' + Codice_Univoco_scommessa_Effetuazione[i] + '" ,  "' + codici_fiscali_effettuazione[i] +  '" ,  ' +  str(round(random.uniform(10, 10000), 2))  +  ' ,  ' + str(random.choice([True, False])) +' ,  "' + data_effettuazione[i] +'")')
    if i != 499:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Saldo 
file_content.append("INSERT INTO Saldo(ID_Saldo, ID_Casino, Bonus, Saldo_Reale, CF_Giocatore) VALUES \n")
for i in range(250):
    file_content.append('( "' + Codice_Univoco_Saldo[i] + '" ,  "' + random.choice(casino_nomi) +  '" ,  ' +  str(round(random.uniform(0, 5000), 2))  +  ' ,  ' + str(round(random.uniform(0, 100000), 2)) +' ,  "' + random.choice(codici_fiscali) +'")')
    if i != 249:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Gioco
file_content.append("INSERT INTO Gioco(ID_Gioco, Puntata_Minima, Casino) VALUES \n")
for i in range(280):
    file_content.append('( "' + Codice_Univoco_ID_Gioco[i] + '" ,  ' + str(random.randint(1, 10)) +  ' ,  "' + random.choice(casino_nomi) +'" )')
    if i != 279:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")


#Poker
file_content.append("INSERT INTO Poker(ID_Gioco, Limite_Tavolo) VALUES \n")
for i in range(70):
    file_content.append('( "' + Codice_Univoco_ID_Gioco_poker[i] + '" ,  ' + str(random.randint(6, 12)) +  ' )')
    if i != 69:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#BlackJack
file_content.append("INSERT INTO BlackJack(ID_Gioco, Numero_Mazzi, Limite_Tavolo) VALUES \n")
for i in range(70):
    file_content.append('( "' + Codice_Univoco_ID_Gioco_blackjack[i] + '" ,  ' + str(random.randint(1, 4)) +  ', ' + str(random.randint(4,8)) + ')')
    if i != 69:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Roulette
file_content.append("INSERT INTO Roulette(ID_Gioco, Moltiplicatore_Numero_Vincente) VALUES \n")
for i in range(70):
    file_content.append('( "' + Codice_Univoco_ID_Gioco_Roulette[i] + '" ,  ' + str(random.uniform(1, 500)) + ')')
    if i != 69:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Slot
file_content.append("INSERT INTO Slot(ID_Gioco, Moltiplicatore_Massimo, Numero_Linee , JackPot) VALUES \n")
for i in range(70):
    file_content.append('( "' + Codice_Univoco_ID_Gioco_Slot[i] + '" ,  ' + str(random.uniform(1, 100)) +  ', ' + str(random.randint(2,10)) +  ', ' + str(random.choice(numeri_jackpot)) + ')')
    if i != 69:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")

#Giocata
file_content.append("INSERT INTO Giocata(ID_Gioco, CF_Giocatore, Importo, Vincita , Data_Giocata ,Numero_Scommesso, Colore_Scommesso  ) VALUES \n")
for i in range(500):
    if  Codice_Univoco_ID_Gioco_giocata[i] in Codice_Univoco_ID_Gioco_Roulette:
        file_content.append('( "' + Codice_Univoco_ID_Gioco_giocata[i] + '" ,  "' + codici_fiscali_giocata[i] +  '" ,  ' +  str(round(random.uniform(10, 10000), 2))  +  ' ,  ' + str(random.randint(0,1000000)) +' ,  "' + Data_giocata[i] + '" , ' +  str(random.randint(0, 36)) + '  , "' + random.choice(['R' , 'B']) + '")')
    else:
        file_content.append('( "' + Codice_Univoco_ID_Gioco_giocata[i] + '" ,  "' + codici_fiscali_giocata[i] +  '" ,  ' +  str(round(random.uniform(10, 10000), 2))  +  ' ,  ' + str(random.randint(0,1000000)) +' ,  "' + Data_giocata[i] +'")')
    if i != 499:
        file_content.append(',\n')
file_content.append(";\n\n\n\n")



with open(file_name, 'w') as file:
    for line in file_content:
        file.write(line)
