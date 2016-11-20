

#create pages
from cookbook.models import Page
p = 1
i = 2146
while i <= 2405:
    page = Page(page_number = p, img_sm_url='https://s3-us-west-1.amazonaws.com/lovefamily/cookbook/IMG_%s.jpg' % i, img_lg_url='https://s3-us-west-1.amazonaws.com/lovefamily/cookbook/IMG_%s.jpg' % i)
    i += 1
    p += 1
    page.save()
