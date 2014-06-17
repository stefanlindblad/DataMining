#Merkmalsextraktion mit der Nicht-Negativen Matrixfaktorisierung

##Allgemein

** Was versteht man unter Artikel/Wort-Matrix? Wie sieht diese im aktuellen Versuch aus? ** 

Die Artikel/Wort-Matrix enthält pro Dokument eine Spalte und pro Wort eine Zeile. 
In der i-ten Zeile und der j-ten Spalte steht, wie oft was Wort wj im Dokument di vorkommt.


			  wort1   wort2   wort3   wort4   wort5   wort6
	A	=  [[    1,		5, 		0, 		0, 		1, 		0    ]		Artikel 1
  			[	 2,		0,		2,		3,		0,		8	 ]]		Artikel 2


	v = {wort1, wort2, wort3, wort4, wort5, wort6}

	a = A * v
	a =	[[titel 1]	   = [[{ 1*wort1,  5*wort2,  1*wort5		   }]
		 [titel 2]]       [{ 2*wort1,  2*wort3,  3*wort4,  8*wort6 }]]


** Wie multipliziert man die Matrix A mit dem Vector v? **

	A = 	|a00 a01 a02 a03|	v = 	|v1|		A * v =  	|a00*v1 + a01*v2 + a02*v3 +  a03*v4|	(zeile * spalte)
			|a10 a11 a12 a13|			|v2|					|a10*v1 + a11*v2 + a12*v3 +  a13*v4|
			|a20 a21 a22 a23|			|v3|					|a20*v1 + a21*v2 + a22*v3 +  a23*v4|
			|a30 a31 a32 a33|			|v4|					|a30*v1 + a31*v2 + a32*v3 +  a33*v4|

** Was versteht man im Kontext der nnMF unter... **

- Merkmalsmatrix? 

Die Merkmalsmatrix definiert aus welchen Wörtern die Merkmale gebildet werden.
//TODO more

- Gewichtsmatrix 

Die Gewichtsmatrix beschreibt mit welchem Gewicht die einzelnen Merkmale in den Artikeln auftreten. 
//TODO more

** Wie definieren die Zeilen der Merkmalsmatrix die einzelnen Merkmale (Topics)? ** 

	????????

** Was definieren die Zeilen der Gewichtungsmatrix? ** 

	????????

** Wie werden in Numpy zwei Arrays (Typ numpy.array) ... **

- im Sinne der Matrixmultiplikation miteinander multipliziert? 

---> a.dot(b)	   or     np.dot(a,b)

>>> import numpy as np
>>> a
array([[0, 1],
	  [2, 3]])
>>> b
array([[2, 3],
	   [4, 5]])
>>> a.dot(b)
array([[ 4,  5],
	   [16, 21]])
>>> np.dot(a,b)
array([[ 4,  5],
	   [16, 21]])

- elementweise multipliziert?		

---> np.multiply(a,b)

>>> import numpy as np
>>> a
array([[0, 1],
	   [2, 3]])
>>> b
array([[2, 3],
	   [4, 5]])
>>> np.multiply(a,b)
array([[ 0,  3],
	   [ 8, 15]])

** Wie wird die Transponierte eines Numpy-Arrays berechnet? **

>>> x = np.arange(4).reshape((2,2))
>>> x
array([[0, 1],
	   [2, 3]])
>>> np.transpose(x)
array([[0, 2],
	   [1, 3]])
