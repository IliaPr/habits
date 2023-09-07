from django.db import models
from django.core.validators import MaxValueValidator

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    action = models.CharField(max_length=500, verbose_name='действие') 
    place = models.CharField(max_length=150, verbose_name='место')  
    starting_time = models.TimeField(verbose_name='время начала')
    execution_time = models.IntegerField(validators=[MaxValueValidator(120)], verbose_name='время на выполнение в сек.') 
    interval = models.IntegerField(validators=[MaxValueValidator(7)], default=1, verbose_name='периодичность выполнения - раз в ... дней')
    reward = models.CharField(max_length=500, **NULLABLE, verbose_name='вознаграждение') 
    bound_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('action',)

    def __str__(self):
        return self.action
