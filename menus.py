import inputs
import professores
import alunos
import disciplinas
import turmas

# ********* MENUS *********

def prof_menu(): #MENU DOS PROFESSORES
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

        OP = int(input("::: ")) #CHAMA O COMANDO DESEJADO
        print("="*70+"\n")

        if OP > 6 or OP < 0:
            print("Tente novamente.")
            continue

        if OP == 1:
            np = inputs.nome_prof() #CHAMA NOME DO PROFESSOR.
            cp = inputs.cpf_prof() #CHAMA CPF DO PROFESSOR.
            dp = inputs.dep_prof() #CHAMA O DEPARTAMENTO.
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
            


def aluno_menu(): #MENU DOS ALUNOS
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

        OA = int(input("::: ")) #CHAMA A OPÇÃO DESEJADA
        print("="*70+"\n")

        if OA > 6 or OA < 0:
            print("Tente novamente.")
            continue
            
        if OA == 1: #SE A OPÇÃO FOR IGUAL A 1 SERÁ EXECUTADA A SEGUINTE OPERAÇÃO...
            na = inputs.nome_aluno() #CHAMA NOME DO ALUNO
            ca = inputs.cpf_aluno() #CHAMA CPF DO ALUNO
            if alunos.new_aluno(na, ca) == True: #SE FOR VERDADEIRO PRINTA O QUE VEM A BAIXO
                print(" ")
                print("Sucesso! Aluno adicionado.\n")
                print("="*70+"\n")
                print(" ")
            aluno_menu() #RETORNA AO MENU DO ALUNO
            
        if OA == 2: #SE A OPÇÃO FOR IGUAL A 2 SERÁ EXECUTADA A SEGUINTE OPERAÇÃO...
            ca = inputs.cpf_aluno() #CHAMA O CPF DO ALUNO QUE DESEJA ATUALIZAR
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
            ca = inputs.cpf_aluno() #CHAMA O CPF DO ALUNO QUE DESEJA APAGAR
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
            alunos.list_aluno() #FUNÇÃO PARA MOSTRAR A LISTA DE ALUNOS
            aluno_menu()

        if OA == 5:
            alunos.grava_aluno() #FUNÇÃO PARA SALVAR A LISTA DE ALUNOS EM ARQUIVO
            aluno_menu()

        if OA == 6:
            alunos.lê_arquivo_aluno() #FUNÇÃO PARA MOSTRAR O ARQUIVO SALVO
            print("="*70+"\n")
            aluno_menu()

        if OA == 0: #RETORNAR PARA O MENU PRINCIPAL
            menu_principal()
            
            
# MENU DAS DISCIPLINAS::::

def disc_menu():
    print("""       : DADOS DAS DISCIPLINAS :\n
    Escolha uma das opções a seguir:\n
    0 - Para retornar ao menu principal;
    1 - Para adicionar uma disciplina;
    2 - Para atualizar uma disciplina;
    3 - Para deletar uma disciplina;
    4 - Para consultar lista de disciplinas.
    5 - Para gravar disciplina.
    6 - Para ler a lista de disciplinas gravadas.\n""")

    while True:

        OD = int(input("::: "))
        print("="*70+"\n")

        if OD > 6 or OD < 0: #SE O INPUT FOR MENOR QUE 0 OU MAIOR QUE 6 SERÁ EXECUTADO NOVAMENTE, POIS NÃO EXISTEM ESSAS OPÇÕES
            print("Tente novamente.")
            continue
            
        if OD == 1:
            nd = inputs.nome_disc() #CHAMA O NOME DA DISCIPLINA
            cd = inputs.cod_disc() #CHAMA O CÓDIGO DA DISCIPLINA
            if disciplinas.new_disc(nd, cd) == True:
                print(" ")
                print("Sucesso! Disciplina adicionada.\n")
                print("="*70+"\n")
                print(" ")
            disc_menu()
            
        if OD == 2:
            cd = inputs.cod_disc() #CHAMA O CÓDIGO DA DISCIPLINA QUE DESEJA ATUALIZAR
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
            cd = inputs.cod_disc() #CHAMA O CÓDIGO DA DISCIPLINA QUE DESEJA APAGAR
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
            disciplinas.list_disc() #LISTA DE DISCIPLINAS
            disc_menu()
            
        if OD == 5:
            disciplinas.grava_disc() #SALVA LISTA EM ARQUIVO
            disc_menu()

        if OD == 6:
            disciplinas.lê_arquivo_disc() #LÊ O ARQUIVO SALVO
            print("="*70+"\n")
            disc_menu()

        if OD == 0: #RETORNAR PARA O MENU PRINCIPAL
            menu_principal()
            

# MENU DAS TURMAS::::

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
    7 - Para ver a ATA de exercícios.\n""")

    while True:

        OT = int(input("::: "))
        print("="*70+"\n")

        if OT > 8 or OT < 0:
            print("Tente novamente.")
            continue
            
        if OT == 1:
            ct = inputs.cod_turma() #CHAMA O CÓDIGO DA TURMA
            pt = inputs.peri_turma() #CHAMA O PERÍODO DA TURMA
            cdd = inputs.cod_disc() #CHAMA O CÓDIGO DA DISCIPLINA
            cpp = inputs.cpf_prof() #CHAMA O CPF DO PROFESSOR
            caa = inputs.cpf_aluno() #CHAMA O CPF DO ALUNO
            if turmas.new_turma(ct, pt, cdd, cpp, caa) == True:
                print(" ")
                print("Sucesso! Turma adicionada.\n")
                print("="*70+"\n")
                print(" ")
            turma_menu()
            
        if OT == 2:
            ct = inputs.cod_turma() #CHAMA O CÓD. DA TURMA QUE DESEJA ALTERAR
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
            ct = inputs.cod_turma() #CHAMA O CÓD. DA TURMA QUE DESEJA APAGAR
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
            turmas.list_turma() #LISTA DE TURMAS
            turma_menu()

        if OT == 5:
            turmas.grava_turma() #SALVA LISTA EM ARQUIVOS
            turma_menu()

        if OT == 6:
            turmas.lê_arquivo_turma() # LÊ O ARQUIVO
            print("="*70+"\n")
            turma_menu()

        if OT == 7:
            turmas.ata() #CHAMA A FUNÇÃO DA ATA DE EXERCÍCIOS
            print("="*70+"\n")
            turma_menu()

        if OT == 0:
            menu_principal()
            
            

# ::::

def menu_principal():
    print("::: Bem vindo(a)!")
    print(" ")
    print("""    Escolha uma das opções a seguir:\n
    0 - Para sair;
    1 - Para dados dos professores;
    2 - Para dados dos alunos;
    3 - Para dados das disciplinas;
    4 - Para dados das turmas.\n""")


    while True:
        OM = int(input("::: "))
        print("="*70+"\n")

        if OM > 4 or OM < 0:
            print("Tente novamente.")
            continue

        if OM == 0: #ENCERRA O PROGRAMA
            exit()
 
        if OM == 1: #EXECUTA O MENU DOS PROFESSORES
            prof_menu()
            
        if OM == 2: #EXECUTA O MENU DOS ALUNOS
            aluno_menu()
                        
        if OM == 3: #EXECUTA O MENU DAS DISCIPLINAS
            disc_menu()          

        if OM == 4: #EXECUTA O MENU DAS TURMAS
            turma_menu()

       
