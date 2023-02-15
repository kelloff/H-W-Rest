from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    """Car model."""

    brand = models.CharField(
        max_length=50,
        verbose_name="марка"
    )

    model = models.CharField(
        max_length=50,
        verbose_name='модель'
    )

    horsepower = models.PositiveSmallIntegerField(
        verbose_name="лошидиные силы",
        default=300,
    )
    owner = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2
    )
    class Meta:
        ordering = (
            '-horsepower',
        )
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
    
    def save(
        self,
        *args,
        **kwargs
    ) -> None:
        self.full_clean()
        return super().save(*args , **kwargs)
