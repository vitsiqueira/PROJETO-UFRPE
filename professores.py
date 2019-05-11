import inputs

# ********* PROFESSORES *********

professores = []
def new_prof(np, cp, dp):
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            return False
    professores.append([np, cp, dp])
    return True
    print(" ")
    print("Sucesso! Professor adicionado.\n")
    print("="*70+"\n")
    print(" ")

def att_prof(cp):
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            nn_prof = input("Novo nome do professor: ").upper()
            nc_prof = input("Novo CPF do professor: ")
            nd_prof = input("Novo departamento: ").upper()
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

def apaga_prof(cp):
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            del professores[a]
            print(" ")
            print("Sucesso! Professor deletado.\n")
            print("="*70+"\n")
            print(" ")

def list_prof():
    global professores
    print("     : LISTA DE PROFESSORES :\n")
    print(" ")
    print("{0:10} {1:45} {2:13} {3:20}".format("Número", "Nome", "CPF", "Departamento"))
    for a, b in enumerate(professores):
        print("{0:0>5}    {1:45} {2:13} {3:20}".format(str(a+1), b[0], b[1], b[2])) #formatar direitinho os espaçamentos.
    print("="*70+"\n")

def grava_prof():
    global professores
    arqv_prof = open("professores.txt", "w", encoding = "utf-8")
    for a, b in enumerate(professores):
        arqv_prof.write("Professor: {} :: CPF: {} :: Departamento: {}\n".format(b[0], b[1], b[2]))
    arqv_prof.close()


def lê_arquivo_prof(): #resolver bug do começo do arquivo.
    global professores
    arqv_prof = open("professores.txt", "r")
    for v in arqv_prof.readlines():
        print(v)
    arqv_prof.close()



    
