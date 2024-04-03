⚠️ Deze repository is verouderd. De CONNECT wrapper is gebouwd om de oude API heen en werkt dus niet met de huidige versie (v7). 



# Stikstof Vingerafdruk Analyse

## Intro 
Om kwetsbare natuur te beschermen, zal de N-depositie in gevoelige N2000-gebieden moeten verminderen. Voor het treffen van maatregelen is het van belang om de emissiebronnen die voor (een grote) depositie zorgen, zo goed mogelijk in beeld te krijgen. Deze informatie maakt het mogelijk om een helder beeld te krijgen van het nut van verschillende maatregelpaketten
In Aerius monitor valt te achterhalen welke sectoren de grootste bijdrage leveren aan de depositie. Er valt echter niet te achterhalen wat de ruimtelijke spreiding van deze emissiebronnen is, of hoeveel invloed de individuele bronnen hebben. 
Dit script helpt bij het berekenen van de lokale effecten van stikstofemissies. 

## Contact
Via GitHub of via de mail: t.schouten@pzh.nl.

## Instructies
Het script is geschreven in Python v3.7 m.b.v. De code en documentatie zijn samengevoegd in een Jupyter Notebook. Vervolgstappen zijn uitgewerkt in FME en komen evt. later ook beschikbaar in Python.

## Bestanden & Folders
- bronnen-lokaliseren.ipynb -- Jupyter Notebook workflow
- utils.py -- Helpfuncties om te communiceren met de AERIUS Connect API.
- nox-env.yml -- Conda package file: via (mini)conda kan je een kopie maken van de werkomgeving met het volgende commando:
```sh
conda env create -f aerius-env.yml
```

## Brondata
We maken gebruik van 500x500 emissierasters van o.a. Emissieregistratie (RIVM) en zelf gegenereerde sets.
