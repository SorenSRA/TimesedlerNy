#Hvordan kan man udtrække ini fra navnestreng
import re


def ini():
    tekst = "Rasmussen, Søren (sra)"

    match = re.search(r'\((.*?)\)', tekst)

    if match:
        tekst_i_parentes = match.group(1)
        print(tekst_i_parentes)
    else:
        print("Ingen tekst i parentes blev fundet.")

if __name__ == '__main__':
    ini()