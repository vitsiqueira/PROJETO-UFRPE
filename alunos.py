import inputs

# ********* ALUNOS *********

alunos = []
def new_aluno(na, ca): #FUNÇÃO PARA ADICIONAR ALUNOS
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            return False
    alunos.append([na, ca]) #ADICIONANDO OS ELEMENTOS A LISTA ALUNOS
    return True

def att_aluno(ca): #FUNÇÃO PARA ATUALIZAR UM ALUNO
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            nn_aluno = input("Novo nome do aluno: ").upper() #UPPER PARA DEIXAR EM MAIÚSCULO
            nc_aluno = input("Novo CPF do aluno: ")
            alunos[a][0] = nn_aluno
            alunos[a][1] = nc_aluno
            return True

def apaga_aluno(ca): #FUNÇÃO PARA APAGAR ALUNOS
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            del alunos[a] #DEL PARA DELATAR xd
            return True

def list_aluno(): #FUNÇÃO PARA LISTAR OS ALUNOS
    global alunos
    print("     : LISTA DE ALUNOS :\n")
    print(" ")
    print("{0:10} {1:45} {2:13}".format("Número", "Nome", "CPF")) #ORGANIZAÇÃO = POSIÇÃO PARA CADA ELEMENTO
    for a, b in enumerate(alunos):
        print("{0:0>5}      {1:45} {2:13}".format(str(a+1), b[0], b[1])) #ELEMENTOS NA LISTA - ORGANIZADOS
    print("="*70+"\n")
              
def grava_aluno(): #FUNÇÃO PARA GRAVAR OS ALUNOS COMPUTADOS
    global alunos
    arqv_aluno = open("alunos.txt", "w", encoding = "utf-8")
    for a, b in enumerate(alunos):
        arqv_aluno.write("Aluno: {} :: CPF: {}\n".format(b[0], b[1]))
    arqv_aluno.close()

def lê_arquivo_aluno(): #FUNÇÃO PARA LER O ARQUIVO SALVO COM OS ALUNOS
    global alunos
    arqv_aluno = open("alunos.txt", "r", encoding = "utf-8")
    for v in arqv_aluno.readlines():
        print(v)
    arqv_aluno.close()
    
