from django.contrib import admin
from .models import Review
from rooms.models import Room

class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [("좋아요", "좋아요"), ("별로", "별로"), ("시설", "시설"),]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )