# class Livro:

#     livros = []

#     def __init__(self, titulo,autor,ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self._ativo = True
#         Livro.livros.append(self)


#     def __str__(self):
#         return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {self.ano_publicacao.ljust(25)}'


#     def alternar_estado(self):
#         self._ativo = not self._ativo

    
#     @staticmethod
#     def listar_livros():
#         print(f'{"Titulo".ljust(25)} | {"Autor".ljust(25)} | {"Ano Publicação".ljust(25)} | {"Ativo".ljust(25)}')
#         for livro in Livro.livros:
#             print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {livro.ano_publicacao.ljust(25)} | {livro._ativo.ljust(25)}')


# livro1 = Livro('O amor em 1899','Roberth Morthy','2010')
# livro2 = Livro('Como empreender em 2025','Allana Morgan','2025')


# Livro.listar_livros()

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._ativo = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano_publicacao).ljust(25)}'

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_livros(cls):
        print(f'{"Titulo".ljust(25)} | {"Autor".ljust(25)} | {"Ano Publicação".ljust(25)} | Ativo')
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(25)} | {livro.autor.ljust(25)} | {str(livro.ano_publicacao).ljust(25)} | {livro.ativo}')
