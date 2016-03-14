from django.conf.urls import url 
from .views import * 

urlpatterns = [
    url(r'sarah$', sarah_page, name="sarah"), 
    url(r'question(?P<question_id>[0-9]+)', question_details, name="question_details")

]