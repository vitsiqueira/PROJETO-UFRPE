import inputs, professores, alunos, disciplinas

# ********* TURMAS *********

turmas = []

def checar_aluno(cp):
    global professores, turmas
    try:
        arqv_prof = open("professores.txt", "r", encoding = "utf-8")
        for cpfprof in professores.readlines():
            cpfprof = cpfprof.split(" :: ")[1]
            if cpfprof == cp:
                return cpfprof
        arqv_prof.close()

def checar_aluno(ca):
    global alunos, turmas
    try:
        arqv_aluno = open("alunos.txt", "r", encoding = "utf-8")
        for cpfaluno in alunos.readlines():
            cpfaluno = cpfaluno.split(" :: ")[1]
            if cpfaluno == ca:
                return cpfaluno
            arqv_aluno.close()

def checar_disc(cd):
    global disciplinas, turmas
    try:
        arqv_disc = open("disciplinas.txt", "r", encoding = "utf-8")
        for coddisc in disciplinas.readlines():
            coddisc = coddisc.split(" :: ")[1]
            if coddisc == cd:
                return coddisc
            arqv_disc.close()
                 

def new_turma(ct, pt, cd, cp, ca):
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            return False
        turmas.append([ct, pt, cd, cp, ca])
        return True

def att_turmas(ct):
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            nc_turma = input("Novo código da turma: ")
            np_turma = input("Novo período da turma: ").upper()
            ncd_turma = input("Novo código da disciplina: ")
            ncp_turma = input("Novo CPF do professor: ")
            nca_turma = input("Novo CPF do aluno: ")
            turmas[a][0] = nc_turma
            turmas[a][1] = np_turma
            turmas[a][2] = ncd_turma
            turmas[a][3] = ncp_turma
            turmas[a][4] = nca_turma
            return True

def apaga_turma(ct):
    global turmas
    for a, b in enumerate(turmas):
        if b[0] == ct:
            del turmas[a]
            return True

def list_turma():
    global turmas
    print("     : TURMAS :\n")
    print(" ")
    print("{0:10} {1:12} {2:12} {3:12} {4:12}".format("Número", "Código da Turma", "Período", "Código da Disciplina", "CPF do professor")) #organização
    for a, b in enumerate(professores):
        print("{0:0>5}      {1:12} {2:12} {3:12} {4:12}".format(str(a+1), b[0], b[1], b[2], b[3])) #formatar direitinho os espaçamentos. = resolvido
    print("="*70+"\n")

def grava_turma():
    global turmas
    arqv_turma = open("turmas.txt", "w", encoding = "utf-8")
    for a, b in enumerate(turmas):
        arqv_turma.write("Código: {} :: Período: {} :: Cód. da Disciplina: {} :: CPF/professor: {}\n".format(b[0], b[1], b[2], b[3], b[4]))
    arqv_turma.close()

def lê_arquivo_turma():
    global turmas
    arqv_turma = open("turmas.txt", "r", encoding = "utf-8")
    for v in arqv_turma.readlines():
        print(v)
    arqv_turma.close()
