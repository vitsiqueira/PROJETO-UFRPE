# ********************************** MENUS - PROJETO ***************************************

while True:
    print("::: Bem vindo(a)!")
    print(" ")
    print("""    Escolha uma das opções a seguir:\n
    0 - Para sair;
    1 - Para dados dos professores;
    2 - Para dados dos alunos;
    3 - Para dados das disciplinas;
    4 - Para dados das turmas;
    5 - Para relatórios.\n""")

    OM = int(input("::: "))
    print("="*80+"\n")

    if OM == 0:
        break;

# ---------------------------------------------------------------------------------    

    if OM == 1:
        print("""       : DADOS DOS PROFESSORES :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar um professor(a);
    2 - Para atualizar um professor(a);
    3 - Para deletar um professor(a);
    4 - Para consultar lista de professores.
    5 - Para gravar.\n""")

        OP = int(input("::: "))
        print("="*80+"\n")

        if OP == 0:
            break;

        if OP == 1:
            new_prof()

        if OP == 2:
            att_prof()

        if OP == 3:
            del_prof()

        if OP == 4:
            list_prof()

        if OP == 5:
            grava_prof()

# ---------------------------------------------------------------------------------
            
    if OM == 2:
        print("""         : DADOS DOS ALUNOS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar um aluno(a);
    2 - Para atualizar um aluno(a);
    3 - Para deletar um aluno(a);
    4 - Para consultar lista de alunos.
    5 - Para gravar.\n""")

        OA = int(input("::: "))
        print("="*80+"\n")

        if OA == 0:
            break;
            
        if OA == 1:
            new_aluno()
            
        if OA == 2:
            att_aluno()

        if OA == 3:
            del_aluno()

        if OA == 4:
            list_aluno()

        if OA == 5:
            grava_aluno()
            
# ---------------------------------------------------------------------------------
            
    if OM == 3:
        print("""       : DADOS DAS DISCIPLINAS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar uma disciplina;
    2 - Para atualizar uma disciplina;
    3 - Para deletar uma disciplina;
    4 - Para consultar lista de disciplinas.
    5 - Para gravar.\n""")

        OD = int(input("::: "))
        print("="*80+"\n")

        if OD == 0:
            break;
            
        if OD == 1:
            new_disc()
            
        if OD == 2:
            att_disc()

        if OD == 3:
            del_disc()

        if OD == 4:
            list_disc()
            
        if OD == 5:
            grava_disc()

# ---------------------------------------------------------------------------------            

    if OM == 4:
        print("""         : DADOS DAS TURMAS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar uma turma;
    2 - Para atualizar uma turma;
    3 - Para deletar uma turma;
    4 - Para consultar lista de turmas.
    5 - Para gravar.\n""")

        OT = int(input("::: "))
        print("="*80+"\n")

        if OT == 0:
            break;
            
        if OT == 1:
            new_turma()
            
        if OT == 2:
            att_turma()

        if OT == 3:
            del_turma()

        if OT == 4:
            list_turma()

        if OT == 5:
            grava_turma()

# ---------------------------------------------------------------------------------

    if OM == 5:
        print("""            : RELATÓRIOS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para consultar a ATA de exercícios;
    2 - Para consultar a lista de turma por professor;
    3 - Para consultar a lista de disciplinas por aluno;\n""")

        OR = int(input("::: "))
        print("="*80+"\n")

        if OR == 0:
            break;
            
        if OR == 1:
            ata()
            
        if OR == 2:
            print("""              : TURMAS POR PROFESSOR :\n
        1 - Para relatório de todas as turmas;
        2 - Para relatório de turmas por semestre;
        3 - Para retornar ao menu de relatórios.\n""")

            TPO = int(input("::: "))
            print("="*80+"\n")

            if TPO == 1:
                tpo_todas()

            if TPO == 2:
                top_psem()

            if TPO == 3:
                break;

        if OR == 3:
            print("""              : DISCIPLINAS POR ALUNO :\n
        1 - Para relatório de todas as turmas;
        2 - Para relatório de turmas por semestre.
        3 - Para retornar ao menu de relatórios.\n""")

            DAO = int(input("::: "))
            print("="*80+"\n")

            if DAO == 1:
                dao_todas()

            if DAO == 2:
                dao_psem()

            if DAO == 3:
                break;



