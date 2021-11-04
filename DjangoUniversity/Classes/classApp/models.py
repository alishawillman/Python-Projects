from django.db import models

# Creating objects of djangoClasses
TYPE_CHOICES = {
    ('Beginner Python', 'Beginner Python'),
    ('Intermediate Python', ' Intermediate Python'),
    ('Advanced Python', 'Advanced Python'),
    ('Beginner JavaScript', 'Beginner JavaScript'),
    ('Intermediate JavaScript', 'Intermediate JavaScript'),
    ('Advanced JavaScript', 'Advanced JavaScript'),
    ('Beginner HTML/CSS', 'Beginner HTML/CSS'),
    ('Intermediate HTML/CSS', 'Intermediate HTML/CSS'),
    ('Advanced HTML/CSS', 'Advanced HTML/CSS'),

}

# Creating class djangoClasses
class djangoClasses(models.Model):
    Title = models.CharField(max_length=50, choices=TYPE_CHOICES)
    Course_Number = models.IntegerField(default="100", blank=True)
    Instructor_Name = models.CharField(max_length=50, default="", null=False)
    Duration = models.FloatField(max_length=10, default="1.00", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Title

