import csv
from django.core.management.base import BaseCommand
from livros.models import Autor, Livro

class Command(BaseCommand): # comando customizado do Django
    help = 'Importa livros de um arquivo CSV' # descrição do comando
    
    def add_arguments(self, parser): # adiciona argumentos ao comando
        parser.add_argument('base_livros', type=str) # argumento para o caminho do arquivo CSV
        
    def handle(self, *args, **kwargs): # lógica de importação
        with open(kwargs['base_livros'], newline='', encoding='utf-8') as csvfile: # abre o arquivo CSV
            reader = csv.DictReader(csvfile) # lê o CSV como dicionários
            for row in reader: # para cada linha do CSV
                autor_nome = row['autor'] # obtém o nome do autor
                autor, _ = Autor.objects.get_or_create(nome=autor_nome) # obtém ou cria o autor
                Livro.objects.get_or_create( # cria o livro
                titulo=row['titulo'], # título do livro
                autor=autor, # autor obtido/criado
                isbn=row['isbn'], # código ISBN
                paginas=int(row['paginas']), # número de páginas
                ano=int(row['ano_publicacao']) # ano de publicação
 )
        self.stdout.write(self.style.SUCCESS('Importação concluída!')) # mensagem de sucesso
        
        
