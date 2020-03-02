# camelMe
CamelMe is a vscode extention build to automatically convert variable names to camel cases.
	```newitem => newItem```
This is done on basis of the data set on wordlist of top 60k english words and their frequencies.
Currently it a Naive app to get proper camel cased variable names in future a ML module can be trained to get
appropriate camel case.
The drawback of naive is that, it cannot determine proper subsetting of variable names ;eg incat => in_cat or inc_at.This
can be highly improoved using machine learning which can determine which subset to use.
