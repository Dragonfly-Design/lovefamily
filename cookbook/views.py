from django.db.models import F, Q, Count
from django.shortcuts import get_object_or_404, render
from .models import Document, Page

def index(request):

    pages = None
    error_message = None
    search_terms = None

    try:
        search_terms = request.POST['search-terms']

        # Split the search string into individual terms, and then filter based on each term
        # This effectively creates an AND query with each term, finding only products containing all terms
        search_tokens = search_terms.split(' ')
        pages = Page.objects.all()
        for search_token in search_tokens:
            pages = \
                (pages
                    .filter(Q(title__icontains=search_token) |
                            Q(manual_search_text__icontains=search_token) |
                            Q(ocr_search_text__icontains=search_token))
                    .order_by('page_number'))

        if search_terms and not pages:
            error_message = "'%s' not found." % search_terms

    except (KeyError):
        error_message = "Please enter search terms"

    if not pages:
        pages = Page.objects.all()
    return render(request, 'cookbook/index.html', {'pages': pages, 'error_message': error_message, 'search_terms': search_terms})

def page(request, page_id=None):
    page = get_object_or_404(Page, page_number=page_id)
    return render(request, 'cookbook/page.html', {'page': page})
