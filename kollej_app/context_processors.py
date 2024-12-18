from .models import DirectionsModel

def directions(request):
    directions = DirectionsModel.objects.all()
    return {"directions":directions}