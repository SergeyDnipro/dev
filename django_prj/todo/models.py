from django.db import models


class ToDoDate(models.Model):
    date = models.DateField(null=False, max_length=10)
    comment = models.CharField(null=True, max_length=200)

    def __str__(self):
        return f'{self.date}'


class Items(models.Model):
    group = models.ForeignKey(ToDoDate, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=200, null=False)

    class Meta():
        ordering = ('group__date',)

    class Order():
        important = 'Important'
        common = 'Common'
        All = (important, common)
        All_Django = ((x, x) for x in All)

    order = models.CharField(
        max_length=20,
        choices=Order.All_Django,
        default=Order.common
    )

    class Status():
        done = 'Done'
        in_process = 'In process'
        na = 'N/A'
        All = (done, in_process)
        All_Django = ((x, x) for x in All)

    status = models.CharField(
        max_length=20,
        choices=Status.All_Django,
        default=Status.na
    )

    def __str__(self):
        return f' DATE:{self.group.date}   TODO:{self.name.ljust(30)}   STATUS:{self.status.ljust(15)}  ID:{self.id} \n'


# Create your models here.
