# EppTec - Mikhail Karimov
 Řešení naborového úkolu
 
## Původní zadání:

> ### a) Algoritmus
> Prosím napište algoritmus (jazyk volný), který ze seznamu vytřídí prvky podle nějakých pravidel, včetně příkladu takového pravidla. Tzn. ať je tam sekce, kam se doplní konkrétní pravidla, prvky budou někde mimo v seznamu, > který algoritmus projde a smaže hodnoty, které neprošly pravidly.

Řešení je ve složce [Algoritmus](https://github.com/karimmik/EppTec/tree/main/Algoritmus).

> ### b)  Datový model
> Vytvořte jednoduchý datový model obsahující 4 základní entity: Klient, Účet, Transakce a Balance.
> Naznačte základní sadu atributů v jednotlivých tabulkách, kardinalitu, primární/cizí klíče, apod.
> V tabulce transakcí se bude vyskytovat TYP_TRANSAKCE, který bude odkazovat do číselníku typů transakcí.
> Předpokládejte, že tabulka BALANCE obsahuje denní snímky nesoucí informaci o výši jednotlivých komponent pohledávky (jistina, úrok, poplatky) na konci dne.
> Postavte dotaz, který vybere všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit, že suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.
> Postavte dotaz, který zobrazí 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta) k ultimu měsíce a tuto na konci řádku vždy zobrazte.

Řešení je ve složce [Datový model](https://github.com/karimmik/EppTec/tree/main/Datov%C3%BD%20model).
