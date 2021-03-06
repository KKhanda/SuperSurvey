from surveyapp.models import Question, Session

from django.contrib.auth.models import User
User.objects.create_superuser('root', 'admin@example.com', 'qwerty123')

Session.objects.create().save()

Question.objects.create(
    text='What is your favorite programming language',
    type='MC',
    number=1,
    variants=['C#', 'Java', 'Python', 'Go', 'Pascal', 'C++']
).save()

Question.objects.create(
    text='How many years do you write code?',
    type='NR',
    number=2,
    variants=[],
).save()

Question.objects.create(
    text='Where are you from?',
    type='TE',
    number=3,
    variants=[],
).save()
