from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # Meta 클래스는 TimeStampedModel이 실제 DB에 생성되는게 아니라 다른 클래스에서 상속받기 위해서 사용함.
    class Meta:
        abstract = True
