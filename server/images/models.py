from django.db import models


class Image(models.Model):
    picture = models.ImageField()
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classifed at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))

    def save(self, *args, **kwargs):
        try:
            print('Success')
        except Exception as e:
            print(f"Classification Failed {e}")
        super().save(*args, **kwargs)