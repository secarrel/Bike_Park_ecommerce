from django import forms
from timeslots.models import Timeslot
from .widgets import CustomClearableFileInput
from .models import Activity, Category, Review


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
    duration = forms.DurationField(widget=forms.TextInput(
        attrs={'placeholder': 'HH:MM:SS'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class TimeslotForm(forms.ModelForm):

    class Meta:
        model = Timeslot
        exclude = ['spaces_booked', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['start_time'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local'})

    def clean_start_time(self):
        """
        Remove seconds from the date time field to reduce
        validation errors.
        """
        start_time = self.cleaned_data.get('start_time')
        if start_time:
            start_time = start_time.replace(second=0)
        return start_time


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'content', 'activity', 'reviewer']
        widgets = {
            'rating': forms.RadioSelect(choices=Review.RATING_CHOICES),
            'content': forms.Textarea(attrs={'rows': 6}),
            'reviewer': forms.HiddenInput(),
            'activity': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.reviewer = kwargs.pop('reviewer', None)
        super().__init__(*args, **kwargs)
