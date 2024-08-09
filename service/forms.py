from django.contrib.auth.forms import UserCreationForm

from service.models import Cook


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", )
