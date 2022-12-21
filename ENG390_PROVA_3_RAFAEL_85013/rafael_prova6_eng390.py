'''Algoritmo:

1- Importar o arquivo dados_csv.csv utilizando Biblioteca Pandas.
2- Converter a tabela de dados Pandas em uma matriz NumPY
Criar um menu baseado em funções com as  funcionalidades:
a) selecionar uma das variáveis, visualizar a série de dados e processar para esta
série valores mínimo e máximo, a média, o desvio padrão e o coeficiente de
variação.
b) Mostrar os dados selecionados;
c) Apresentar uma tabela com os dados selecionas e os valores mínimo e
máximo, a média, o desvio padrão e o coeficiente de variação.
d) Gravar os arquivos processados sendo que o usuário definirá o nome do
arquivo.


'''


##BIBLIOTECAS UTILIZADAS
import numpy as np
import pandas as pd

# Proceder a leitura de arquivos ***.CSV
dados_aeras = pd.read_csv('dados_csv.csv', encoding= "ISO-8859-1", sep=';')

# Converter DataFrame Pandas para Array Numpy
dadosNP = dados_aeras.to_numpy()

# Selecionar os dados numéricos para cálculos com a NumPy
dadoNum = dados_aeras[['ID','Tamb','URamb','Taqv','URaqv','UEaqv','Aqq']].to_numpy()

#visualizar a série de dados e processar para esta
#série valores mínimo e máximo, a média, o desvio padrão e o coeficiente de
#variação.
def dados_id():
    dadoNum_ = dados_aeras[['ID']]

    #Estatistica por ID
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 55*'_'
    print(linha)
    print('Tabela de Dados - Indice')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))



def dados_Tamb():

    dadoNum_ = dados_aeras[['Tamb']]

    #Estatistica por Tamb
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 55*'_'
    print(linha)
    print('Série de Dados - Temperatura do ar ambiente')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))

def dados_URamb():
    dadoNum_ = dados_aeras[['URamb']]

    #Estatistica por Uramb
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 55*'_'
    print(linha)
    print('Série de Dados - Umidade relativa do ar ambiente')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))

def dados_Taqv():
    dadoNum_ = dados_aeras[['Taqv']]

    #Estatistica por Taqv
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 100*'_'
    print(linha)
    print('Série de Dados - Temperatura do ar aquecido após passar pelo ventilador do silo')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))


def dados_URaqv():

    dadoNum_ = dados_aeras[['URaqv']]

    #Estatistica por URaqv
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 100*'_'
    print(linha)
    print('Série de Dados - Temperatura do ar aquecido após passar pelo ventilador do silo')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))


def dados_UEaqv():

    dadoNum_ = dados_aeras[['UEaqv']]

    #Estatistica por UEaqv
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 100*'_'
    print(linha)
    print('Série de Dados - Teor de água dos grãos ao entrar em equlibrio com ar aquecido')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))


def dados_Aqq():

    dadoNum_ = dados_aeras[['Aqq']]

    #Estatistica por Aqq
    minimo_ = np.min(dadoNum_, axis=0)
    med_ = np.mean(dadoNum_, axis=0)
    max_ = np.max(dadoNum_, axis=0)
    desvio_ = np.std(dadoNum_,axis=0)
    cv_ = (desvio_*100)/(med_)


