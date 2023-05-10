# Datový model
  Zvolil jsem notací [fyzickou notace](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning?usecase=erd) ERD na vizualizace datového modelu. 
  
### Banka
  Mimo původního zadání jsem doplnil entitu Bank, která mně pomohla přípojít transakce k učtu pomocí dvou relací(*z učtu* a *do učtu*). Každá transakce bude mít odesílatele a odběratele, což umožní ušetřit místo a evidovat příchozí a výchozí transakce u klientů.
  
![](https://github.com/karimmik/EppTec/blob/main/Datov%C3%BD%20model/Bank%20model.png)

# SQL dotaz na klienty pro něž suma jistin na konci měsice je vetší než číslo c
Takový dotaz v MS SQL by mohl vypadat jako:
```
Select ClientID, 
       Name, 
       Surname,
       TotalAmount
  
  from (
       Select Account.ClientID as ClientID,
              SUM(CreditBalance.Amount) as TotalAmount
              
         from Account
   inner join CreditBalance on ( (CreditBalance.AcountID = Account.ID) and (EOMONTH(GETDATE()) = CreditBalance.Date) )
     group by Account.ID

  ) tmp 
  inner join Client on ( (Client.ID = tmp.ClientID) and (tmp.TotalAmount > c))
```

# SQL dotaz na 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta) k ultimu měsíce s zobrazením celkové výší pohledávky
Takový dotaz v MS SQL by mohl vypadat jako:
