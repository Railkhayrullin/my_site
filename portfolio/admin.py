from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MyInfo, MyHobby, PersonalQualities, MySkills, Education, Work, Certifications, Projects,\
    ContactMe, SocialNetwork, ProjectsCategory


@admin.register(MyInfo)
class MyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'email')
    list_display_links = ('name',)

    def has_add_permission(self, request):
        """Функция не дает добавлять объектов больше, чем 'max_objects' """
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)


@admin.register(MyHobby)
class MyHobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(PersonalQualities)
class PersonalQualitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'good_or_bad')
    list_display_links = ('name',)
    list_editable = ('good_or_bad',)


@admin.register(MySkills)
class MySkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'assessment')
    list_display_links = ('name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_for', 'date_to')
    list_display_links = ('name',)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'position', 'date_for', 'date_to')
    list_display_links = ('organisation',)


@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'assessment', 'date', 'is_education')
    list_display_links = ('name',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="80">')
    get_image.short_description = 'изображение'


@admin.register(ContactMe)
class ContactMe(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('name',)


@admin.register(SocialNetwork)
class SocialNetwork(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(ProjectsCategory)
class ProjectsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.site_title = 'Хайруллин Раиль'
admin.site.site_header = 'Хайруллин Раиль'
