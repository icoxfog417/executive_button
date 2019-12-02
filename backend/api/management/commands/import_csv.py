import csv
from django.core.management.base import BaseCommand, CommandError
from api.models import Remuneration


class Command(BaseCommand):
    help = "Import CSV for Remuneration model"

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs="?", type=str)
        parser.add_argument(
            "--refresh",
            action="store_true",
            help="Delete all data before import csv",
        )

    def handle(self, *args, **options):
        if "file_path" in options:
            if options["refresh"]:
                Remuneration.objects.all().delete()

            models = []
            with open(options["file_path"], "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    m = Remuneration(
                        edinet_code=row["edinet_code"],
                        sec_code=row["sec_code"],
                        filer_name=row["filer_name"],
                        doc_description=row["doc_description"],
                        doc_id=row["doc_id"],
                        period_start=row["period_start"],
                        period_end=row["period_end"],
                        amount=int(row["amount"]),
                        number=int(row["number"])
                    )
                    models.append(m)

            Remuneration.objects.bulk_create(models)
            self.stdout.write(self.style.SUCCESS(f"Successfully import {len(models)} remuneration"))
