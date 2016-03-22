from django.conf.urls import url
from .views import *


urlpatterns = [

    #no need to say views.port_home because of the 'import *' above
    url(r'^$', port_home), 


    # url(r'^myfriend', hello)
    # url(r'^adele', view.adele) (don't need view)
]