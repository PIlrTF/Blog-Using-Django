from django.contrib import admin
from blog.models import Post, Profile, Tag, Comment, Category

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

# ...
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    

    def __str__(self):
        return f"{self.author} on '{self.post}'"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True


    