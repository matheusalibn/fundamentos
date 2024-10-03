def adicionarTarefa(tarefas, nome_tarefa):

    # tarefa: nome da tarefa
    # completada: indicar se ja foi completada
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:\n")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "x" if tarefa["completada"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["nome"] = novo_nome
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice Invalido!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    tarefas[indice_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def deletar_tarefas(tarefas):
    print("Tarefas completadas foram deletadas")
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completas")
    print("6. Sair")

    escolha = input("Digite a sua escolha:")

    if escolha == "1":
        nome_tarefa = input("Qual o nome da tarefa:")
        adicionarTarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja atualizar:\n ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja completar:")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        deletar_tarefas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break


print("Programa finalizado")