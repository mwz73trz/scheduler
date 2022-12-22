from rest_framework.viewsets import ModelViewSet
from .serializer import ScheduleSerializer
from .models import Schedule

class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all().order_by('game_date').values()
    serializer_class = ScheduleSerializer
