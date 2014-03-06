from __future__ import unicode_literals

from django.http import HttpResponse
import simplejson as json
from .models import Question, Answer

def get_questions(request):

    data = []
    for question in Question.objects.all():
        data.append({
            'title': question.title,
            'author': question.author,
            'created_at': question.created_at,
            'changed_at': question.changed_at,
        })

    return HttpResponse(json.dumps(data), content_type='application/json')

def get_question(request, question_id=None):

    try:
        data = {
            'status': 'ok',
            'question': Question.objects.get(id=question_id).values(),
            'answers': Answer.objects.filter(parent_id=question_id).values(),
        }
    except:
        data = {
            'status': 'Question not found',
        }

    return HttpResponse(json.dumps(data), content_type='application/json')
