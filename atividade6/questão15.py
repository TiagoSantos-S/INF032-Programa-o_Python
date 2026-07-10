tarefas = []

while True:
    comando = input("\nADD | DONE | LIST | EXIT: ").upper()

    if comando == "ADD":
        titulo = input("Título: ")
        prioridade = int(input("Prioridade (1-5): "))

        tarefas.append({
            "titulo": titulo,
            "prioridade": prioridade,
            "status": "aberta"
        })

    elif comando == "DONE":
        titulo = input("Título: ")

        for tarefa in tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["status"] = "concluida"

    elif comando == "LIST":
        filtro = input("Filtro (aberta/concluida ou Enter): ").lower()

        ordenadas = sorted(tarefas, key=lambda x: x["prioridade"])

        for tarefa in ordenadas:
            if filtro == "" or tarefa["status"] == filtro:
                print(
                    tarefa["titulo"],
                    "| Prioridade:", tarefa["prioridade"],
                    "| Status:", tarefa["status"]
                )

    elif comando == "EXIT":
        break

    else:
        print("Comando inválido.")