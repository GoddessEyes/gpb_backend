import logging

from django.core.management.base import BaseCommand
from faker import Faker

from breathtaking.modules.ideas.models import IdeaComment, IdeaOffer, Tag, Theme


loggger = logging.getLogger(__name__)
fake = Faker()


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        loggger.warning('Старт генерации Тем')
        [Theme.objects.get_or_create(name=fake.name()) for _ in range(1, 20)]
        loggger.warning('Старт генерации Тэгов')
        [Tag.objects.get_or_create(name=fake.name()) for _ in range(1, 20)]
        loggger.warning('Старт генерации Предложений идей')
        idea_offers = [IdeaOffer.objects.get_or_create(
            user_id=1,
            theme=fake.text(10),
            description=fake.text(),
            status=0
        ) for _ in range(1, 20)]
        [idea.tags.set(
            Tag.objects.values_list('id', flat=True)[1:10:2]
        ) for idea, _ in idea_offers]
        [idea.themes.set(
            Theme.objects.values_list('id', flat=True)[1:10:2]
        ) for idea, _ in idea_offers]

        loggger.warning('Старт генерации комментариев к идеям')
        [IdeaComment.objects.get_or_create(
            user_id=1,
            idea_id=idea.id,
            comment=fake.text()
        ) for idea, _ in idea_offers]
        loggger.warning('Успех!')
