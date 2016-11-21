from django.shortcuts import get_object_or_404, render
from .models import Page


def index(request):
    pages = None
    error_message = None
    search_terms = None

    try:
        search_terms = request.POST['search_terms']
        pages = Page.objects.filter(search_text__icontains=request.POST['search_terms'])
        if search_terms and not pages:
            error_message = "'%s' not found." % search_terms
    except KeyError:
        pass

    if not pages:
        pages = Page.objects.all()
    return render(request, 'cookbook/index.html',
                  {'pages': pages, 'error_message': error_message, 'search_terms': search_terms})


def page(request, page_id=None):
    page = get_object_or_404(Page, page_number=page_id)
    return render(request, 'cookbook/page.html', {'page': page})
