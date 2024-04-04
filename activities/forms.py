from django import forms
from timeslots.models import Timeslot
from django.core.exceptions import ValidationError
from .models import Activity, Category

class DurationInput(forms.TextInput):
    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            # Check if the value is in the format HH:MM
            parts = value.split(':')
            if len(parts) == 2:
                try:
                    hours = int(parts[0])
                    minutes = int(parts[1])
                    if 0 <= hours <= 23 and 0 <= minutes <= 59:
                        # Return the value in HH:MM:00 format
                        return f'{hours:02d}:{minutes:02d}:00'
                except ValueError:
                    pass
            raise ValidationError('Invalid duration format. Please use HH:MM format.')

        return value
    
class ActivityForm(forms.ModelForm):
    duration = forms.CharField(label='Duration', required=True, widget=DurationInput(attrs={'placeholder': 'HH:MM'}))
    
    class Meta:
        model = Activity
        fields = '__all__'

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
        self.fields['start_time'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
