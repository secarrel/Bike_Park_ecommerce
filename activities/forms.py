from django import forms
from timeslots.models import Timeslot
from .widgets import CustomClearableFileInput
from .models import Activity, Category


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
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class TimeslotForm(forms.ModelForm):

    class Meta:
        model = Timeslot
        exclude = ['spaces_booked', 'available_capacity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        activities = Activity.objects.all()

        self.fields['activity'].queryset = activities
        self.fields['start_time'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
