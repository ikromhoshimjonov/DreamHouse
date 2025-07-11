from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from home.models import Home


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
            Home.objects.create(
                name="Toshkent Villa",
                description="Juda chiroyli villa",
                property_code="TV123",
                new_column="Yangi ustun",
                price=Decimal("350000.00"),
                beds=4,
                baths=2,
                volume="450m2",
                build="2021",
                garage=1,
                country="Uzbekistan",
                state="Tashkent",
                area="Chilonzor",
                documents="documents/sample1.pdf",
                latitude=Decimal("41.2995"),
                longitude=Decimal("69.2401"),
                status="sale",
                property="family",
                status_home="villa",
                sale=True
            )

            Home.objects.create(
                name="Boys Uyi",
                description="Yigitlar uchun ijara",
                property_code="BU456",
                new_column="Ijaraga beriladi",
                price=Decimal("1200.00"),
                beds=3,
                baths=1,
                volume="100m2",
                build="2018",
                garage=0,
                country="Uzbekistan",
                state="Samarqand",
                area="Registon",
                documents="documents/sample2.pdf",
                latitude=Decimal("39.6545"),
                longitude=Decimal("66.9750"),
                status="rent",
                property="boys",
                status_home="office",
                sale=False
            )

            Home.objects.create(
                name="Shop City Center",
                description="Savdo do'koni shahar markazida",
                property_code="SC789",
                new_column="Sotuvga qo‘yilgan",
                price=Decimal("80000.00"),
                beds=1,
                baths=1,
                volume="60m2",
                build="2015",
                garage=0,
                country="Uzbekistan",
                state="Bukhara",
                area="Markaz",
                documents="documents/sample3.pdf",
                latitude=Decimal("39.7676"),
                longitude=Decimal("64.4234"),
                status="sale",
                property="family",
                status_home="shop",
                sale=True
            )

            self.stdout.write(self.style.SUCCESS('3 ta Home obyekt yaratildi.'))