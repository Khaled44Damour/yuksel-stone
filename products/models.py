from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر ($)")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج")
    
    # تصنيف القسم (1: غرانيت، 2: بورسلين، 3: ستانلس)
    category = models.IntegerField(default=1, verbose_name="القسم") 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"