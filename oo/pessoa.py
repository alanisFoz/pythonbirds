class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
      self.idade = idade
      self.nome = nome
      self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

    def cumprimentar(self):
        return f'Óla {id(self)}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}.Aperto de mão'

class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
    chuck = Mutante(nome='Chuck')
    red = Homem(chuck, nome='Red')
    print(Pessoa.cumprimentar(red))
    print(id(red))
    print(red.cumprimentar())
    print(red.nome)
    print(red.idade)
    for filho in red.filhos:
        print(filho.nome)
    red.sobrenome = 'Rage'
    del  red.filhos
    red.olhos = 1
    del red.olhos
    print(red.__dict__)
    print(chuck.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(red.olhos)
    print(chuck.olhos)
    print(id(Pessoa.olhos), id(red.olhos), id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), red.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), red.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(chuck, Pessoa))
    print(isinstance(chuck, Homem))
    print(chuck.olhos)
    print(red.cumprimentar())
    print(chuck.cumprimentar())
