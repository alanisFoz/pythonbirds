class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
      self.idade = idade
      self.nome = nome
      self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla {id(self)}'


if __name__ == '__main__':
    chuck = Pessoa(nome='Chuck')
    red = Pessoa(chuck, nome='Red')
    print(Pessoa.cumprimentar(red))
    print(id(red))
    print(red.cumprimentar())
    print(red.nome)
    print(red.idade)
    for filho in red.filhos:
        print(filho.nome)
    red.sobrenome = 'Rage'
    del  red.filhos
    print(red.__dict__)
    print(chuck.__dict__)