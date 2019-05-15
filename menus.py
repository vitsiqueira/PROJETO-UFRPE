import inputs
import professores
import alunos
import disciplinas
import turmas

# ********* MENUS *********

def prof_menu():
    print("""       : DADOS DOS PROFESSORES :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar um professor(a);
    2 - Para atualizar um professor(a);
    3 - Para deletar um professor(a);
    4 - Para consultar lista de professores.
    5 - Para gravar professor.
    6 - Para ler a lista de professores gravados.\n""")

    while True:

        OP = int(input("::: "))
        print("="*70+"\n")

        if OP > 6 or OP < 0:
            print("Tente novamente.")
            continue

        if OP == 1:
            np = inputs.nome_prof() #adicionar nome do professor.
            cp = inputs.cpf_prof() #adicionar cpf do professor.
            dp = inputs.dep_prof() #adicionar departamento.
            if professores.new_prof(np, cp, dp) == True: # se a operação for verdadeira.
                print(" ")
                print("Sucesso! Professor adicionado.\n")
                print("="*70+"\n")
                print(" ")
            prof_menu()         #retornar para o menu do professor.

        if OP == 2:
            cp = inputs.cpf_prof() # pede cpf do professor que quer atualizar.
            if professores.att_prof(cp) == True: # se a operação for verdadeira.
                print(" ")
                print("Sucesso! Professor atualizado.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Professor não cadastrado.\n")
                print("="*70+"\n")
                print(" ")
            prof_menu() #retornar.

        if OP == 3:
            cp = inputs.cpf_prof() #pede cpf do professor que quer apagar.
            if professores.apaga_prof(cp) == True: # se a operação for verdadeira.
                print(" ")
                print("Sucesso! Professor deletado.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Professor não cadastrado.\n")
                print("="*70+"\n")
                print(" ")
            prof_menu() #retornar.

        if OP == 4:
            professores.list_prof() #chama a função da lista de professores.
            prof_menu() #retornar.

        if OP == 5:
            professores.grava_prof() #chama a função de gravar professor.
            prof_menu() #retornar.

        if OP == 6:
            professores.lê_arquivo_prof() #chama a função de ler arquivo.
            print("="*70+"\n")
            prof_menu() #retornar.

        if OP == 0:
            menu_principal()


def aluno_menu():
    print("""         : DADOS DOS ALUNOS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar um aluno(a);
    2 - Para atualizar um aluno(a);
    3 - Para deletar um aluno(a);
    4 - Para consultar lista de alunos.
    5 - Para gravar aluno.
    6 - Para ler a lista de alunos gravada.\n""")

    while True:

        OA = int(input("::: "))
        print("="*70+"\n")

        if OA > 6 or OA < 0:
            print("Tente novamente.")
            continue
            
        if OA == 1:
            na = inputs.nome_aluno()
            ca = inputs.cpf_aluno()
            if alunos.new_aluno(na, ca) == True:
                print(" ")
                print("Sucesso! Aluno adicionado.\n")
                print("="*70+"\n")
                print(" ")
            aluno_menu()
            
        if OA == 2:
            ca = inputs.cpf_aluno()
            if alunos.att_aluno(ca) == True:
                print(" ")
                print("Sucesso! Aluno atualizado.\n")
                print("="*70+"\n")
                print(" ")
                aluno_menu()
            else:
                print(" ")
                print("Erro! Aluno não cadastrado.\n")
                print("="*70+"\n")
                print(" ")
                aluno_menu()

        if OA == 3:
            ca = inputs.cpf_aluno()
            if alunos.apaga_aluno(ca) == True:
                print(" ")
                print("Sucesso! Aluno deletado.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Aluno não cadastrado.\n")
                print("="*70+"\n")
                print(" ")
            aluno_menu()

        if OA == 4:
            alunos.list_aluno()
            aluno_menu()

        if OA == 5:
            alunos.grava_aluno()
            aluno_menu()

        if OA == 6:
            alunos.lê_arquivo_aluno()
            print("="*70+"\n")
            aluno_menu()

        if OA == 0:
            menu_principal()
            
# ::::

def disc_menu():
    print("""       : DADOS DAS DISCIPLINAS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar uma disciplina;
    2 - Para atualizar uma disciplina;
    3 - Para deletar uma disciplina;
    4 - Para consultar lista de disciplinas.
    5 - Para gravar disciplina.
    6 - Para ler a lista de disciplinas gravadas.\n""") #falta fazer o if. = resolvido

    while True:

        OD = int(input("::: "))
        print("="*70+"\n")

        if OD > 6 or OD < 0:
            print("Tente novamente.")
            continue
            
        if OD == 1:
            nd = inputs.nome_disc()
            cd = inputs.cod_disc()
            if disciplinas.new_disc(nd, cd) == True:
                print(" ")
                print("Sucesso! Disciplina adicionada.\n")
                print("="*70+"\n")
                print(" ")
            disc_menu()
            
        if OD == 2:
            cd = inputs.cod_disc()
            if disciplinas.att_disc(cd) == True:
                print(" ")
                print("Sucesso! Disciplina atualizada.\n")
                print("="*70+"\n")
                print(" ")
                disc_menu()
            else:
                print(" ")
                print("Erro! Disciplina não cadastrada.\n")
                print("="*70+"\n")
                print(" ")
                disc_menu()

        if OD == 3:
            cd = inputs.cod_disc()
            if disciplinas.apaga_disc(cd) == True:
                print(" ")
                print("Sucesso! Disciplina deletada.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Disciplina não cadastrada.\n")
                print("="*70+"\n")
                print(" ")
            disc_menu()

        if OD == 4:
            disciplinas.list_disc()
            disc_menu()
            
        if OD == 5:
            disciplinas.grava_disc()
            disc_menu()

        if OD == 6:
            disciplinas.lê_arquivo_disc()
            print("="*70+"\n")
            disc_menu()

        if OD == 0:
            menu_principal()
            continue

