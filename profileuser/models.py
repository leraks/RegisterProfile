from django.db import models
from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    real_name = models.CharField(max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=100,null=True,blank=True)
    main_photo = models.ImageField(upload_to='img/profile', null=True, height_field=None, width_field=None,
                                   max_length=100,blank=True)

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
