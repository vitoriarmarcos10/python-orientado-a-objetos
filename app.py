from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')
restaurante_pizza = Restaurante('pizza express','Italiana')
restaurante_fast_food = Restaurante('Fast Food today','Fast Food')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Lais',8)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()