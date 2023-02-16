from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Comics(models.Model):
    """Book for temp project"""

    title = models.CharField(
        verbose_name="comics",
        max_length=200
    )
    # author = models.ForeignKey(
    #     to=User,
    #     on_delete=models.CASCADE
    # )
    # description = models.TextField(
    #     verbose_name='description'
    # )
    image = models.ImageField(
        verbose_name='image',
        upload_to='images/'
    )
    price = models.DecimalField(
        verbose_name='price',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'comics'
        verbose_name_plural = 'comicses'

    def __str__(self) -> str:
        return f"{self.title} | {self.price}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def clean(self) -> None:
        if (
            self.price <= 0
        ) and (
            not self.price
        ):
            raise ValidationError(
            "Price is zero!"
        )
        return super().clean()