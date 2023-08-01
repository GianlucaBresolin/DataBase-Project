--CREAZIONE TABELLE

CREATE TABLE Giocatore(
    Codice_Fiscale CHAR(16) PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Data_di_Nascita DATE NOT NULL,
    Nazionalità VARCHAR(255),
)

-- MENNY

CREATE TABLE Conto(
   ID_Conto VARCHAR(10) PRIMARY KEY,
   Importo DECIMAL(12,2) NOT NULL,
   Banca VARCHAR(255) NOT NULL,
)

CREATE TABLE ID_Casino(
   ID_Casino VARCHAR(30) PRIMARY KEY,
   Indirizzo VARCHAR(255) NOT NULL,
   Nazionalità VARCHAR(255) NOT NULL,
   Data_Apertura DATE NOT NULL,
   Conto VARCHAR(10) NOT NULL,

   FOREIGN KEY(Conto) REFERENCES Conto(ID_Conto) ON DELETE CASCADE
)

CREATE TABLE Gioco(
    ID_Gioco CHAR(10) PRIMARY KEY,
    Puntata_Minima DECIMAL(4,2) NOT NULL,
    Casino CHAR(10) NOT NULL,

    FOREIGN KEY(Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE
)

CREATE TABLE Poker(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Limite_Tavolo UNSIGNED INT NOT NULL, --CONTROLLARE SE ESISTE "UNSIGNED INT"

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
)

CREATE TABLE BlackJack(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Numero_Mazzi UNSIGNED INT NOT NULL, --CONTROLLARE SE ESISTE "UNSIGNED INT"
    Limite_Tavolo UNSIGNED INT NOT NULL, --CONTROLLARE SE ESISTE "UNSIGNED INT"

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
)

CREATE TABLE Roulette(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Moltiplicatore_Numero_Vincente DECIMAL(5,2) NOT NULL, --CONTROLLARE SE ESISTE "UNSIGNED INT"
    
    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
)

CREATE TABLE Slot(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Moltiplicatore_Massimo DECIMAL(5,2) NOT NULL, --CONTROLLARE SE ESISTE "UNSIGNED INT"
    Numero_Linee INT NOT NULL CHECK (Numero_Linee >= 2 AND Numero_Linee <= 10), 
    JackPot DECIMAL(6,2) , -- PUO' ESSERCI COME NO  

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
)

CREATE TABLE Giocata(
    ID_Gioco VARCHAR(10),
    CF_Giocatore VARCHAR(16),
    Importo FLOAT NOT NULL CHECK (Importo= ROUND(Importo,2)),
    Vincita DECIMAL(10,2),
    Data_Giocata DATE NOT NULL,
    Numero_Scommesso INT DEFAULT NULL CHECK (Numero_Scommesso >= 0 AND Numero_Scommesso <= 36), 
    Colore_Scommesso CHAR(1) DEFAULT NULL CHECK (Colore_Scommesso == 'R' OR Colore_Scommesso == 'B'), 

    PRIMARY KEY(ID_Gioco,CF_Giocatore),
    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE
)


-- GIAN

CREATE TABLE Scomessa(
    ID_Scommessa CHAR(10) PRIMARY KEY,
    Quota DECIMAL(4,2) NOT NULL,
    Data_Apertura DATE,
    Data_Chiusura DATE,
    Casino CHAR(10) NOT NULL,

    FOREIGN KEY(Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE
)

CREATE TABLE Scomessa_Cavallo(
    ID_Scommessa VARCHAR(10) PRIMARY KEY,
    Cavallo VARCHAR(255) NOT NULL,
    Gara VARCHAR(10) NOT NULL,

    FOREIGN KEY(ID_Scommessa) REFERENCES Scomessa(ID_Scommessa) ON DELETE CASCADE
)

CREATE TABLE Scomessa_Calcio(
    ID_Scommessa VARCHAR(10) PRIMARY KEY,
    Risultato VARCHAR(2) NOT NULL,
    Partita VARCHAR(255) NOT NULL,

    FOREIGN KEY(ID_Scommessa) REFERENCES Scomessa(ID_Scommessa) ON DELETE CASCADE
)

CREATE TABLE Effettuazione(
    ID_Scommessa VARCHAR(10),
    CF_Giocatore VARCHAR(16),
    Importo FLOAT NOT NULL CHECK (Importo= ROUND(Importo,2)),
    Esito BOOLEAN,
    Data_Effettuazione DATE NOT NULL,

    PRIMARY KEY(ID_Scommessa,CF_Giocatore),
    FOREIGN KEY(ID_Scommessa) REFERENCES Scomessa(ID_Scommessa) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE
)

CREATE TABLE Saldo(
    ID_Saldo VARCHAR(10),
    ID_Casino VARCHAR(10),
    Bonus FLOAT DEFAULT 0 CHECK (Bonus= ROUND(Bonus,2)),
    Saldo_Reale FLOAT DEFAULT 0 CHECK (Saldo_Reale= ROUND(Saldo_Reale,2)), --RICORDO A MENNY DI CAMBIARE IMPORTO IN SALDO REALE NEL MOD. LOGICO -- FATTO
    CF_Giocatore CHAR(16) NOT NULL,

    PRIMARY KEY(ID_Saldo, ID_Casino),
    FOREIGN KEY(ID_Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE 
)

--INDICI
CREATE INDEX indice_giocata_cf_giocatore ON Giocata USING hash(CF_Giocatore);
CREATE INDEX indice_data_giocata ON Giocata (Data_Giocata);

CREATE INDEX indice_importi_scommesse ON Effettuazione USING hash(CF_Giocatore);
CREATE INDEX indice_quote ON Scommesse(Quota);

--QUERY


--POPOLAMENTO