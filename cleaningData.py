import csv
import pandas as pd

def limpezaDeArquivo(arquivo):
    with open(arquivo, 'r') as csvFile:
        data_list = list(csv.reader(csvFile))
        tratado = []
        for separandoPorVirgula in data_list:
            string = ''
            separado = separandoPorVirgula[1].split(" ")
            for i in separado:
                if "http" in i: 
                    i = ''
                if "@" in i:
                    i = ''
                if "#" in i:
                    i = ''
                if not i.isalpha():
                    i = ''
                string = string + ' ' + i
            final = (string, separandoPorVirgula[0])
            tratado.append(final)
    csvFile.close()
    file1 = open(arquivo,"w")
    for l in tratado:
        file1.writelines("\'"+l[1]+"\',\'"+l[0]+"\'\n")
    file1.close()

def preparandoArquivoParaUpload(arquivo):
    with open(arquivo, 'r') as csvFile: 
        data_list = list(csv.reader(csvFile))
        listaDeTupla = []
        i = 0
        lista = 0
        for row in data_list:
            listaDeTupla.append((row[0], row[1]))
            lista = lista+1
            i = i+1
            if(i==50):
                i = 0
    csvFile.close()

    file1 = open("arquivoFinal.txt","w") 
    file1.write("[")
    for l in listaDeTupla:
        file1.writelines("(\'"+ l[0] + "\', " + "\'" + l[1] + "\'),\n")
    file1.write("]") 
    file1.close()

def contagemDaBSD(arquivo): 
    df = pd.read_csv(arquivo, sep=',')
    print(df.groupby('Classification').size())
    print(df.set_index(["Classification"]).count(level="Classification"))