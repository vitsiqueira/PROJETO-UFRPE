import inputs

# ********* PROFESSORES *********

disciplinas = []
def new_disc(nd, cd): #ADICIONAR NOVAS DISCIPLINAS
    global disciplinas
    for a, b in enumerate(disciplinas):
        if b[1] == cd:
            return False
    disciplinas.append([nd, cd]) #ADICIONAR A LISTA DISCIPLINAS
    return True

def att_disc(cd): #ATUALIZAR DISCIPLINAS
    global disciplinas
    for a, b in enumerate(disciplinas):
        if b[1] == cd:
            nn_disc = input("Novo nome da disciplina: ").upper()
            nc_disc = input("Novo código da disciplina: ")
            disciplinas[a][0] = nn_disc #SUBSTITUINDO
            disciplinas[a][1] = nc_disc
            return True
    
def apaga_disc(cd): #APAGAR UMA DISCIPLINA
    global disciplinas
    for a, b in enumerate(disciplinas):
        if b[1] == cd:
            del disciplinas[a]
            return True

def list_disc(): #LISTA DE DISCIPLINAS
    global disciplinas
    print("     : LISTA DE DISCIPLINAS :\n")
    print(" ")
    print("{0:10} {1:45} {2:13}".format("Número", "Nome", "Código"))
    for a, b in enumerate(disciplinas):
        print("{0:0>5}      {1:45} {2:13}".format(str(a+1), b[0], b[1]))
    print("="*70+"\n")

def grava_disc(): #GRAVAR EM ARQUIVO AS DISCIPLINAS ADICIONADAS
    global disciplinas
    arqv_disc = open("disciplinas.txt", "w", encoding = "utf-8")
    for a, b in enumerate(disciplinas):
        arqv_disc.write("Disciplina: {} :: Código: {}\n".format(b[0], b[1]))
    arqv_disc.close()

def lê_arquivo_disc(): #LÊ O ARQUIVO SALVO COM AS DISCIPLINAS
    global disciplinas
    arqv_disc = open("disciplinas.txt", "r", encoding = "utf-8")
    for v in arqv_disc.readlines():
        print(v)
    arqv_disc.close()
