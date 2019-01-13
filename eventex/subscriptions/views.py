from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        #sender_user = 'app119176526@heroku.com'
        sender_user = 'contato@eventex.com.br'


        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                 form.cleaned_data)

            mail.send_mail('Confirmação de inscrição', body, sender_user,
                           ['contato@eventex.com.br', form.cleaned_data['email']])

            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, "subscriptions/subscription_form.html", context)


