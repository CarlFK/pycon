from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse 

from cStringIO import StringIO

from dabo.dReportWriter import dReportWriter

# from models import Country
from symposion.proposals.models import Proposal 

from datetime import datetime 

import os

# @login_required
def mk_pdf(request, proposal_id, rfxml='test.rfxml'):

    """
    Generates a pdf 
    layout defined by rfxml
    """

    proposal=get_object_or_404(Proposal,id=proposal_id)
    proposals = [proposal]

    base  = os.path.dirname(__file__)
    rfxmlfile  = os.path.join(base,'templates', rfxml+".rfxml")
     
    # buffer to create pdf in
    buffer = StringIO()

    ds=[]
    for proposal in proposals:
        ds.append({
            "letter_date": datetime.today(),
            "talk_title": proposal.title,
            'applicant_name':proposal.speaker.name,
            "applicant_country":proposal.speaker.country.name,
            "consulate_city":proposal.speaker.country.consulate_city,
          })
        
    # generate the pdf in the buffer, using the layout and data
    rw = dReportWriter(
            OutputFile=buffer, ReportFormFile=rfxmlfile, Cursor=ds)
    rw.write()

    # get the pdf out of the buffer
    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(mimetype='application/pdf')
    filename = '_'.join( [proposal.speaker.name, rfxml] )
    response['Content-Disposition'] = 'filename=%s.pdf' % ( filename )
    response.write(pdf)
    return response
