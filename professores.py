import inputs

# ********* PROFESSORES *********

professores = []
def new_prof(np, cp, dp): #ADICIONAR NOVO PROFESSOR
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            return False
    professores.append([np, cp, dp]) #ADICONAR DADOS A LISTA
    return True

def att_prof(cp): #ATUALIZAR PROFESSOR
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            nn_prof = input("Novo nome do professor: ").upper()
            nc_prof = input("Novo CPF do professor: ")
            nd_prof = input("Novo departamento: ").upper()
            professores[a][0] = nn_prof #ATUALIZANDO DADOS
            professores[a][1] = nc_prof #ATUALIZANDO DADOS
            professores[a][2] = nd_prof #ATUALIZANDO DADOS
            return True

def apaga_prof(cp): #APAGAR PROFESSOR
    global professores
    for a, b in enumerate(professores):
        if b[1] == cp:
            del professores[a] #FUNÇÃO DEL PARA DELETAR PROFESSOR
            return True

def list_prof(): #LISTA DE PROFESSORES
    global professores
    print("     : LISTA DE PROFESSORES :\n")
    print(" ")
    print("{0:10} {1:45} {2:13} {3:20}".format("Número", "Nome", "CPF", "Departamento")) #organização
    for a, b in enumerate(professores):
        print("{0:0>5}      {1:45} {2:13} {3:20}".format(str(a+1), b[0], b[1], b[2])) #FORMATAÇÃO DOS ELEMENTOS
    print("="*70+"\n")

def grava_prof(): #SALVA LISTA DE PROFESSORES EM ARQUIVO
    global professores
    arqv_prof = open("professores.txt", "w", encoding = "utf-8") #ABRIR ARQUIVO QUE SERÃO SALVOS OS DADOS
    for a, b in enumerate(professores):
        arqv_prof.write("Professor: {} :: CPF: {} :: Departamento: {}\n".format(b[0], b[1], b[2])) #WRITE PARA ESCREVER NO ARQUIVO AQUILO QUE DESEJA
    arqv_prof.close()  #FECHAR ARQUIVO


def lê_arquivo_prof(): #LÊ O ARQUIVO SALVO
    global professores
    arqv_prof = open("professores.txt", "r", encoding = "utf-8")
    for v in arqv_prof.readlines():
        print(v)
    arqv_prof.close()



    
