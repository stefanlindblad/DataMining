#Fragen zum zweiten Versuch (Recommender Systeme)

##Allgemein

**Beschreiben sie das Prinzip des userbasierten Collaborative Filtering (UCF).**

Das UCF nutzt die Ähnlichkeit zwischen Nutzern um Produkte zu empfehlen. Dabei wird für jeden Nutzer U1 der jeweils ähnlichste Nutzer U2 ermittelt. Nutzer U1 werden dann jene Produkte vorgeschlagen, die Nutzer U2 bereits erworben hat, Nutzer U1 jedoch noch nicht. 

**Welche Nachteile hat das UCF?**

Das UCF skaliert schlecht für große User/Item-Matrizen.
Außerdem ist es für Nutzer, die erst wenige Produkte erworben haben sehr unzuverlässig.

**Worin besteht der Unterschied zwischen dem UCF und dem itembasierten Collaborative Filtering (ICF)?**

Im Gegensatz zum UCF, bei dem für jeden Nutzer der jeweils ähnlichste Nutzer ermittelt wird, wird beim ICF für jedes Produkt, dass der entsprechende Nutzer U gekauft hat, das ähnlichste Produkt ermittelt. Dabei sind Produkte umso ähnlicher, je mehr Kunden sie zusammen gekauft haben. Das ähnlichste Produkt wird dann dem Nutzer U vorgeschlagen. 

**Zeigen Sie am Beispiel des Vectors a = [1,2,3,4,5,6] wie Mittelwert und Varianz eines Vectors berechnet werden.**
- Mittelwert: 	`(1+2+3+4+5+6)/6 = 3,5`            -> Summe aller Elemente durch die Anzahl aller Elemente
- Varianz:	 	`((1-3.5)^2 +(2-3.5)^2 +(3-3.5)^2 +(4-3.5)^2 +(5-3.5)^2 +(6-3.5)^2 )/6` -> (jedes Element minus den Mittelwert (Erwartungswert) hoch 2) geteilt durch die Anzahl aller Elemente 

**Wie werden Mittelwert und Varianz mit numpy berechnet?**

```
>>> a = array([1,2,3,4,5,6])
>>> np.mean(a)
3.5
>>> np.var(a)
2.91666666667
```

**Wie groß ist die ... der beiden Vectoren a = [1,2,3,4,5,6] und b = [3,3,5,6,7,8]:**

- euclidische Ähnlichkeit
	`4.58257569496`
- Pearson-Ähnlichkeit
	`0.0166565779371`
- Cosinus-Ähnlichkeit
	`0.00893991525484`

**In welchen Fällen sind die Cosinus- und Pearson-Ähnlichkeit der euklidischen Ähnlichkeit vorzuziehen?**

**Wie wird in Python ein doppelt verschachteltes Dictionary angelegt und wie greift man auf dessen Elemente zu?**

```
>>> d = {'a'={'b'='c'}}
>>> d['a']['b']
c
```

**Wie können mit Hilfe der last.fm-API pylast.py alle Alben einer Band bestimmt werden?**