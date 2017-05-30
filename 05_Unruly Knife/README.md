# Distribution of the marital status' of the inhabitants Copenhagen

The dataset provided contains ~174.000 observations from 1992 - 2015.  

## Columns:
* AAR: Which year the observation was made

* BYDEL: Which part of the city, described by an integer contained in following dict; 1=Indre By, 2=Østerbro, 3=Nørrebro, 4=Vesterbro/Kgs. Enghave, 5=Valby, 6=Vanløse, 7=Brønshøj-Husum, 8=Bispebjerg, 9=Amager Øst, 10=Amager Vest, 99=Udenfor inddeling

* ALDER: The age of the observed people

* CIVST: Marital Status, described by an upper-case character contained in the following dict: E=Widdow, F=Divorced, G=Maried, L=Oldest living partner, O=Dissolved partnership, P=Registered partnership, U=Unmarried

* KOEN: Gender of observed people, described by an integer contained in the following dict: 1=Male, 2=Female

* PERSONER: Number of observations with the given features of the row.

## Excercise:
1. We use matplotlib to show the distribution of the following four categories over the time of 1992 - 2015
```Terminal
  - Males between age 18 and 30
  - Females between age 18 and 30
  - Males age 50+
  - Females age 50+
```

2. We use matplotlib to plot a bar-char showing how many single males and females of age 18 to 30, are living in BYDEL 1, 2 and 3 over the time 1992 - 2015

3. Find the three most populated city parts(BYDEL), in 1992, 2000 and 2015
```Terminal
1992 - Norrebro
2000 - Osterbro
2015 - Osterbro
```
4. We created two pie-charts, showing the distribution of marital status' in bydel 1, 2 and 3 in year 2000 and 2015

5. We made a histogram of the age distribution in all of the municipality of Copenhangen.
