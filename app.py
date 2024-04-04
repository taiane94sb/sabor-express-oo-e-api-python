from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')

restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)

def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
