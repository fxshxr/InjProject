from django.db import models

# Create your models here.

class Bookings(models.Model):
    title = models.CharField(max_length=150, verbose_name='Столик')
    content = models.TextField(blank=True, verbose_name='Посетитель')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    updated_at = models.DateTimeField(blank=True, verbose_name='Дата посещения')
    is_published = models.BooleanField(default=True, verbose_name='Подтверждение брони')

    def __str__(self) : 
        return self.title

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ['-created_at']
        db_table = "bookings_bookings"
