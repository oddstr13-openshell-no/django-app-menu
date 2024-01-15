from django.db import models


# Create your models here.
class MenuItem(models.Model):
    order = models.IntegerField(default=1)

    url = models.CharField(
        max_length=512
    )  # longer urls than this is unlikley in the menu
    title = models.CharField(
        max_length=60
    )  # a 60 characters long menu item title is way too long

    DISABLED = 0
    ANYONE = 1
    ANONYMOUS = 2
    USERS = 3
    MODERATORS = 4
    ADMINS = 5

    VISIBILITY_CHOICES = (
        (DISABLED, "Disabled"),
        (ANYONE, "Anyone"),
        (ANONYMOUS, "Anonymous"),
        (USERS, "Users"),
        (MODERATORS, "Moderators"),
        (ADMINS, "Admins"),
    )

    visibility = models.PositiveSmallIntegerField(
        choices=VISIBILITY_CHOICES, default=ANYONE
    )
