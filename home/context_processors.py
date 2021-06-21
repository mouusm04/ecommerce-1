from .models import Product, SubCatagory, Catagory

def navigation(request):
    catagories = Catagory.objects.all()
    subcatagories = SubCatagory.objects.all()

    return {
        "catagories": catagories,
        "subcatagories": subcatagories
    }
