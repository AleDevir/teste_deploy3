from django.db import models

class Categoria(models.Model):
    '''
    Categoria
    '''
    nome = models.CharField('Categoria', max_length=30)
    
    criado_em = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='', blank=True)
    slug = models.SlugField(default="", null=False)

    
    def __str__(self):
        '''
        str
        '''
        return str(self.nome)
    
    class Meta:
        '''
        Metamodelo
        '''
        db_table = 'categorias'
    
  
