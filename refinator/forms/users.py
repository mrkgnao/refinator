from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
        ]

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({'class': 'form-control', })
