from django.contrib.auth import login
from django.views.generic import CreateView
from ..forms import CivicSignUpForm
from ..models import User

class CivicSignUpView(CreateView):
    model = User
    form_class = CivicSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'civic'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')
