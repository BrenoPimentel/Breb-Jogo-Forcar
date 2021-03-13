import sys
from time import sleep
import random


def forca():
    lista = ('Tornado',
             'Produzir',
             'Manequim',
             'Veleiro',
             'Sarda',
             'Demolir',
             'Data',
             'Cadeia',
             'Trigo',
             'Ancinho',
             'Alegria',
             'Carros',
             'Livros',
             'Ambulancia',
             'Copo',
             'Cabide',
             'Subir',
             'Senhora',
             'Casado',
             'Valor',
             'Kremlin',
             'Desenho',
             'Vir',
             'Nublado',
             'Compartimento',
             'Pano',
             'Berinjela',
             'Morder',
             'Cerca',
             'Arqueologia',
             'Esqui',
             'Espeto',
             'Hoje',
             'Concavo',
             'Bumerangue',
             'Cativo',
             'Bronquios',
             'Sofrer',
             'Aparar',
             'Flutuador',
             'Vaso',
             'Lapso',
             'Urso',
             'Resposta',
             'Sangue',
             'Alfaiate',
             'Inferno',
             'Cadeia',
             'Levedura',
             'Sentir',
             'Fita',
             'Goleiro',
             'Segredo',
             'Tempestade',
             'Barco',
             'Couro',
             'Resposta',
             'Coral',
             'Retrovisor',
             'Sinusite',
             'Resgate',
             'Meias',
             'Rolo',
             'Obeso',
             'Coiote',
             'Delta',
             'Poeira',
             'Sorte',
             'Descongelar',
             'Esticador',
             'Gastar',
             'Cerdas',
             'Beterraba',
             'Maca',
             'Cabelo',
             'Ladrões',
             'Abrigo',
             'Emboscada',
             'Futebol',
             'Chaves',
             'Leite',
             'Fervura',
             'Alvenaria',
             'Paciente',
             'Violoncelo',
             'Nogueira',
             'Apertado',
             'Verdor',
             'Veia',
             'Realidade',
             'Regras',
             'Irrigar',
             'Geladeira',
             'Misturar',
             'Revistas',
             'Bondade',
             'Fatiado',
             'passar',
             'nascer',
             'pernambuco',
             'muralha',
             'rinoceronte'
             )
    print('=' * 60)
    print(f'{"BEM VINDO":^60}')
    print(f'{"AO":^60}')
    print(f'{"JOGO DA FORCA":^60}')
    print('=' * 60)
    print('')
    secreto = random.choice(lista).upper()
    digitada = []
    erradas = []
    perdeu = 8
    print('~' * 50)
    print(f'{"Você só pode errar 8 vezes.":^50}')
    print('~' * 50)
    print(f'A palavra tem _{len(secreto)}_ letras.')
    while perdeu != 0:
        print('')
        letra = input('Digite uma letra: ').strip().upper()
        #  Vai salvando as letras ja digitadas
        digitada.append(letra)
        if letra == '':
            print('OPÇÃO INVÁLIDA. Digite uma letra.')
            continue
        elif erradas.count(letra) >= 1:
            print('OPÇÃO INVÁLIDA. Essa letra já foi digitada.')
            continue
        elif letra.isdigit():
            print('OPÇÃO INVÁLIDA. Digite uma letra. ')
            continue
        elif len(letra) > 1:
            print('OPÇÃO INVÁLIDA. Digite apenas uma letra.')
            continue
        if letra in secreto:
            print('')
            print(f'{"PARABÉNS!!!":^35}\nA letra "{letra}" está na palavra secreta.')
            palavra = ''
            sleep(0.8)
            print('-' * 35)
            for value in secreto:
                if value in digitada:
                    palavra += value
                else:
                    palavra += '*'
            print(f'{"palavra"} {palavra:^20}')
            print('-' * 35)
            for i in secreto:
                if digitada.count(i) > 1:
                    digitada.append(i)
            if palavra == secreto:
                print('-' * 30)
                print(f'PARABÉNS!!! "{secreto.title()}" era a palavra secreta \nVocê acertou')
                print('-' * 30)
                keep = ' '
                while keep != 's' and keep != 'n':
                    keep = input('Deseja reiniciar o jogo? [S/N]: ').lower().strip()
                if keep == 's':
                    forca()
                elif keep == 'n':
                    input('ENTER para sair')
                    sys.exit()
        else:
            erradas.append(letra)
            digitada.pop()
            print(f'Ops!! Não tem essa letra na palavra.')
            perdeu -= 1
            sleep(0.5)
            print(f'Você só pode errar mais {perdeu} vezes.')
            print('')
            print('=-=' * 10)
            print(f'ERRADAS:', end=' ')
            print(*erradas, sep=', ')
            print('=-=' * 10)
    print(f'Você perdeu!!!!! Não acertou a palavra "{secreto}."')
    keep = ' '
    while keep != 's' and keep != 'n':
        keep = input('Deseja reiniciar o jogo? [S/N]: ').lower().strip()
    if keep == 's':
        forca()
    elif keep == 'n':
        input('ENTER para sair')
        sys.exit()


if __name__ == '__main__':
    forca()
