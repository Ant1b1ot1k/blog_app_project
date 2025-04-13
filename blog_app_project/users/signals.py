# Signals provide a way for decoupled applications to get notified when certain events occur.
# They follow an observer (publish/subscribe) pattern, where sender events (like model saves) dispatch notifications to receiver functions.

# signal that gets implemented after an object is saved (used for creating profiles when a user is created in our case)
from django.db.models.signals import post_save
# Sender of the signal
from django.contrib.auth.models import User
# Receiver of the signal
from django.dispatch import receiver
from .models import Profile


# Import the post_save signal and the receiver decorator.
# The post_save signal is sent by Django after a model's save() method is called.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
      This receiver function listens for the post_save signal on the User model.
      Parameters:
      - sender: The model class sending the signal (in this case, User).
      - instance: The actual instance of User that was saved.
      - created: A boolean; True if a new record was created in the User model, False if an existing record was updated.
      - **kwargs: Additional keyword arguments (not used here).
      """
    if created:
        Profile.objects.create(user=instance)


# Import the post_save signal and the receiver decorator.
# The post_save signal is sent by Django after a model's save() method is called.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    This receiver function listens for the post_save signal on the User model and saves the associated Profile for the User.
    Parameters:
    - sender: The model class sending the signal (in this case, User).
    - instance: The actual instance of User that was saved.
    - **kwargs: Additional keyword arguments provided by the signal.
    """
    # save profile when user is saved/updated their profile
    instance.profile.save()

