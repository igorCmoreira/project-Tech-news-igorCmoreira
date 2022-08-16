from tech_news.analyzer.ratings import top_5_categories, top_5_news
import sys


def text_init():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )


# Requisito 12
def analyzer_menu():
    options = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
        "5": lambda: top_5_news(),
        "6": lambda: top_5_categories(),
        "7": lambda: "Encerrando script"
    }

    try:
        text_init()

        x = input()

        if x not in options or not x:
            raise ValueError("Opção inválida\n")

        if int(x) > 4:
            print(options[x]())

    except Exception:
        return print("Opção inválida", file=sys.stderr)
