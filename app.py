from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')

def main():
    print(prato_paozinho)
    print(bebida_suco)


if __name__ == '__main__':
    main()
