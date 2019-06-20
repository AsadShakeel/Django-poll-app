from polls.models import Choice, Question
from django.utils import timezone

Question.objects.all()
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

q.id

