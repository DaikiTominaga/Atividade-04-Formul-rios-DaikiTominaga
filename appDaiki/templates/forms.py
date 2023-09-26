from django import forms

class JogadorMessiForm(forms.Form):
    nome_jogador = forms.CharField(label='Nome do Jogador')
    ano_juntos = forms.IntegerField(label='Ano em que jogaram juntos')
    clube_juntos = forms.CharField(label='Clube em que jogaram juntos')