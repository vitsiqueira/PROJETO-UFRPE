import inputs

# ********* ALUNOS *********

alunos = []
def new_aluno(na, ca):
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            return False
    alunos.append([na, ca])
    return True

def att_aluno(ca):
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            nn_aluno = input("Novo nome do aluno: ").upper()
            nc_aluno = input("Novo CPF do aluno: ")
            alunos[a][0] = nn_aluno
            alunos[a][1] = nc_aluno
            return True

def apaga_aluno(ca):
    global alunos
    for a, b in enumerate(alunos):
        if b[1] == ca:
            del alunos[a]
            return True

def list_aluno():
    global alunos
    print("     : LISTA DE ALUNOS :\n")
    print(" ")
    print("{0:10} {1:45} {2:13}".format("Número", "Nome", "CPF"))
    for a, b in enumerate(alunos):
        print("{0:0>5}      {1:45} {2:13}".format(str(a+1), b[0], b[1]))
    print("="*70+"\n")
              
def grava_aluno():
    global alunos
    arqv_aluno = open("alunos.txt", "w", encoding = "utf-8")
    for a, b in enumerate(alunos):
        arqv_aluno.write("Aluno: {} :: CPF: {}\n".format(b[0], b[1]))
    arqv_aluno.close()

def lê_arquivo_aluno():
    global alunos
    arqv_aluno = open("alunos.txt", "r", encoding = "utf-8")
    for v in arqv_aluno.readlines():
        print(v)
    arqv_aluno.close()
    
