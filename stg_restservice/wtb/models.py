from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название игры')
    description = models.TextField(
        max_length=2000, verbose_name='Описание игры')

    class Meta:
        db_table = 'games'
        ordering = ('name', )
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class WtbUser(models.Model):
    roles = (
        ('client', 'Клиент'), ('administrator', 'Администратор'),
        ('leader', 'Руководитель'), ('editor', 'Редактор')
    )
    full_name = models.CharField(max_length=255, verbose_name='Клиент')
    phone_number = models.CharField(
        max_length=11, verbose_name='Номер телефона')
    role = models.CharField(
        max_length=255, choices=roles, verbose_name='Клиент')

    class Meta:
        db_table = 'wtb_users'
        ordering = ('full_name', )
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Wallet(models.Model):
    wtb_user = models.ForeignKey(
        WtbUser, related_name='wtb_user_wallet',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    private_key = models.CharField(max_length=255, verbose_name='Private key')
    public_key = models.CharField(max_length=255, verbose_name='Public key')

    class Meta:
        db_table = 'wallets'
        ordering = ('wtb_user', )
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'


class GameResult(models.Model):
    game = models.ForeignKey(
        Game, related_name='game_result',
        verbose_name='Игра',
        on_delete=models.CASCADE
    )
    ranking_position = models.IntegerField(verbose_name='Позиция в рейтинге')
    prize = models.IntegerField(verbose_name='Приз')

    class Meta:
        db_table = 'game_results'
        ordering = ('game', )
        verbose_name = 'Результат игры'
        verbose_name_plural = 'Результаты игр'


class Article(models.Model):
    caption = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')

    class Meta:
        db_table = 'articles'
        ordering = ('caption', )
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Like(models.Model):
    wtb_user = models.ForeignKey(
        WtbUser, related_name='user_like',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        WtbUser, related_name='article_like',
        verbose_name='Статья',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'likes'
        ordering = ('article', )
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Publication(models.Model):
    caption = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    link = models.URLField(verbose_name='Ссылка на публикацию')

    class Meta:
        db_table = 'publications'
        ordering = ('caption', )
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, verbose_name='Социальная сеть')
    repost_link = models.URLField(verbose_name='Репост')

    class Meta:
        db_table = 'social_network'
        ordering = ('name', )
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальная сети'


class Repost(models.Model):
    wtb_user = models.ForeignKey(
        WtbUser, related_name='wtb_user_repost',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    publication = models.ForeignKey(
        Publication, related_name='publication_repost',
        verbose_name='Публикация',
        on_delete=models.CASCADE
    )
    social_network = models.ForeignKey(
        SocialNetwork, related_name='social_network_repost',
        verbose_name='Социальная сеть',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'reposts'
        ordering = ('wtb_user', )
        verbose_name = 'Репост'
        verbose_name_plural = 'Репосты'


class Quiz(models.Model):
    name = models.CharField(max_length=100, verbose_name='Опрос')

    class Meta:
        db_table = 'quiz'
        ordering = ('name', )
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='quiz_question',
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100, verbose_name='Вопрос')

    class Meta:
        db_table = 'question'
        ordering = ('quiz', )
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(
        Quiz, related_name='question_answer',
        verbose_name='Ответ',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100, verbose_name='Ответ')
    status = models.BooleanField(verbose_name='Верный ответ')

    class Meta:
        db_table = 'answer'
        ordering = ('question', )
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
