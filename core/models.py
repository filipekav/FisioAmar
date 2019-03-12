from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    foto = models.ImageField(upload_to='images/profile_image', default='images/avatar/avatar-2.png', null=True, blank=True)


class Casa_de_Apoio(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    foto = models.ImageField(upload_to='images/profile_image', default='images/gallary/casa-de-apoio.jpg', null=True, blank=True)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    SEX_CHOICES = (('F', 'Feminino'), ('M', 'Masculino'))
    nome = models.CharField(max_length=200)
    nacimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    foto = models.ImageField(upload_to='images/profile_image', default='images/avatar/avatar-5.png', null=True, blank=True)
    casa = models.ForeignKey(Casa_de_Apoio, on_delete=models.PROTECT)
    alertaPA = models.BooleanField(default=False)
    alertaGlicemia = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Log(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    acao = models.CharField(max_length=100)
    user = models.CharField(max_length=100)


class Visita(models.Model):
    ResultadosTestes1 = (('Normal', 'Normal'), ('Diminuido', 'Diminuido'))
    ResultadosTestes2 = (('Positivo', 'Positivo'), ('Negativo', 'Negativo'))
    ResultadosTestes3 = (('Normal', 'Normal'), ('Equilibrio Alterado', 'Equilibrio Alterado'))

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data = models.DateField()

    altura = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    imc = models.FloatField(null=True, blank=True)
    resultadoImc = models.CharField(max_length=20, null=True, blank=True)

    pa = models.CharField(max_length=10, null=True,blank=True)
    glicemia = models.IntegerField(null=True, blank=True)

    estesiometroMaos = models.CharField(max_length=100, null=True, blank=True)
    estesiometroPeDireito = models.CharField(max_length=100, null=True, blank=True)
    estesiometroPeEsquerdo = models.CharField(max_length=100, null=True, blank=True)

    reflexoPatelarDireito = models.CharField(max_length=15, choices=ResultadosTestes1, null=True, blank=True)
    reflexoPatelarEsquerdo = models.CharField(max_length=15, choices=ResultadosTestes1, null=True, blank=True)
    reflexoTricipitalDireito = models.CharField(max_length=15, choices=ResultadosTestes1, null=True, blank=True)
    reflexoTricipitalEsquedo = models.CharField(max_length=15, choices=ResultadosTestes1, null=True, blank=True)

    cordIdxIdxOpen = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)
    cordIdxNazOpen = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)
    cordIdxIdx = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)
    cordIdxNaz = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)
    cordDiadococinesia = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)
    cordCalcanharJoelho = models.CharField(max_length=15, choices=ResultadosTestes2, null=True, blank=True)

    tinetti = models.IntegerField(null=True, blank=True)
    GetUpAndGo = models.CharField(max_length=20, choices=ResultadosTestes3, null=True, blank=True)
