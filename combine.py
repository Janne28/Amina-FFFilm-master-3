import os
datein = []
text =""
for root, dirs, files in os.walk("./",topdown=True):
    for file in files:
        if file.endswith(".fountain"):
            datei=os.path.join(root, file)
            if "Backup" in datei or  "Formatierung.fountain" == file or  "Gesammt.fountain" == file or  "0_Info.fountain" == file:
                pass
                #print(datei + "x")
            else:
                datein.append(datei)
                #print(datei)
datein = sorted(datein)
for filename in datein:
    file_object  = open(filename, "r").read()
    text = text + file_object
open("Gesammt.fountain", "w").write(text+ "\n")
print(datein)