#Publicação da tabela dos valores calculados
    linha = 100*'_'
    print(linha)
    print('Série de Dados - Aquecimento necessário a ser aplicado ao ar ambiente para que o teor de água dos grãos atinja 13%')
    print(linha)
    print(dadoNum_)
    print(linha)

    print('{:<8s}{:<18s}{:>8.0f}' \
            .format('', 'Mínimo', minimo_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Média', med_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Máximo',max_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Desvio Padrão', desvio_[0]))

    print('{:<8s}{:<18s}{:>8.2f}' \
            .format('', 'Coef. Var (%)', cv_[0]))

##Publicar tabela com os valores cálculados
def dados_complementar():

    dados_complementar = pd.read_csv('dados_csv.csv', encoding= "ISO-8859-1", sep=';')


    minimoLinha   = np.min(dados_complementar,  axis=1)
    mediaLinha    = np.mean(dados_complementar, axis=1)
    maximoLinha   = np.max(dados_complementar,  axis=1)
    desvioPlinha  = np.std(dados_complementar,  axis=1)
    cvLinha       = (desvioPlinha*100)/(mediaLinha)

    dados_complementar['Minimo']= minimoLinha
    dados_complementar['Média']= mediaLinha
    dados_complementar['Máximo']= maximoLinha
    dados_complementar['Desvio P.']= desvioPlinha
    dados_complementar['CV']= cvLinha


    linha = '_'*110


#Publicação da tabela
    print(linha)
    print('{:^95s}'.format('DADOS - 13/12/2022 - AERA-STD#1'))
    print(linha)
    print('{:<8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^18s}'\
        .format('ID.','Tamb','URamb','Taqv','URaqv','UEaqv','Aqq','Mínimo','Média' ,' Máximo', ' DP', ' CV (%)'))
    print(linha)

    for i in range(0,len(dadosNP)):
        id  = dadosNP[i,0]
        tamb = dadosNP[i,1]
        uramb   = dadosNP[i,2]
        taqv   = dadosNP[i,3]
        uraqv   = dadosNP[i,4]
        ueaqv   = dadosNP[i,5]
        aqq   = dadosNP[i,6]

        print('{:<8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^10.2f}{:^10.2f}{:^10.2f}' \
                .format(id, tamb, uramb,taqv,uraqv,ueaqv,aqq, minimoLinha[0], mediaLinha[0], maximoLinha[0], \
                        desvioPlinha[0], cvLinha[0]))


#Gravar arquivo CSV contendo com o dataframe atualizado
def savecsv(name):

    dados_complementar = pd.read_csv('dados_csv.csv', encoding= "ISO-8859-1", sep=';')


    minimoLinha   = np.min(dados_complementar,  axis=1)
    mediaLinha    = np.mean(dados_complementar, axis=1)
    maximoLinha   = np.max(dados_complementar,  axis=1)
    desvioPlinha  = np.std(dados_complementar,  axis=1)
    cvLinha       = (desvioPlinha*100)/(mediaLinha)

    dados_complementar['Minimo']= minimoLinha
    dados_complementar['Média']= mediaLinha
    dados_complementar['Máximo']= maximoLinha
    dados_complementar['Desvio P.']= desvioPlinha
    dados_complementar['CV']= cvLinha


    linha = '_'*110



    print(linha)
    print('{:^95s}'.format('DADOS - 13/12/2022 - AERA-STD#1'))
    print(linha)
    print('{:<8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^8s}{:^18s}'\
        .format('ID.','Tamb','URamb','Taqv','URaqv','UEaqv','Aqq','Mínimo','Média' ,' Máximo', ' DP', ' CV (%)'))
    print(linha)

    for i in range(0,len(dadosNP)):
        id  = dadosNP[i,0]
        tamb = dadosNP[i,1]
        uramb   = dadosNP[i,2]
        taqv   = dadosNP[i,3]
        uraqv   = dadosNP[i,4]
        ueaqv   = dadosNP[i,5]
        aqq   = dadosNP[i,6]

        print('{:<8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^8.2f}{:^10.2f}{:^10.2f}{:^10.2f}' \
                .format(id, tamb, uramb,taqv,uraqv,ueaqv,aqq, minimoLinha[0], mediaLinha[0], maximoLinha[0], \
                        desvioPlinha[0], cvLinha[0]))


        dados_complementar.to_csv (name+'.csv', index = True, header=True)
        print('Arquivo salvo!')

opcao = 99
#___________________________________________PROCESSAMENTO
#Menu com opções:
""" a) selecionar uma das variáveis, visualizar a série de dados e processar para esta
série valores mínimo e máximo, a média, o desvio padrão e o coeficiente de
variação.
b) Mostrar os dados selecionados;
c) Apresentar uma tabela com os dados selecionas e os valores mínimo e
máximo, a média, o desvio padrão e o coeficiente de variação.
d) Gravar os arquivos processados sendo que o usuário definirá o nome do
arquivo. """
while(opcao != 5):

    opcao = int(input(' 1- Visualizar a série de dados com valores mínimo e máximo, média, desvio padrão e coeficiente devariação.\n 2 - Mostrar os dados selecionados\n 3 - Tabela com os dados selecionas e os valores mínimo e máximo, a média, o desvio padrão e o coeficiente de variação\n 4 - Gravar os arquivos processados\n 5 - SAIR '))
    #a) selecionar uma das variáveis, visualizar a série de dados e processar para esta
        #série valores mínimo e máximo, a média, o desvio padrão e o coeficiente de
        #variação.
    if(opcao == 1):
                op1 = 99
                while (op1 != 8):
                        try:
                            rel = float(input(' (1)Índice\n (2)Temperatura do ar ambiente, °C\n (3)Umidade relativa do ar ambiente\n (4)Temperatura do ar aquecido após passar pelo ventilador do silo, °C\n (5)Umidade relativa do ar aquecido após passar pelo ventilador do silo\n (6)Teor de água dos grãos ao entrar em equlibrio com ar aquecido\n (7)Aquecimento necessário a ser aplicado ao ar ambiente para que o teor de água dos grãos atinja 13%\n (8) para finalizar: '))
                            if(rel == 1):

                                dados_id()
                            elif(rel == 2):
                                dados_Tamb()
                            elif(rel == 3):
                                dados_URamb()
                            elif(rel == 4):
                                dados_Taqv()
                            elif(rel == 5):
                                dados_URaqv()
                            elif(rel == 6):
                                dados_UEaqv()
                            elif(rel == 7):
                                dados_Aqq()
                        except ValueError:
                            print('Erro: Informe número inteiros.')
                        op1 = rel
     #a) selecionar uma das variáveis, visualizar a série de dados e processar para esta
        #série valores mínimo e máximo, a média, o desvio padrão e o coeficiente de
        #variação.
    if(opcao == 2):

                op2 = 99
                while (op2 != 2):
                    try:
                        select = int(input('Aperte 1 para Mostrar Dados Selecionados ou 2 para finalizar: '))
                        if(select == 1):
                            print(dados_aeras)
                    except ValueError:
                        print('Erro: Informe número inteiros.')
                    op2 = select

        #Apresentar uma tabela com os dados selecionas e os valores mínimo e
        #máximo, a média, o desvio padrão e o coeficiente de variação.
    if(opcao == 3):

                op3 = 99
                while (op3 != 2):
                    try:
                        complementar = int(input('Aperte 1 para Mostrar Dados Selecionados ou 2 para finalizar: '))
                        if(complementar == 1):
                            dados_complementar()
                    except ValueError:
                        print('Erro: Informe número inteiros.')
                    op3 = complementar


    if(opcao == 4):
        #d) Gravar os arquivos processados sendo que o usuário definirá o nome do
        #arquivo.

                op4 = 99
                while (op4 != 2):
                    try:
                        save = int(input('Aperte 1 para Gravar os arquivos processados ou 2 para finalizar: '))
                        if(save == 1):

                                nome = input('Defina um nome para salvar o arquivo: ')
                                savecsv(nome)
                    except ValueError:
                        print('Erro: Informe número inteiros.')
                    op4 = save




