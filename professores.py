# ********************************** PROFESSORES - PROJETO ***************************************

professores = []
def new_prof():
    global professores
    np = nome_prof().upper()
    cp = cpf_prof()
    dp = dep_prof().upper()
    professores.append([np, cp, dp])
    print(" ")
    print("Sucesso! Professor adicionado.\n")
    print("="*70+"\n")
    print(" ")

def att_prof(): #ajeitar isso aqui
    global atualizap
    cpa = cpf_prof()
    for a, b in enumerate(professores):
        if b[1] == cpf_prof:
            nn_prof = input("Novo nome do professor: ")).upper()
            nc_prof = input("Novo CPF do professor: "))
            nd_prof = input("Novo departamento: ")).upper()
            professores[a][0] = nn_prof
            professores[a][1] = nc_prof
            professores[a][2] = nd_prof
            print(" ")
            print("Sucesso! Professor atualizado.\n")
            print("="*70+"\n")
            print(" ")
        else:
            print(" ")
            print("Falha! Professor não encontrado.\n")
            print("="*70+"\n")
            print(" ")

def grava_prof():
    global professores
    nome_arquivo = nome_aqv()
    arqv_prof = open(nome_arquivo, "w", encoding = "utf-8")
    for e in professores:
        arqv_prof.write("{} :: {} :: {}".format(e[0], e[1], e[2]))
    arqv_prof.close()

def list_prof():
    print("     : LISTA DE PROFESSORES :\n"
    nome_arquivo = nove_aqv()
    lista_prof(nome_arquivo)
    




    
