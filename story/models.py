from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Ingredient(models.Model):
    UNIT_CHOICE = (
        (1, _("ml")),
        (2, _("g")),
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    sku_nubmer = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(default=0)
    supplier = models.ForeignKey(
        "supplier.Supplier", on_delete=models.SET_NULL, blank=True, null=True
    )
    unit = models.PositiveSmallIntegerField(
        choices=UNIT_CHOICE,
        default=1,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} — {self.quantity} {self.get_unit_display()}"
