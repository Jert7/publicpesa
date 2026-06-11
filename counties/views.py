from django.shortcuts import get_object_or_404, render
from .models import County, Project, Tender
def homepage(request):
    counties =County.objects.all()
    return render(request,'counties/homepage.html',{'counties':counties})

def county_detail(request, county_id):
    county = get_object_or_404(County, id=county_id)
    tenders = Tender.objects.filter(county=county)
    projects = Project.objects.filter(county=county)
    return render(request, 'counties/county_detail.html',{
        'county': county,
        'tenders': tenders,
        'projects': projects
    })


# Create your views here.
