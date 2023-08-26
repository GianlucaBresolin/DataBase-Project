--CREAZIONE TABELLE

CREATE TABLE Giocatore(
    Codice_Fiscale CHAR(16) PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Data_di_Nascita DATE NOT NULL CHECK(EXTRACT(YEAR FROM Data_di_Nascita) < 2005),
    Nazionalita VARCHAR(255)
);

-- MENNY

CREATE TABLE Conto(
   ID_Conto VARCHAR(10) PRIMARY KEY,
   Importo DECIMAL(12,2) NOT NULL,
   Banca VARCHAR(255) NOT NULL
);

CREATE TABLE Casino(
   ID_Casino VARCHAR(30) PRIMARY KEY,
   Indirizzo VARCHAR(255) NOT NULL,
   Nazionalita VARCHAR(255) NOT NULL,
   Data_Apertura DATE NOT NULL,
   Conto VARCHAR(10) NOT NULL,

   FOREIGN KEY(Conto) REFERENCES Conto(ID_Conto) ON DELETE CASCADE
);

CREATE TABLE Gioco(
    ID_Gioco CHAR(10) PRIMARY KEY,
    Puntata_Minima DECIMAL(4,2) NOT NULL,
    Casino CHAR(30) NOT NULL,

    FOREIGN KEY(Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE
);

CREATE TABLE Poker(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Limite_Tavolo INT NOT NULL, 

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
);

CREATE TABLE BlackJack(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Numero_Mazzi INT NOT NULL, 
    Limite_Tavolo INT NOT NULL, 

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
);

CREATE TABLE Roulette(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Moltiplicatore_Numero_Vincente DECIMAL(5,2) NOT NULL, 
    
    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
);

CREATE TABLE Slot(
    ID_Gioco VARCHAR(10) PRIMARY KEY,
    Moltiplicatore_Massimo DECIMAL(5,2) NOT NULL, 
    Numero_Linee INT NOT NULL CHECK (Numero_Linee >= 2 AND Numero_Linee <= 10), 
    JackPot DECIMAL(10,2),   

    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE
);

CREATE TABLE Giocata(
    ID_Gioco VARCHAR(10),
    CF_Giocatore VARCHAR(16),
    Importo DECIMAL(10, 2) NOT NULL,
    Vincita DECIMAL(10,2),
    Data_Giocata DATE NOT NULL,
    Numero_Scommesso INT DEFAULT NULL CHECK (Numero_Scommesso >= 0 AND Numero_Scommesso <= 36), 
    Colore_Scommesso CHAR(1) DEFAULT NULL CHECK (Colore_Scommesso = 'R' OR Colore_Scommesso = 'B'), 

    PRIMARY KEY(ID_Gioco,CF_Giocatore),
    FOREIGN KEY(ID_Gioco) REFERENCES Gioco(ID_Gioco) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE
);


-- GIAN

CREATE TABLE Scommessa(
    ID_Scommessa CHAR(10) PRIMARY KEY,
    Quota DECIMAL(4,2) NOT NULL,
    Data_Apertura DATE,
    Data_Chiusura DATE,
    Casino CHAR(30) NOT NULL,

    FOREIGN KEY(Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE
);

CREATE TABLE Scommessa_Cavallo(
    ID_Scommessa VARCHAR(10) PRIMARY KEY,
    Cavallo VARCHAR(255) NOT NULL,
    Gara VARCHAR(20) NOT NULL,

    FOREIGN KEY(ID_Scommessa) REFERENCES Scommessa(ID_Scommessa) ON DELETE CASCADE
);

CREATE TABLE Scommessa_Calcio(
    ID_Scommessa VARCHAR(10) PRIMARY KEY,
    Risultato VARCHAR(2) NOT NULL,
    Partita VARCHAR(255) NOT NULL,

    FOREIGN KEY(ID_Scommessa) REFERENCES Scommessa(ID_Scommessa) ON DELETE CASCADE
);

CREATE TABLE Effettuazione(
    ID_Scommessa VARCHAR(10),
    CF_Giocatore VARCHAR(16),
    Importo DECIMAL(10,2) NOT NULL,
    Esito BOOLEAN,
    Data_Effettuazione DATE NOT NULL,

    PRIMARY KEY(ID_Scommessa,CF_Giocatore),
    FOREIGN KEY(ID_Scommessa) REFERENCES Scommessa(ID_Scommessa) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE
);

CREATE TABLE Saldo(
    ID_Saldo VARCHAR(10),
    ID_Casino VARCHAR(30),
    Bonus DECIMAL(10,2) DEFAULT 0,
    Saldo_Reale DECIMAL(10,2) DEFAULT 0,
    CF_Giocatore CHAR(16) NOT NULL,

    PRIMARY KEY(ID_Saldo, ID_Casino),
    FOREIGN KEY(ID_Casino) REFERENCES Casino(ID_Casino) ON DELETE CASCADE,
    FOREIGN KEY(CF_Giocatore) REFERENCES Giocatore(Codice_Fiscale) ON DELETE CASCADE 
);

--INDICI
CREATE INDEX indice_giocata_cf_giocatore ON Giocata USING hash(CF_Giocatore);
CREATE INDEX indice_data_giocata ON Giocata (Data_Giocata);

CREATE INDEX indice_importi_scommesse ON Effettuazione USING hash(CF_Giocatore);
CREATE INDEX indice_quote ON Scommessa(Quota);

--QUERY

--1 : Top 20 Vincite Scommesse Cavalli 
SELECT G.Nome, G.Cognome, E.Importo*Sc.Quota AS Vincita, S.Cavallo, S.Gara
FROM    ((Giocatore AS G 
        JOIN 
        Effettuazione AS E 
        ON G.Codice_Fiscale=E.CF_Giocatore)
        JOIN 
        Scommessa_Cavallo AS S 
        ON S.ID_Scommessa=E.ID_Scommessa)
        JOIN 
        Scommessa AS Sc
        ON S.ID_Scommessa=Sc.ID_Scommessa 
WHERE E.Esito=TRUE
ORDER BY Vincita DESC
LIMIT 20

--2 : Giocatori con Saldo Reale maggiore di 500€
SELECT DISTINCT G.Nome, G.Cognome, SUM(S.Saldo_Reale)
FROM    (Giocatore AS G
        JOIN
        Saldo AS S
        ON G.Codice_Fiscale=S.CF_Giocatore)
GROUP BY G.Nome, G.Cognome 
HAVING SUM(S.Saldo_Reale) > 500

--3 : Totale Scommesso nei Cavalli e in partite di Calcio da ogni giocatore 
SELECT G.Nome, G.Cognome, SUM(E.Importo) AS Tot_Scommesso
FROM    (Giocatore AS G
        JOIN 
        Effettuazione AS E
        ON G.Codice_Fiscale=E.CF_Giocatore)
GROUP BY G.Nome, G.Cognome        
ORDER BY Tot_Scommesso DESC

--4 : Top 20 Perdite in scommesse su partite di Calcio
SELECT G.Nome, G.Cognome, E.Importo AS Perdita, S.Risultato, S.Partita
FROM    (Giocatore AS G 
        JOIN 
        Effettuazione AS E 
        ON G.Codice_Fiscale=E.CF_Giocatore)
        JOIN 
        Scommessa_Calcio AS S 
        ON S.ID_Scommessa=E.ID_Gioco 
WHERE E.Esito=FALSE
ORDER BY Perdita DESC
LIMIT 20

--MENNY
--1 : Giocatori e rispettivo numero di giocate a poker in ordine decrescente tra il '2020-05-22' e il '2022-05-22'
SELECT G.Codice_Fiscale ,G.nome,  COUNT(*) AS Numero_Giocate
FROM Giocatore AS G
    JOIN Giocata AS J 
    ON G.Codice_Fiscale = J.CF_Giocatore
    JOIN Gioco AS O 
    ON O.ID_Gioco = J.ID_Gioco
    JOIN Poker AS P 
    ON P.ID_Gioco = O.ID_Gioco
    JOIN Casino AS C 
    ON O.Casino = C.ID_Casino
WHERE  J.Data_Giocata >= '2020-05-22' AND J.Data_Giocata <= '2022-05-22'
GROUP BY G.Codice_Fiscale , G.nome
ORDER BY Numero_Giocate DESC


--2 : Casino' e rispettivo numero di tavoli da poker che hanno in totale, che possiedono un conto superiore a 7.000.000 euro e con almeno un tavolo da poker avente il limite di giocatori maggiore di 7

SELECT DISTINCT C.ID_Casino, C.indirizzo, C.nazionalita , COUNT(P.ID_Gioco) as Numero_Tavoli
FROM ((Casino as C
	JOIN Conto as Co
	ON C.Conto = Co.ID_conto)
	JOIN Gioco as G
	ON C.ID_Casino  = G.casino)
    JOIN Poker as P
	ON G.ID_Gioco = P.ID_Gioco
WHERE Co.Importo >= 7000000 AND P.Limite_Tavolo > 7
GROUP BY C.ID_Casino, C.indirizzo, C.nazionalita



--3 : Casino' e numero di giocate alle slot di quel casino' tra il '2015/01/01' e il '2022/12/31'

SELECT  DISTINCT C.ID_Casino , C.indirizzo, C.nazionalita, COUNT(*) AS Numero_Giocate
FROM ((Casino as C
	JOIN Gioco as G 
ON C.ID_Casino  = G.casino)
	JOIN Slot as SL 
ON G.ID_Gioco = SL.ID_Gioco)
	JOIN Giocata as S 
ON SL.ID_Gioco  = S.ID_Gioco
WHERE S.Data_Giocata >= '2015/01/01'
AND S.Data_Giocata <= '2022/12/31'
GROUP BY C.ID_Casino, C.indirizzo, C.nazionalita

