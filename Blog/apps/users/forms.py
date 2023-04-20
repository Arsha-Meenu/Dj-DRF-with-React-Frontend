from django.forms import Form,ModelForm
from apps.users.models  import CustomUser



class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email')