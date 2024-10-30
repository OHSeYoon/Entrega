from django.core.management.base import BaseCommand
from myapp.models import DistanceCalculation

class Command(BaseCommand):
    help = 'Runs a custom query on DistanceCalculation model'

    def handle(self, *args, **options):
        # Define and run the query
        all_calculations = DistanceCalculation.objects.all()
        for calculation in all_calculations:
            self.stdout.write(
                f"Start: {calculation.start_address}, "
                f"End: {calculation.end_address}, "
                f"Distance: {calculation.distance_km} km"
            )