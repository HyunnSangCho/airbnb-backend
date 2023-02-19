from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta 를 선언함으로써, 다른 모델들이 상속 받을수 있는 모델이 됨
    class Meta:
        abstract = True
