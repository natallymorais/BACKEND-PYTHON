from django.db import models

# Tabela Pessoa (registro de contato)
class Pessoas(models.Model):
    nome = models.CharField(max_length=100) # nome
    email = models.EmailField(unique=True) # e-mail (único)
    telefone = models.CharField(max_length=20) # telefone
    cidade = models.CharField(max_length=100) # cidade
    
    
    def __str__(self):
        return self.nome # texto representa
