from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^user$', 'faqflow.views.user', name='user'),
    url(r'^questions$', 'faqflow.views.questions', name='questions'),
    url(r'^questions/(?P<qid>\d+)$', 'faqflow.views.questions', name='questions'),
    url(r'^questions/(?P<qid>\d+)/answers$', 'faqflow.views.answers', name='answers'),
    url(r'^questions/(?P<qid>\d+)/answers/(?P<aid>\d+)$', 'faqflow.views.answers', name='answers'),
    url(r'^test$', TemplateView.as_view(template_name='faqflow/faqflow.html')),
)
