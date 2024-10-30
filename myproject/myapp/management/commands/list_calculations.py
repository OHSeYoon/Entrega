from django.core.management.base import BaseCommand
from myapp.models import DistanceCalculation
class Command(BaseCommand):
    help = 'List all distance calculations'

    def handle(self, *args, **kwargs):
        all_calculations = DistanceCalculation.objects.all()
        for calculation in all_calculations:
            self.stdout.write(
                f"Start: {calculation.start_address}, End: {calculation.end_address}, Distance: {calculation.distance_km} km"
            )
