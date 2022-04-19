from django.db import models


class Cheese(models.Model):
    slug = models.SlugField(primary_key=True, max_length=200)
    name = models.CharField(unique=True, max_length=200)
    description = models.TextField(blank=True)
    country_of_origin = models.CharField(max_length=200)
    fat_content = models.FloatField(null=True)
    last_updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["name"]
        get_latest_by = "last_updated"

    def __str__(self):
        return self.name

    def is_high_fat(self):
        if self.fat_content is None:
            return False
        return self.fat_content >= 50.0
