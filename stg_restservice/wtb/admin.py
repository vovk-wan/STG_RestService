from django.contrib import admin
from wtb.models import (
    WtbUser, Wallet, Answer, Article, Quiz, Game, GameResult, Like,
    Publication, Question, Repost, SocialNetwork
)


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, AnswerInline]


admin.site.register(Quiz, QuizAdmin)