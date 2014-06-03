#Dokumenten Klassifikation / Spam Filter

##Allgemein

** Wie wird ein Naiver Bayes Classifier trainiert? **
Aus den Trainingsdaten wird die Zugehörigkeit zu einer bestimmten Klasse gelernt.
[...]

** Wie teilt ein Naiver Bayes Classifier ein neues Dokument ein? **
Um für eine Eingabe x eine Klasse zu bestimmen wird für alle möglichen Klassen Ci die bedingte Wahrscheinlichkeit P(Ci|x) bestimmt und dann die Klasse gewählt für die diese Wahrscheinlichkeit maximal ist. x ist dabei ein Vektor von Wörtern, die im Dokument vorkommen. Der Naive Bayes Classifier geht davon aus, dass alle Wörter des Vektors unabhängig voneinander sind. 

** Welche naive Annahme liegt dem Bayes Classifier zugrunde? **
Dem Naiven Bayes Classifier liegt die Annahme zugrunde, dass alle Wörter in einem Dokument unabhängig voneinander sind. 

** Ist die Annahme im Fall der Dokumentenklassifikation tatsächlich gegeben? **
Nicht unbedingt. Es können so zum Beispiel keine Negierungen miteinbezogen werden. Es kann also nicht beurteilt werden ob ein Dokument ein Thema kritisch oder positiv betrachtet, da nicht festgestellt werden kann auf welche Worte sich die Negierungen beziehen. 

** Betrachten Sie die Formeln 5 und 6. Welches Problem stellt sich ein, wenn ein einer Menge W(D) ein Wort vorkommt, das nicht in den Trainingsdaten der Kategorie G vorkommt und ein anderes Wort aus W(D) nicht in den Trainingsdaten der Kategofie B enthalten ist? Wie könnte dieses Problem gelöst werden? **
Für jedes Wort w in D wird die Wahrscheinlichkeit berechnet wirt, dass es in G vorkommt, und alle so entstandenen Wahrscheinlichkeiten werden multipliziert. Die Wahrscheinlichkeit, dass ein nicht bekanntes Wort vorkommt ist jedoch 0. So wird das Ergebnis des Produkts auf jeden Fall 0 sein.
Dies könnte vermieden werden indem man nicht bekannte Wörter aus einem Dokument D bei der Klassifizierung nicht berücksichtigt. Bei der nächsten Klassifkiation würde dann das Dokument D zu den Trainingsdokumenten zählen und die darin vorkommenden Wörter können für alle weiteren Klassifikationen miteinberechnet werden.
