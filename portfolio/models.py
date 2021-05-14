from django.db import models


class MyInfo(models.Model):
    """Информация обо мне"""
    name = models.CharField("имя", max_length=50, blank=False)
    surname = models.CharField("фамилия", max_length=50, blank=False)
    address = models.CharField("адрес", max_length=100, default='')
    phone = models.CharField("телефон", max_length=15, blank=False)
    email = models.EmailField("email", max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "информация обо мне"
        verbose_name_plural = "информация обо мне"


class MyHobby(models.Model):
    """Мои хобби и увлечения"""
    name = models.CharField("хобби/увлечения", max_length=100, blank=False)
    description = models.TextField("описание", max_length=300, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'мои хобби и увлечения'
        verbose_name_plural = 'мои хобби и увлечения'


class PersonalQualities(models.Model):
    """Мои достоинства/недостатки"""
    name = models.CharField("достоинство/недостаток", max_length=100, blank=False)
    description = models.TextField("описание", max_length=300, blank=False)
    good_or_bad = models.BooleanField("это достоинство?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-good_or_bad']
        verbose_name = "мои достоинства/недостатки"
        verbose_name_plural = "мои достоинства/недостатки"


class MySkills(models.Model):
    """Мои навыки"""
    name = models.CharField("мой навык", max_length=100, blank=False)
    description = models.TextField("описание", max_length=300, blank=False)
    assessment = models.PositiveSmallIntegerField("оценка навыка", default=50)
    icon = models.CharField("Иконка Font Awesome", max_length=50, default="fa fa-check-square-o")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "мой навык"
        verbose_name_plural = "мои навыки"


class Education(models.Model):
    """Мое образование"""
    name = models.CharField("учебное заведение", max_length=100, blank=False)
    date_for = models.DateField("дата начала учебы", max_length=10, blank=False)
    date_to = models.DateField("дата окончания обучения", max_length=10, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "мое образование"
        verbose_name_plural = "мое образование"


class Work(models.Model):
    """Карьера"""
    organisation = models.CharField("имя организации", max_length=100, blank=False)
    position = models.TextField("должность", max_length=100, blank=False)
    date_for = models.DateField("дата начала работы", max_length=10, blank=False)
    date_to = models.DateField("дата окончания работы", max_length=10, default="")

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['-date_to']
        verbose_name = "место работы"
        verbose_name_plural = "место работы"


class Certifications(models.Model):
    """Мои сертификаты"""
    name = models.CharField("сертификат", max_length=100, blank=False)
    assessment = models.TextField("оценка", max_length=50, blank=False)
    image = models.ImageField("изображение", upload_to='certifications', blank=False)
    date = models.DateField("дата получения", max_length=10, blank=False)
    url = models.URLField("ссылка на сертификат", max_length=100, default="https://")
    is_education = models.BooleanField("по образованию?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сертификат"
        verbose_name_plural = "сертификаты"


class ProjectsCategory(models.Model):
    """Категория проектов"""
    name = models.CharField("категория", max_length=100, blank=False)
    slug = models.SlugField("slug", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория проекта"
        verbose_name_plural = "категории проектов"


class Projects(models.Model):
    """Мои проекты"""
    name = models.CharField("имя проекта", max_length=100, blank=False)
    description = models.TextField("описание", max_length=300, blank=False)
    image = models.ImageField("изображение", upload_to='projects/', blank=False)
    category = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE, related_name='category_projects',
                                 verbose_name='категория проекта', default=None)
    url = models.URLField("ссылка на проект", max_length=100, default="https://")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"


class ContactMe(models.Model):
    """Обратная связь"""
    name = models.CharField("имя", max_length=100, blank=False)
    email = models.EmailField("email", max_length=100, blank=False)
    message = models.TextField("сообщение", max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class SocialNetwork(models.Model):
    name = models.CharField("Соцсеть", max_length=100, blank=False)
    icon = models.CharField("Иконка Font Awesome", max_length=50, default="fa fa-check-square-o")
    url = models.URLField("ссылка на сайт", max_length=100, default='https://', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "соцсеть"
        verbose_name_plural = "соцсети"
