def voto(a):
    from datetime import date
    anohoje = date.today().year
    idade = anohoje - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


nasc = int(input('Que ano você nasceu? : '))
print(voto(nasc))
