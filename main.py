# Rainer Herold
# Version 0.1
# 23.12.2021

# Bibliotheken_Implementierung
try:
    from numpy import array
    from os import walk, makedirs
    from os.path import expanduser, getsize, join
    from sys import argv, exit
    from shutil import copy2
    from time import sleep
except ModuleNotFoundError as e:
    input(f"Das Modul {e} wurde nicht gefunden.\n\nBitte wenden Sie Sich an den Entwickler.\n\nZum Verlassen, bitte mit Enter bestaetigen.")

# Sicherheits_Einstellungen
if (len(argv) > 2): print ("Eine Ueberladung des Programmes ist nicht moeglich."), sleep(5), exit()

# Variablen_Bereich
try: Vorgang = argv[1]
except IndexError: print ("Es wurde kein Parameter angegeben."), sleep(5), exit()

# Arrays
Array_Festplatte = array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

# Funktionen
def Initialien():
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ('               		      OS-Detector')
    print ('                              Version 0.1')
    print ('                             Rainer Herold')
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def Datei_Lesen(Pfadangabe):
    Datei = open(Pfadangabe, 'r')
    Text = Datei.readlines()
    Datei.close()

    return Text

def OS_Scannen():
    with open(expanduser(r'~\Desktop\OS.txt'), 'w', encoding='utf-8') as f:
        for Festplatte in Array_Festplatte:
            for root,_,files in walk(f'{Festplatte}:/', topdown=False):
                for file in array(files): f.write(f'{join(root, file)[3:]}, {getsize(join(root, file))}\n')
    f.close()

def Auswerten():
    Liste_OS, Liste_Groesse, Liste_Pfade = Datei_Lesen(expanduser(r'~\Desktop\OS.txt')), [], []

    for i in array(Liste_OS):
        Liste_Groesse.append(i.split(', ')[1]), Liste_Pfade.append(i.split(',')[0])

    with open(expanduser(r'~\Desktop\Filter.txt'), 'w', encoding='utf-8') as f:
        for Festplatte in Array_Festplatte:
            for root,_,files in walk(f'{Festplatte}:/', topdown=False):
                for file in array(files):
                    for Pfad in range(0, len(array(Liste_Pfade))):
                        if (Liste_Pfade[Pfad] == join(root, file)[:3]):
                            if (int(Liste_Groesse[Pfad]) > getsize(join(root, file)) or int(Liste_Groesse[Pfad]) < getsize(join(root, file))):
                                f.write(f'{join(root, file)}\n')
                                try: makedirs(expanduser(fr'~\Desktop\Beweismaterial\{root[3:]}'))
                                except: pass
                                copy2(join(root, file), expanduser(fr'~\Desktop\Beweismaterial\{join(root, file)[3:]}'))

                for file in array(files):                    
                    if (join(root, file)[:3] not in Liste_Pfade):                  
                        f.write(f'{join(root, file)}\n')
                        try: makedirs(expanduser(fr'~\Desktop\Beweismaterial\{root[3:]}'))
                        except: pass
                        copy2(join(root, file), expanduser(fr'~\Desktop\Beweismaterial\{join(root, file)[3:]}'))
    f.close()

# Aufruf_Bereich
if __name__ == '__main__':
    Initialien()
    try:
        if (Vorgang == 'Scan' or Vorgang == 'scan'): OS_Scannen()
        elif (Vorgang == 'Auswerten' or Vorgang == 'auswerten'): Auswerten()
    except PermissionError: print ("Es gibt Berechtigungsprobleme, wodurch das Skript nicht richtig verwendet werden kann.")
