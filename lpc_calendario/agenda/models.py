from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    visivel = models.BooleanField('Público')
    institucional = models.BooleanField('Institucional')
    descricao = models.TextField()
    tipo = models.CharField(max_length = 100)
    usuario = models.ManyToManyField(User, null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.tipo)

class Compromisso(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    dataHoraInicio = models.DateTimeField(blank=True, null=True)
    dataHoraFim = models.DateTimeField(blank=True, null=True)
    agendas = models.ForeignKey(Agenda, null=True, blank=False)

    def __str__(self):
        return "{}".format(self.nome)

class AgendaUsuario(models.Model):
    agenda = models.ForeignKey(Agenda, null=True, blank=False)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return "{}".format(self.agenda.tipo)

class Invite(models.Model):
    dono_evento = models.ForeignKey(User, null=True, blank=False)
    convidado = models.ManyToManyField(User, null=True, blank=False, related_name = "convidados")
    compromissos = models.ForeignKey(Compromisso, null=True, blank=False)
    resposta = models.BooleanField("Aceitar convite!")
