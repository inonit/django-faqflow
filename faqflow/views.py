from __future__ import unicode_literals

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, Http404
from .models import Question, Answer


def json_response(data):
    return HttpResponse(
        json.dumps(data, cls=DjangoJSONEncoder),
        content_type='application/json'
    )


def user(request):

    data = {
        'id': request.user.id,
        'username': unicode(request.user.username),
    }

    return json_response(data)


def questions(request, qid=None):

    if qid:
        try:
            question = Question.objects.get(id=qid)
            data = question.values()
        except:
            raise Http404

    if request.method == 'POST':

        if not qid:
            question = Question()

        data = json.loads(request.body)

        for key, value in data:
            setattr(question, key, value)

        question.save()
        data = question.values()
        return json_response(data)

    if not qid:

        questions = Question.objects.all()
        data = list(questions.values())

    return json_response(data)


def answers(request, qid=None, aid=None):

    if aid:
        try:
            answer = Answer.objects.get(id=aid)
            data = answer.values()
        except:
            raise Http404

    if request.method == 'POST':

        if not aid:
            answer = Answer()

        data = json.loads(request.body)

        for key, value in data:
            setattr(answer, key, value)

        answer.save()
        data = answer.values()

    try:
        question = Question.objects.get(id=qid)
    except:
        raise Http404

    if not aid:

        answers = Answer.objects.filter(parent_id=qid)
        data = list(answers.values())

    return json_response(data)
