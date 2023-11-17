from django.db import models

class AppSettings(models.Model):
    domain = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    default_password = models.CharField(max_length=100)
    user_dn = models.CharField(max_length=255, blank=True)
    search_base = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Dynamically set `user_dn` and `search_base` before saving
        self.user_dn = f"CN={self.user},CN=Users," + ",".join([f"DC={dc}" for dc in self.domain.split('.')])
        self.search_base = ",".join([f"DC={dc}" for dc in self.domain.split('.')])
        super(AppSettings, self).save(*args, **kwargs)
