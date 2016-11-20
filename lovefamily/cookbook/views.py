from django.shortcuts import get_object_or_404, render
from .models import Document, Page

# Create your views here.


from django.http import HttpResponse


def index(request):

    pages = None
    error_message = None
    search_terms = ''

    try:
        search_terms = request.POST['search_terms']
        pages = Page.objects.filter(search_text__icontains=request.POST['search_terms'])
        if not pages:
            error_message = "Search returned no results."
    except (KeyError):
        pass

    if not pages:
        pages = Page.objects.all()
    return render(request, 'cookbook/index.html', {'pages': pages, 'error_message': error_message, 'search_terms': search_terms})

def page(request, page_id=None):
    page = get_object_or_404(Page, page_number=page_id)
    return render(request, 'cookbook/page.html', {'page': page})

