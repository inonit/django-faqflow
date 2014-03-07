from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^auth$', 'faqflow.views.get_auth', name='get_auth'),
    url(r'^question$', 'faqflow.views.get_questions', name='get_questions'),
    url(r'^question/(?P<question_id>\d.+)$', 'faqflow.views.get_question', name='get_question'),
)
