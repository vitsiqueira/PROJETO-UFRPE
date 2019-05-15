import inputs

# ********* TURMAS *********

turmas = []
cpfalunos = []
def new_turma(ct, pt, cdd, cpp, caa): #NOVA TURMA
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            return Flase
    turmas.append([ct, pt, cdd, cpp, caa])
    return True

def att_turma(ct): #ATUALIZAR TURMA
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            nc_turma = input("Novo código da turma: ")
            np_turma = input("Novo período da turma: ")
            ncd_turma = input("Novo código da disciplina: ")
            ncp_turma = input("Novo CPF do professor: ")
            nca_turma = input("Novo CPF do aluno: ")
            turmas[a][0] = nc_turma
            turmas[a][1] = np_turma
            turmas[a][2] = ncd_turma
            turmas[a][3] = ncp_turma
            turmas[a][4] = nca_turma
            return True

def apaga_turma(ct): #APAGAR TURMA
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            del turmas[a]
            return True

def list_turma(): #LISTAR TURMAS ADICIONADAS
    global turmas
    print("     : LISTA DE TURMAS :\n")
    print(" ")
    print("{0:10} {1:18} {2:21} {3:17} {4:22} {5:18}".format("Número", "Código/Turma", "Período", "Código/Disciplina", "CPF/Professor", "CPF/Aluno"))
    for a, b in enumerate(turmas):
        print("{0:0>5}      {1:18} {2:21} {3:17} {4:22} {5:18}".format(str(a+1), b[0], b[1], b[2], b[3], b[4]))
    print("="*70+"\n")

def grava_turma(): #GRAVAR TURMAS EM ARQUIVO
    global turmas
    arqv_turma = open("turmas.txt", "w", encoding = "utf-8")
    for a, b in enumerate(turmas):
        arqv_turma.write("Código/Turma: {} :: Período: {} :: Código/Disciplina: {} :: CPF/Professor: {} :: CPF/Aluno: {}\n".format(b[0], b[1], b[2], b[3], b[4]))
    arqv_turma.close()

def lê_arquivo_turma(): #LÊ ARQUIVO SALVO
    global turmas
    arqv_turma = open("turmas.txt", "r", encoding = "utf-8")
    for v in arqv_turma.readlines():
        print(v)
    arqv_turma.close()


# ********* RELATÓRIOS *********

def ata():  #ATA DE EXERCÍCIOS 
    global turmas
    coddisc = inputs.cod_disc() #CHAMA O CÓD. DA DISCIPLINA
    codturm = inputs.cod_turma() #CHAMA O CÓD. DA TURMA
    nomealuno = inputs.nome_aluno() #CHAMA O NOME COMPLETO DO ALUNO

    for v in turmas:
        if codturm == v[0] and coddisc == v[2]: #A BAIXO IMPRIMIMOS A ATA DE EXERCÍCIOS
            print("""
============================================================================
Cód. Disciplina: {}
============================================================================
Cód. Turma: {}                Período: {}
============================================================================
CPF/Professor: {}
============================================================================
Aluno(a): {}            | CPF: {}
Nota: ____________   Assinatura: ___________________________________________
============================================================================
""".format(v[2], v[0], v[1], v[3], nomealuno, v[4]))

            
