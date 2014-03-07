from __future__ import unicode_literals

from django.http import HttpResponse
import simplejson as json
from .models import Question, Answer

def get_auth(request):

    data = {
        'id': request.user.id,
    }

    return HttpResponse(json.dumps(data), content_type='application/json')

def get_questions(request):

    questions = Question.objects.all()
    data = {
        'status': 'ok',
        'question_count': questions.count()
        'questions': []
    }
    for question in questions:
        data['questions'].append({
            'id': question.id,
            'title': question.title,
            'author': question.author,
            'created_at': question.created_at,
            'changed_at': question.changed_at,
        })

    return HttpResponse(json.dumps(data), content_type='application/json')

def get_question(request, question_id=None):

    try:
        question = Question.objects.get(id=question_id)
        answers = Answer.objects.filter(parent_id=question_id)
        data = {
            'status': 'ok',
            'question': question.values(),
            'answer_count': answers.count()
            'answers': answers.values(),
        }
    except:
        data = {
            'status': 'Question not found',
        }

    return HttpResponse(json.dumps(data), content_type='application/json')

def post_question(request, question_id=None):

    try:
        data = json.loads(request.POST)
        question, created = Question.objects.get_or_create(id=question_id)

        for key, value in data:
            setattr(question, key, value)

    except:
        data = {
            'status': 'Question not found',
        }

    return HttpResponse(json.dumps(data), content_type='application/json')

def post_answer(request, question_id=None, answer_id=None):

    try:
        data = json.loads(request.POST)
        answer, created = Answer.objects.get_or_create(id=answer_id)

        for key, value in data:
            setattr(answer, key, value)

    except:
        data = {
            'status': 'Answer not found',
        }

    return HttpResponse(json.dumps(data), content_type='application/json')
