from django.db import models


class Window(models.Model):
    name = models.CharField(max_length=255)
    dl = models.CharField(max_length=255, blank=True, null=True)
    sh = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


#class Review(models.Model):
 #   text = models.TextField()
  #  book = models.ForeignKey(Book, on_delete=models.CASCADE)

   # def __str__(self):
    #    return self.text