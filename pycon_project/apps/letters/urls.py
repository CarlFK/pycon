from django.conf.urls.defaults import url, patterns

from views import *

urlpatterns = patterns(
    'letters.views',
     url(r'(?P<rfxml>\w+)/(?P<proposal_id>\w+)/.*$', 
        mk_pdf, name='mk_pdf'),

)

