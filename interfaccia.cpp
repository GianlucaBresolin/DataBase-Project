#include <cstdio>
#include <iostream>
#include <fstream>
#include "dependencies/include/libpq-fe.h"

#define PG_HOST "127.0.0.1" 
#define PG_USER "postgres" 
#define PG_DB "CASINO"
#define PG_PASS "Sansone1" 
#define PG_PORT 5432

using namespace std ;

void checkResults(PGresult* res, const PGconn* conn){
    if(PQresultStatus(res)!=PGRES_TUPLES_OK){
        cout<<"Risultati inconsistenti!"<<PQerrorMessage(conn)<<endl;
        PQclear(res);
        exit(1);
    }
}

int main(int argc, char** argv){
    PGconn* conn;
    char conninfo [250];
    sprintf(conninfo , "user=%s password=%s dbname=%s hostaddr=%s port=%d", PG_USER, PG_PASS, PG_DB, PG_HOST, PG_PORT);
    conn=PQconnectdb(conninfo);

    if(PQstatus(conn) != CONNECTION_OK){
        cout<<"Errore di connessione"<<PQerrorMessage(conn);
        PQfinish(conn);
        exit(1);
    }
    else{
        cout<<"\nConnessione avvenuta correttamente\n";    
    }

    bool flag=true;

    while(flag){
        cout<<"\nQuery disponibili:\n";
        cout<<"\t1. Top 20 Vincite Scommesse Cavalli\n";
        cout<<"\t2. Giocatori con Saldo Reale maggiore di 500 euro\n";
        cout<<"\t3. Totale Scommesso nei Cavalli e in partite di Calcio da ogni giocatore\n";
        cout<<"\t4. Top 20 Perdite in scommesse su partite di Calcio\n";
        cout<<"\t5. ";
        cout<<"\t6. ";
        cout<<"\t7. ";
        cout<<"\tDEFAULT: CLOSE INTERFACE\n";

        cout<<"\nInserisci il numero della query che vuoi eseguire:\n";
        int x;
        cin>>x;

        PGresult *res;
        int tuple;
        int campi;

        switch(x){
            case 1:
                res=PQexec(conn, "SELECT G.Nome, G.Cognome, E.Importo*S.Quota AS Vincita, S.Cavallo, S.Gara FROM (Giocatore AS G JOIN Effettuazione AS E ON G.Codice_Fiscale=E.CF_Giocatore) JOIN Scommesse_Cavallo AS S ON S.ID_Scommessa=E.ID_Gioco WHERE E.Esito=TRUE ORDER BY Vincita DESC LIMIT 20");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 2:
                res=PQexec(conn, "SELECT G.Nome, G.Cognome, SUM(S.Saldo_Reale) FROM (Giocatore AS G JOIN Saldo AS S ON G.Codice_Fiscale=S.CF_Giocatore) GROUP BY G.Nome, G.Cognome HAVING SUM(S.Saldo_Reale) > 500");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 3:
                res=PQexec(conn, "SELECT G.Nome, G.Cognome, SUM(E.Importo) AS Tot_Scommesso FROM (Giocatore AS G JOIN Effettuazione AS E ON G.Codice_Fiscale=E.CF_Giocatore) GROUP BY G.Nome,G.Cognome ORDER BY Tot_Scommesso DESC");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 4:
                res=PQexec(conn, "SELECT G.Nome, G.Cognome, E.Importo AS Perdita, S.Risultato, S.Partita FROM (Giocatore AS G JOIN Effettuazione AS E ON G.Codice_Fiscale=E.CF_Giocatore) JOIN Scommessa_Calcio AS S ON S.ID_Scommessa=E.ID_Gioco WHERE E.Esito=FALSE ORDER BY Perdita DESC LIMIT 20");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 5:
                res=PQexec(conn, "SELECT G.Codice_Fiscale, G.Nome, G.Cognome FROM  (Giocatore as G JOIN Giocata as J ON G.Codice_Fiscale = J.CF_Giocatore ) JOIN Poker as P ON J.ID_Gioco = P.ID_Gioco JOIN Gioco as O ON O.ID_Gioco = P.ID_Gioco JOIN Casino as C ON O.Casino = C.ID_Casino WHERE C.Nazionalita = 'Australiana';");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 6:
                res=PQexec(conn, "SELECT C.ID_Casino, C.indirizzo, C.nazionalita , COUNT(P.ID_Gioco) as Numero_Tavoli FROM (Casino as C JOIN Conto as Co ON C.Conto = Co.Id_conto JOIN Gioco as G ON C.ID_Casino = G.casino JOIN Poker as P ON G.ID_Gioco = P.ID_Gioco) WHERE (Co.Importo >= 7000000 AND P.Limite_Tavolo > 7) GROUP BY C.ID_Casino, C.indirizzo, C.nazionalita");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            case 7:
                res=PQexec(conn, "SELECT C.ID_Casino , C.indirizzo, C.nazionalita, COUNT(*) AS Numero_Giocate FROM (Casino as C JOIN Gioco as G ON C.ID_Casino  = G.casino JOIN Slot as SL ON G.ID_Gioco = SL.ID_Gioco JOIN Giocata as S ON SL.ID_Gioco  = S.ID_Gioco) WHERE S.Data_Giocata >= '2015/05/22' AND S.Data_Giocata <= '2022/05/22' GROUP BY C.ID_Casino, C.indirizzo, C.nazionalita;");
                checkResults(res, conn);

                tuple=PQntuples(res); //prende il # di tuple
                campi=PQnfields(res); //prende il # di fields

                //Stampo intestazioni
                for(int i=0; i<campi; ++i){
                    cout<<PQfname(res,i)<<"\t\t"; //prende il nome del field in posizione i
                }
                cout<<endl;

                //Stampa i valori selezionati
                for(int i=0; i<tuple; ++i){
                    for(int j=0; j<campi; ++j){
                        cout<<PQgetvalue(res, i, j)<<"\t\t"; //prende il valore del field in posizione j alla tupla #i
                    }
                    cout<<endl;
                }

                PQclear(res); //pulisce il risultato
                break;
            default:
                flag=false;
                break;
        }
    }

    PQfinish(conn); //chiude la connessione

    return 0;
}