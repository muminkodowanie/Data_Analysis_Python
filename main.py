import pandas as pd
import matplotlib.pyplot as plt
import calendar

plt.style.use("ggplot")
url = "https://raw.githubusercontent.com/muminkodowanie/Data_Analysis_Python/refs/heads/master/house_odcinki.csv"
dane = pd.read_csv(url)


dane["Air_date"] = pd.to_datetime(dane["Air_date"])
dane["Month"] = dane["Air_date"].dt.month
dane["Day_of_week"] = dane["Air_date"].dt.day_name()
dane["Year"] = dane["Air_date"].dt.year
dane["Day"] = dane["Air_date"].dt.day


print(f"Liczba odcinków: {len(dane)}")
print(f"Liczba sezonów: {dane['Season'].nunique()}")


naj_odc = dane.loc[dane["Rating"].idxmax()]
print(f"Najwyżej oceniany odcinek: {naj_odc['Episodes']} (Sezon {naj_odc['Season']}, {naj_odc['Air_date'].date()})")


print("\nPierwszy odcinek:")
print(dane.sort_values("Air_date").iloc[0][["Episodes", "Air_date"]])
print("\nOstatni odcinek:")
print(dane.sort_values("Air_date").iloc[-1][["Episodes", "Air_date"]])


print("\nTop 20 Zebra Score:")
print(dane.sort_values("Zebra_score", ascending=False)[["Zebra_score", "Episodes", "Final_diagnosis"]].head(20))

dane_sezon1 = dane[dane["Season"] == 1].sort_values("Rating", ascending=False)
plt.figure(figsize=(10, 5))
plt.scatter(dane_sezon1["Episodes"], dane_sezon1["Rating"], color="skyblue", edgecolors="black", s=100)
plt.title("Oceny odcinków – Sezon 1")
plt.xlabel("Tytuł odcinka")
plt.ylabel("Ocena")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

sezony_ranking = dane.groupby("Season")["Rating"].mean()
plt.figure(figsize=(8, 5))
plt.plot(sezony_ranking.index, sezony_ranking.values, marker="o", color="green")
plt.title("Średnia ocena wg sezonu")
plt.xlabel("Sezon")
plt.ylabel("Średnia ocena")
plt.tight_layout()
plt.show()


odcinki_rocznie = dane["Year"].value_counts().sort_index()
plt.figure(figsize=(8, 8))
odcinki_rocznie.plot.pie(autopct="%1.1f%%", startangle=90, colors=plt.cm.Set3.colors)
plt.title("Liczba odcinków wg roku")
plt.ylabel("")
plt.tight_layout()
plt.show()

naj_miesiac = dane["Month"].value_counts().idxmax()
naj_dzien = dane["Day_of_week"].value_counts().idxmax()
print(f"\nNajwięcej odcinków wyszło w: {calendar.month_name[naj_miesiac]}")
print(f"Najwięcej odcinków w dzień tygodnia: {naj_dzien}")


najgorszy = dane.loc[dane["Zebra_score"].idxmin()]
print("\nOdcinek z najgorszym Zebra Score:")
print(f"{najgorszy['Episodes']} ({najgorszy['Zebra_score']}) – {najgorszy['Final_diagnosis']} – {najgorszy['Air_date'].date()}")


miesiace_oceny = dane.groupby("Month")["Rating"].mean()
plt.figure(figsize=(10, 5))
plt.plot(miesiace_oceny.index, miesiace_oceny.values, marker="s", linestyle="--", color="darkorange")
plt.title("Średnia ocena wg miesiąca emisji")
plt.xlabel("Miesiąc")
plt.ylabel("Średnia ocena")
plt.xticks(range(1, 13), calendar.month_abbr[1:])
plt.tight_layout()
plt.show()


pier_paz = dane[(dane["Day"] == 1) & (dane["Month"] == 10)]
if pier_paz.empty:
    print("\nNie ma odcinków z 1 października.")
else:
    print("\nOdcinki z 1 października:")
    print(pier_paz[["Episodes", "Zebra_score", "Final_diagnosis"]])


rezyser = dane["Director"].value_counts()
print(f"\nNajczęstszy reżyser: {rezyser.idxmax()} ({rezyser.max()} razy)")


pisarze_kolumny = ["Writer", "Writer 1", "Writer 2", "Writer 3", "Writer 4", "Writer 5"]
wszyscy_pisarze = dane[pisarze_kolumny].stack().value_counts()
print(f"\nNajczęstszy pisarz: {wszyscy_pisarze.idxmax()} ({wszyscy_pisarze.max()} razy)")
print(f"Najrzadszy pisarz: {wszyscy_pisarze.idxmin()} ({wszyscy_pisarze.min()} razy)")


rezyser_ranking = dane.groupby("Director")["Rating"].mean().nsmallest(10)
plt.figure(figsize=(10, 5))
plt.bar(rezyser_ranking.index, rezyser_ranking.values, color="tomato", edgecolor="black")
plt.title("Top 10 najgorszych reżyserów wg średniej oceny")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Średnia ocena")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(dane["Zebra_score"], dane["Rating"], color="orchid", edgecolors="black", s=100, alpha=0.7)
plt.title("Zależność między Zebra Score a oceną odcinka")
plt.xlabel("Zebra Score")
plt.ylabel("Ocena odcinka")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
