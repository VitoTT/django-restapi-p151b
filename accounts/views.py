from django.views.generic.edit import CreateView
from .models import User
from .forms import UserCreateForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = '/'
