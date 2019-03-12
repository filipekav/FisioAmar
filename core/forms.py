from django.forms import *
from core.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'foto']
        widgets = {
            'password': PasswordInput(),
            'foto': FileInput(attrs={'class': 'dropify'})
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserFormEdit(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'foto']
        widgets = {
            'password': PasswordInput(),
            'foto': FileInput(attrs={'class': 'dropify'})
        }


class LarForm(ModelForm):
    class Meta:
        model = Casa_de_Apoio
        fields = ['nome', 'endereco', 'telefone', 'foto']
        widgets = {
            'foto': FileInput(attrs={'class': 'dropify'})
        }

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'nacimento', 'sexo', 'foto', 'casa', 'alertaPA', 'alertaGlicemia']
        labels = {
            'nome': 'Nome Completo',
            'nacimento': 'Data de Nacimento',
            'casa': 'Casa de Apoio',
            'alertaPA': 'Alerta Pressão Arterial',
            'alertaGlicemia': 'Alerta Glicemia',
        }
        widgets = {'nacimento': DateInput(attrs={'class':'datepicker'}),
                   'foto': FileInput(attrs={'class':'dropify'}),
                   }

class VisitaForm(ModelForm):
    class Meta:
        model = Visita

        fields = ['paciente','data', 'altura', 'peso', 'imc', 'resultadoImc', 'pa', 'glicemia', 'estesiometroMaos', 'estesiometroPeDireito', 'estesiometroPeEsquerdo',
                  'reflexoPatelarDireito', 'reflexoPatelarEsquerdo', 'reflexoTricipitalDireito', 'reflexoTricipitalEsquedo', 'cordCalcanharJoelho', 'cordDiadococinesia',
                  'cordIdxIdx', 'cordIdxIdxOpen', 'cordIdxNaz', 'cordIdxNazOpen', 'tinetti', 'GetUpAndGo']
        exclude = ('paciente','imc','resultadoImc',)
        widgets = {
                'data': DateInput(attrs={'class':'datepicker'}),
                'altura': NumberInput(attrs={'placeholder':"Metros"}),
                'peso': NumberInput(attrs={'placeholder':"Kilos"})
                   }
    def getimcAv(self,imc):
        imc = float(imc)
        if imc < 18.5:
            return 'Abaixo do Peso'
        elif imc >= 18.5 and imc < 25:
            return 'Peso Ideal'
        elif imc >= 25 and imc < 30:
            return 'Sobrepeso'
        elif imc >= 30 and imc < 40:
            return 'Obesidade'
        elif imc >= 40:
            return 'Obesidade Mórbida'

    def getimc(self, peso, altura):
        imc = float(peso) / float(altura) ** 2
        return format(imc, '.2f')

    def save(self, commit=True):
        visita = super(VisitaForm, self).save(commit=False)
        imc = self.getimc(visita.peso, visita.altura)
        visita.imc = imc
        visita.resultadoImc = self.getimcAv(imc)
        return visita
