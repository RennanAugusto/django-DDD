from django.db import models


class InvestimentoModel(models.Model):
    id = models.AutoField(primary_key=True)
    valor_investimento = models.DecimalField(max_digits=10, decimal_places=2)
    valor_retorno = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'pix'
        db_table = 'investimento'
