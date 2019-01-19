
from django.shortcuts import render, get_object_or_404

from eventex.core.models import Speaker, Talk, Course


def home(request):
    speakers = Speaker.objects.all()
    #speakers = [ {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},{'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'} ]

    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    from django.http import HttpResponse
    speaker = Speaker(name='Henrique Bastos', slug='henrique-bastos', photo='http://hbn.link/hb-pic')
    courses = [
        dict(title='Título do Curso',
             start='09:00',
             description='Descrição do curso.',
             speakers={'all': [speaker]})
    ]

    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        'courses': Course.objects.all(),
        #'morning_talks': Talk.objects.filter(start__lt='12:00'),
        #'afternoon_talks': Talk.objects.filter(start__gte='12:00')
        #'morning_talks': [Talk(title='Título da Palestra', start='10:00', description='Descrição da palestra.')],
        #'afternoon_talks': [Talk(title='Título da Palestra', start='13:00', description='Descrição da palestra.')]
    }

    return render(request, 'core/talk_list.html', context)

