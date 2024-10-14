def menuprincipal():
    while True:
        print("----------Seja bem vindo à InstaBooks----------")
        print("1. Inserir (Usuário, livro ou interação)")
        print("2. Consultar (Usuário, livro ou interação)")
        print("3. Atualizar (Usuário, livro ou interação)")
        print("4. Deletar (Usuário, livro ou interação)")
        print("5. Visualizar o número de usuários, livros e interações na rede social.")
        print("6. Visualizar Top 5 livros mais avaliados.")
        print("7. Identificar os usuários mais seguidos.")
        print("8. Seguir outros usuários.")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            import inserir 
            inserir.inserirgeral()
        elif opcao == "2":
            import consultar
            consultar.consultargeral()
        elif opcao == "3":
            import atualizar
            atualizar.atualizargeral()
        elif opcao == "4":
            import deletar
            deletar.deletargeral()
        elif opcao == "5":
            import totalBanco
            totalBanco.totalbd()
        elif opcao == "6":
            import livrosMaisAvaliados
            livrosMaisAvaliados.livros_mais_avaliados()
        elif opcao == "7":
            import usuariosMaisSeguidos
            usuariosMaisSeguidos.usuarios_mais_avaliados()
        elif opcao == "8":
            import seguidoresUsuario
            seguidoresUsuario.seguir_usuario()
        else:
            break
menuprincipal()