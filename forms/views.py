from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from .forms import DrillModelForm

# from django.template import loader
from .models import Choice, Question, Drilling
# Create your views here.

# def index(request):
    # return HttpResponse("Hello, world. You're at the forms index.")
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'forms/index.html')

def index(request):
    context = {
        'form': DrillModelForm(),
        'radio_form': ['drilling', 'drilling_exchange', 'StartEnd']
    }
    # debug
    print(context['form'].fields)
    return render(request, 'forms/index.html', context)

@require_POST
def save(request):
    form = MemberModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('forms:index')
 
    context = {
        'form': form,
    }
    return render(request, 'forms/index.html', context)

def comp(request):

    try:
        form_data = request.POST
    except (KeyError, form_data.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'forms/index.html', {
            'error_message': "もう一度入力してください。",
        })
        # raise Http404("Form does not exist")
    print(form_data)

    # return HttpResponse("Hello, world. You're at the forms index.")

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'forms/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'forms/detail.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'forms/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('forms:results', args=(question.id,)))

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'forms/results.html', {'question': question})
