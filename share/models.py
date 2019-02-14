from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=8)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    source = models.ForeignKey(User,related_name="subscription_user", on_delete=models.CASCADE)
    target = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.source.name) + " takes subscription to " + str(self.target.name)


class Image(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    def __str__(self):
        return "Image " + self.serial_number + " : " + self.description


class Port(models.Model):
    port_number = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Port : " + str(self.port_number) + " status : " + ("ON USE" if self.status else "OFF")


class Container(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return "Container created by " + self.user.name + ", using " + self.image.serial_number
