import pandas as pd
import matplotlib.pyplot as plt
import calendar


url = "https://raw.githubusercontent.com/muminkoduje/Data_Analysis_Python/refs/heads/master/house_odcinki.csv"
dane = pd.read_csv(url)

liczba_odcinkow = len(dane)

print(f"Liczba odcinków: {liczba_odcinkow}")

liczba_sezonow = dane["Season"].nunique()

print(f"Liczba sezonów: {liczba_sezonow}")

naj_odc = dane.loc[dane["Rating"].idxmax(), "Episodes"]
naj_sez = dane.loc[dane["Rating"].idxmax(), "Season"]
naj_data = dane.loc[dane["Rating"].idxmax(), "Air_date"]

print(f"Najwyżej oceniany odcinek ma nazwę {naj_odc} \nWyszedł w sezonie {naj_sez} dnia {naj_data}")

dane["Air_date"] = pd.to_datetime(dane["Air_date"])

data_sort = dane.sort_values("Air_date")

pierwszy_odcinek = data_sort.iloc[0]
ostatni_odcinek = data_sort.iloc[-1]

print("Pierwszy odcinek:")
print(pierwszy_odcinek[["Episodes", "Air_date"]])

print("\nOstatni odcinek:")
print(ostatni_odcinek[["Air_date"]])

top_zebra = dane[["Zebra_score", "Episodes", "Final_diagnosis"]].sort_values(by="Zebra_score", ascending=False).head(20)

print(top_zebra)

dane_sezon1 = dane[dane["Season"] == 1]
dane_sezon1 = dane_sezon1.sort_values("Rating", ascending=False)


plt.scatter(dane_sezon1["Episodes"], dane_sezon1["Rating"], color="blue")
plt.title("Oceny odcinków – sezon 1")
plt.xlabel("Tytuł odcinka")
plt.ylabel("Ocena")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.style.use("ggplot")
plt.show()

sezony_ranking = dane[["Season", "Rating"]].groupby("Season", as_index=False).mean()
sezony_ranking = sezony_ranking.sort_values("Season")

plt.figure(figsize=(8, 6))
plt.plot(sezony_ranking["Season"], sezony_ranking["Rating"], marker="o", color="green")
plt.title("Ranking Sezonów wg średniej oceny")
plt.xlabel("Sezon")
plt.ylabel("Średnia Ocena")
plt.xticks(rotation=0)
plt.tight_layout()
plt.style.use("Solarize_Light2")
plt.show()

dane["Air_date"] = pd.to_datetime(dane["Air_date"])
dane["Year"] = dane["Air_date"].dt.year

odcinki_wg_roku = dane["Year"].value_counts().sort_index()

plt.figure(figsize=(8, 8))
odcinki_wg_roku.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=plt.cm.Paired.colors)
plt.title("Rozkład liczby odcinków wg roku wydania")
plt.ylabel("")
plt.tight_layout()
plt.style.use("ggplot")
plt.show()



odcinki_mies = dane["Month"].value_counts()
odcinki_mies_max = odcinki_mies.idxmax()
odcinki_liczba = odcinki_mies.max()

mies_nazwa = odcinki_mies_max
print(f"Miesiąc, w którym wyszło najwięcej odcinków: {mies_nazwa} ({odcinki_liczba} odcinków)")

odcinki_po_dniach = dane["Day_of_week"].value_counts()

najwiecej_odcinkow_dzien = odcinki_po_dniach.idxmax()
najwiecej_odcinkow = odcinki_po_dniach.max()

print(f"Dzień tygodnia, w którym wyszło najwięcej odcinków: {najwiecej_odcinkow_dzien} ({najwiecej_odcinkow} odcinków)")

odcinek_najgorszy = dane.loc[dane['Zebra_score'].idxmin()]

print(f"Odcinek z najgorszym wynikiem:")
print(f"Nazwa odcinka: {odcinek_najgorszy['Episodes']}")
print(f"Zebra_score: {odcinek_najgorszy['Zebra_score']}")
print(f"Choroba: {odcinek_najgorszy['Final_diagnosis']}")
print(f"Data emisji: {odcinek_najgorszy['Air_date']}")

dane["Air_date"] = pd.to_datetime(dane["Air_date"])

dane["Month"] = dane["Air_date"].dt.month
miesiace_oceny = dane.groupby("Month")["Rating"].mean()


plt.step(miesiace_oceny.index, miesiace_oceny.values, where="mid",
         color="orange", linewidth=2, label="Średnia ocena")
plt.title("Zmiana ocen w zależności od miesiąca")
plt.xlabel("Miesiąc")
plt.ylabel("Średnia ocena")
plt.legend(loc="upper left")
plt.style.use("fast")
plt.show()

dane["Air_date"] = pd.to_datetime(dane["Air_date"])
dane["Day"] = dane["Air_date"].dt.day
dane["Month"] = dane["Air_date"].dt.month


pier_paz = dane[(dane["Day"] == 1) & (dane["Month"] == 10)]

if  pier_paz.empty:
    print("Nie ma odcinków z 1 października.")
else:
    print("Odcinki z 1 października:")
    print(pier_paz[["Episodes", "Zebra_score", "Final_diagnosis"]])

rezyser_liczba = dane["Director"].value_counts()

rezyser_max = rezyser_liczba.idxmax()
rezyser_liczba = rezyser_liczba.max()

print("Reżyser, który pojawił się najwięcej razy:", rezyser_max)
print("Liczba wystąpień:", rezyser_liczba)

pisarze_zebrani= ["Writer", "Writer 1",
                  "Writer 2", "Writer 3", "Writer 4", "Writer 5"]
pisarze = dane[pisarze_zebrani].stack()

pisarze_zebrani = pisarze.value_counts()

duzo_pisarz = pisarze_zebrani.idxmax()
liczba_max = pisarze_zebrani.max()

malo_pisarz = pisarze_zebrani.idxmin()
liczba_min = pisarze_zebrani.min()

print("Pisarz, który pojawił się najwięcej razy:",duzo_pisarz)
print("Liczba wystąpień: ",liczba_max)


print("\nPisarz, który pojawił się najmniej razy:",malo_pisarz)
print("Liczba wystąpień: ",liczba_min)

rezyser_ranking = dane.groupby('Director')['Rating'].mean()
rezyser_najgorsi = rezyser_ranking.nsmallest(10)

plt.figure(figsize=(8, 6))
plt.plot(rezyser_najgorsi.index, rezyser_najgorsi.values,
         marker='o', color='red', linestyle='-', alpha=0.7)

plt.title("Top 10 najgorszych reżyserów wg średniej oceny odcinków")
plt.xlabel("Reżyser")
plt.ylabel("Średnia ocena")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(dane["Zebra_score"], dane["Rating"],
            color="pink", alpha=0.8, edgecolors="black",s=100)

plt.title("Zależność między zebra score a oceną odcinka", fontsize=16)
plt.xlabel("Zebra Score", fontsize=12)
plt.ylabel("Ocena odcinka", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
