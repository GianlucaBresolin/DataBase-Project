--CREAZIONE TABELLE

CREATE TABLE Giocatore(
    Codice_Fiscale CHAR(16) PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Data_di_Nascita DATE NOT NULL,
    Nazionalità VARCHAR(255),
)

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
    Saldo_Reale FLOAT DEFAULT 0 CHECK (Saldo_Reale= ROUND(Saldo_Reale,2)), --RICORDO A MENNY DI CAMBIARE IMPORTO IN SALDO REALE NEL MOD. LOGICO
    CF_Giocatore CHAR(16) NOT NULL,

    PRIMARY KEY(ID_Saldo, ID_Casino),
    FOREIGN KEY(ID_Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE 
)

--QUERY


--POPOLAMENTO