from django.db import models


class Link(models.Model):
    full_link = models.TextField(unique=True)
    short_link = models.CharField(max_length=255)
    title = models.CharField(max_length=127, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def click_count(self):
        return self.linkclick_set.count()


class LinkClick(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
