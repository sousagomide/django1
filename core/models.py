from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=255, null=False, blank=False, default='')
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10, null=False, blank=False, default=0.00)
    estoque = models.IntegerField('Quantidade em estoque')
    
    def __str__(self):
        return f'{self.nome} {self.estoque}'

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255, null=False, blank=False, default='')
    sobrenome = models.CharField('Sobrenome', max_length=255, null=True)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
