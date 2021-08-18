def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade > 65 or 16 >= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
