def rhyme_a_name(name):
    """The Name Game."""
    name = str(name).capitalize()
    rhyme = [
        f'{name}!',
        f'{name}, {name}, bo {("B" if name[0]!="B" else "") + name[1:]}',
        f'Banana fanna fo {("F" if name[0]!="F" else "") + name[1:]}',
        f'Fee fi mo {("M" if name[0]!="M" else "") + name[1:]}', 
        f'',
        f'{name}!'
    ]
    print('\n'.join(r.center(30, ' ') for r in rhyme))
    return True


def my_sum(*args):
    return sum(args)

