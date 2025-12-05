import os

def tela_opcao():
    print("========================================================================")
    print("|                                                                      |")
    print("|                            𝗚𝗶𝘁𝗛𝘂𝗯😺💾                               |")
    print("|                                                                      |")
    print("|                       .^7J5GBB#####BGPY?!:.                          |")
    print("|                    ^?5B##&############&&##GY!:                       |")
    print("|                 :?G#&&#####################&&#5!.                    |")
    print("|               :Y#&##&&&&################&&&&&#&&G7.                  |")
    print("|              ?#&####77?5G#&&########&&&#PY?!J####&G~                 |")
    print("|            .5&####&Y     ^77~^^:::^^~7!:     G####&#?                |")
    print("|           .P&#####&5                        .B######&?               |")
    print("|           Y&#######?                        .Y########!              |")
    print("|          ~########!                           J&#####&G              |")
    print("|          J&#####&P                            .B#######^             |")
    print("|          5&#####&5                            .B######&!             |")
    print("|          Y&######G.                           ^########~             |")
    print("|          !&######&J                          .P&######B.             |")
    print("|           P&####&&&Y:                       ^P&######&?              |")
    print("|           ^B&##G5P#&#57^.              .:~?P#&######&5               |")
    print("|            ^B&#G?::J#&&#BGP!        .JPGB#&&#######&5.               |")
    print("|             :5&&&B! ^YGBBB5.         ^#&#########&#?                 |")
    print("|               !G&&#?.  ..             G########&#5^                  |")
    print("|                 !P#&#P5YY57           G#####&&BY^                    |")
    print("|                   :7PB&&&@Y           G&&&#GY!.                      |")
    print("|                      .~7Y5!           ?5J!^.                         |")
    print("|                                                                      |")
    print("|                   Escolha sua opção:                                 |")
    print("|               1-Adicionar novo repositório                           |")
    print("|               2 - Adicionar novo commit                              |")
    print("|               3 - Sair                                               |")
    print("|                                                                      |")
    print("| Criado por Gustavo Nunes da Silva 🖥️                                 |")
    print("========================================================================")

def tela_adicionarnovorepositorio():
    print("========================================================================")
    print("|              𝗔𝗱𝗶𝗰𝗶𝗼𝗻𝗲 𝘂𝗺 𝗻𝗼𝘃𝗼 𝗿𝗲𝗽𝗼́𝘀𝗶𝘁𝗼𝗿𝗶𝗼 𝗻𝗼 𝗚𝗶𝘁𝗛𝘂𝗯😺💾               |")
    print("========================================================================")

def tela_inicial():
    print("========================================================================")
    print("|                       𝗚𝗶𝘁𝗛𝘂𝗯 Automático😺💾                         |")
    print("========================================================================")

def tela_adicionarnovocommit():
    print("========================================================================")
    print("|              𝗔𝗱𝗶𝗰𝗶𝗼𝗻𝗲 𝘂𝗺 𝗻𝗼𝘃𝗼 commit 𝗻𝗼 𝗚𝗶𝘁𝗛𝘂𝗯😺💾               |")
    print("========================================================================")

def tela_sair():
    print("========================================================================")
    print("|                           Você saiu 😿                               |")
    print("========================================================================")

def tela_concluido():
    print("========================================================================")
    print("|       𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼́𝗿𝗶𝗼 𝗰𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗮𝗱𝗼 𝗲 𝗰𝗼́𝗱𝗶𝗴𝗼 𝗲𝗻𝘃𝗶𝗮𝗱𝗼 𝗰𝗼𝗺 𝘀𝘂𝗰𝗲𝘀𝘀𝗼 ✅!       |")
    print("========================================================================")

# Função principal
tela_inicial()
nome = input("| Digite seu nome😊: ")
email = input("| Digite seu email 📩: ")
os.system(f'git config user.name "{nome}"')
os.system(f'git config user.email "{email}"')

tela_opcao()
opção = input("| Qual a opção deseja 😉?: ")

if opção == '1':
    os.system("git init")
    tela_adicionarnovorepositorio()
    print("| *Git Init inicializado")
    os.system("git add .")
    print("| *Git add . inicializado")
    print("| Deseja ver o git status? 🤔")
    gitstatus = input("| Digite sua opção -> S (sim) ou N (não):")
    
    if gitstatus.lower() in ['s', 'sim']:
        os.system("git status")

    mensagem = input("| Digite a mensagem do commit 📨: ")
    os.system(f'git commit -m "{mensagem}"')
    link = input("| Digite o link do repositório remoto 🔗: ")
    os.system(f'git remote add origin {link}')
    os.system("git branch -M main")
    os.system("git push -u origin main")

    tela_concluido()

elif opção == '2':
    tela_adicionarnovocommit()
    os.system("git add .")
    print("| *Git add . inicializado")
    print("| Deseja ver o git status? 🤔")
    gitstatus = input("| Digite sua opção -> S (sim) ou N (não):")
    
    if gitstatus.lower() in ['s', 'sim']:
        os.system("git status")

    mensagem = input("| Digite a mensagem do commit 📨: ")
    os.system(f'git commit -m "{mensagem}"')
    print("| Commit realizado com sucesso!")
    os.system("git push")
    tela_concluido()

elif opção == '3':
    tela_sair()

else:
    print("Opção inválida! Tente novamente.")
