from modelos.classes_construtores_metodos import Livro


livro1 = Livro('O amor em 1899','Roberth Morthy','2010')
livro2 = Livro('Como empreender em 2025','Allana Morgan','2025')

livro1.alternar_estado()


def main():
    Livro.listar_livros()


if __name__ == '__main__':
    main()