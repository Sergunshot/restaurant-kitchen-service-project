from django.contrib.auth.forms import UserCreationForm
from django import forms
from service.models import Cook, Dish, Ingredient


class CookCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by username",
            "class": "form-control",
            "style": "border-bottom-left-radius: 0; border-top-left-radius: 0"
        }
        )
    )


class CookYearsOfExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience", )


class DishForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name",
            "class": "form-control",
            "style": "border-bottom-left-radius: 0; border-top-left-radius: 0"
        }
        )
    )


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name",
            "class": "form-control",
            "style": "border-bottom-left-radius: 0; border-top-left-radius: 0"
        }
        )
    )
