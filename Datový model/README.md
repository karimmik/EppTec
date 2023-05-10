# Datový model
  Zvolil jsem notací [fyzickou notace](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning?usecase=erd) ERD na vizualizace datového modelu. 
  
### Banka
  Mimo původního zadání jsem doplnil entitu Bank, která mně pomohla přípojít transakce k učtu pomocí dvou relací(*z učtu* a *do učtu*). Každá transakce bude mít odesílatele a odběratele, což umožní ušetřit místo a evidovat příchozí a výchozí transakce u klientů.
  
![](https://github.com/karimmik/EppTec/blob/main/Datov%C3%BD%20model/Bank%20model.png)

> ## Postavte dotaz, který vybere všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit, že suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.
Takový dotaz v MS SQL by mohl vypadat jako:
```
Select ClientID, 
       Name, 
       Surname,
       TotalCreditAmount
  
  from (
       Select Account.ClientID as ClientID,
              SUM(CreditBalance.Amount) as TotalCreditAmount
              
         from Account
   inner join CreditBalance on ( (CreditBalance.AcountID = Account.ID) and (EOMONTH(GETDATE()) = CreditBalance.Date) )
     group by Account.ID

  ) tmp 
  inner join Client on ( (Client.ID = tmp.ClientID) and (tmp.TotalCreditAmount > c))
```

> ## Postavte dotaz, který zobrazí 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta) k ultimu měsíce a tuto na konci řádku vždy zobrazte.
Takový dotaz v MS SQL by mohl vypadat podobně za vyjimkou násobení částky procentem pohledávky a dodatečným setříděním:
```
Select TOP 10 
       ClientID, 
       Name, 
       Surname,
       TotalBruttoCreditAmount
  
  from (
       Select Account.ClientID as ClientID,
              SUM(CreditBalance.Amount * CreditBalance.Interest) as TotalBruttoCreditAmount
              
         from Account
   inner join CreditBalance on ( (CreditBalance.AcountID = Account.ID) and (EOMONTH(GETDATE()) = CreditBalance.Date) )
     group by Account.ID

  ) tmp 
  inner join Client on ( (Client.ID = tmp.ClientID) )
  order by TotalBruttoCreditAmount DESC
```