# ::::

def turma_menu():
    print("""         : DADOS DAS TURMAS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar uma turma;
    2 - Para atualizar uma turma;
    3 - Para deletar uma turma;
    4 - Para consultar lista de turmas.
    5 - Para gravar turma.
    6 - Para ler a lista de turmas gravadas.
    7 - Para adicionar alunos.
    8 - Para apagar alunos.\n""") #falta fazer o if

    while True:

        OT = int(input("::: "))
        print("="*70+"\n")

        if OT > 8 or OT < 0:
            print("Tente novamente.")
            continue
            
        if OT == 1:
            ct = inputs.cod_turma()
            pt = inputs.peri_turma()
            cdd = inputs.cod_disc()
            cpp = inputs.cpf_prof()
            caa = inputs.cpf_aluno()
            if turmas.new_turma(ct, pt, cdd, cpp, caa) == True:
                print(" ")
                print("Sucesso! Turma adicionada.\n")
                print("="*70+"\n")
                print(" ")
            turma_menu()
            
        if OT == 2:
            ct = inputs.cod_turma()
            if turmas.att_turma(ct) == True:
                print(" ")
                print("Sucesso! Turma atualizada.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Turma não cadastrada.\n")
                print("="*70+"\n")
                print(" ")
            turma_menu()

        if OT == 3:
            ct = inputs.cod_turma()
            if turmas.apaga_turma(ct) == True:
                print(" ")
                print("Sucesso! Turma deletada.\n")
                print("="*70+"\n")
                print(" ")
            else:
                print(" ")
                print("Erro! Turma não cadastrada.\n")
                print("="*70+"\n")
                print(" ")
            turma_menu()

        if OT == 4:
            turmas.list_turma()
            turma_menu()

        if OT == 5:
            turmas.grava_turma()
            turma_menu()

        if OT == 6:
            turmas.lê_arquivo_turma()
            print("="*70+"\n")
            turma_menu()

        if OT == 0:
            menu_principal()
            continue
            

# ::::

def rela_menu():
    print("""            : RELATÓRIOS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para consultar a ATA de exercícios;
    2 - Para consultar a lista de turma por professor;
    3 - Para consultar a lista de disciplinas por aluno;\n""")

    while True:

        OR = int(input("::: "))
        print("="*70+"\n")

        if OR > 3 or OR < 0:
            print("Tente novamente.")
            continue

        if OR == 0:
            break;
            
        if OR == 1:
            turmas.ata()
            rela_menu()
            
        if OR == 2:
            print("""              : TURMAS POR PROFESSOR :\n
        1 - Para relatório de todas as turmas;
        2 - Para relatório de turmas por semestre;
        3 - Para retornar ao menu de relatórios.\n""")

            TPO = int(input("::: "))
            print("="*70+"\n")

            if TPO > 3 or TPO < 0:
                print("Tente novamente.")
                continue

            if TPO == 1:
                tpo_todas()

            if TPO == 2:
                top_psem()

            if TPO == 3:
                rela_menu()

        if OR == 3:
            print("""              : DISCIPLINAS POR ALUNO :\n
        1 - Para relatório de todas as turmas;
        2 - Para relatório de turmas por semestre.
        3 - Para retornar ao menu de relatórios.\n""")

            DAO = int(input("::: "))
            print("="*70+"\n")

            if DAO > 3 or DAO < 0:
                print("Tente novamente.")
                continue

            if DAO == 1:
                dao_todas()

            if DAO == 2:
                dao_psem()

            if DAO == 3:
                rela_menu()


def menu_principal():
    print("::: Bem vindo(a)!")
    print(" ")
    print("""    Escolha uma das opções a seguir:\n
    0 - Para sair;
    1 - Para dados dos professores;
    2 - Para dados dos alunos;
    3 - Para dados das disciplinas;
    4 - Para dados das turmas;
    5 - Para relatórios.\n""")


while True:
    menu_principal()
    
    OM = int(input("::: "))
    print("="*70+"\n")

    if OM > 5 or OM < 0:
        print("Tente novamente.")
        continue

    if OM == 0:
        exit()
 
    if OM == 1:
        prof_menu()
            
    if OM == 2:
        aluno_menu()
                        
    if OM == 3:
        disc_menu()          

    if OM == 4:
        turma_menu()

    if OM == 5:
        rela_menu()
