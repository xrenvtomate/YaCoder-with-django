from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
