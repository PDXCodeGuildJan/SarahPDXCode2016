#######################
#we made this one

from django.conf.urls import url
from .views import *

urlpatterns = [

    #no need to say views.port_home because of the 'import *' above
    url(r'^$', render_price_list, name='price_list'), 

]


