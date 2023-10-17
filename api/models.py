from django.db import models

class TodoItem(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    user = models.CharField(max_length = 25)

    def __str__(self):
        return self.title
