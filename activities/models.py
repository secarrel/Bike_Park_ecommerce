from django.db import models
from datetime import timedelta
from django.db.models import Avg, Count
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Catgeories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    image = CloudinaryField(
        'category',
        folder='categories',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    @property
    def category_url(self):
        if self.category:
            return self.category.url
        return '/static/images/default_category.svg'


class Activity(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXPERT = 'Expert'
    ANY = 'Any'

    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'Expert'),
        (ANY, 'Any'),
    ]

    class Meta:
        verbose_name_plural = 'Activities'

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    capacity = models.PositiveSmallIntegerField()
    requirements = models.TextField()
    details = models.TextField()
    duration = models.DurationField(default=timedelta)
    image = CloudinaryField(
        'activity',
        folder='activities',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_duration(self):
        if self.duration:
            if self.duration > timedelta(hours=7):
                return "All Day"
            else:
                hours = self.duration.seconds // 3600
                minutes = (self.duration.seconds % 3600) // 60
                if minutes == 0:
                    return f"{hours} hrs"
                else:
                    return f"{hours} hrs {minutes} mins"
        else:
            return None

    def average_rating(self):
        # Get all the reviews associated with this activity
        reviews = Review.objects.filter(activity=self)

        # Calculate the average rating
        average = reviews.aggregate(Avg('rating'))['rating__avg']

        if average is not None:
            round_average = round(average, 1)
            count_average = round_average
            stars = []

            # Display average as stars
            while count_average >= 1:
                count_average -= 1
                stars.append("full")

            if count_average >= 0.25 and count_average <= 0.74:
                stars.append("half")

            return round_average, stars
        else:
            return None

    def review_count(self):
        count = Review.objects.filter(activity=self).count()
        count_per_rating = Review.objects.filter(activity=self).values(
            'rating').annotate(count=Count('id'))
        rating_count = {
            rating['rating']: rating['count'] for rating in count_per_rating}
        return count, rating_count


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    content = models.CharField(max_length=800, null=True, blank=True)
    review_time = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
