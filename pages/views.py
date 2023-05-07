from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class Home(FormView):
    template_name = 'home.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            f'Contact message from {name}',
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path
