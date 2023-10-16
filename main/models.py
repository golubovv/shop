from django.db import models
from django.contrib.postgres.fields import \
    ArrayField  # ArrayField необходим для хранения итерируемых объектов python в записях postgresql


# Модель(таблица) покупателей
class Buyers(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фмилия')
    emailad = models.EmailField(verbose_name='поочта')
    numbersTel = models.CharField(unique=True, max_length=10, verbose_name='Телефон')
    shopping_cart = ArrayField(models.CharField(max_length=50), blank=True, verbose_name='корзина покупателя')

    # переопределение стандартного метода,
    # для того чтобы при обращении к объекту модели возвращалось "Фамилия Имя" а не индификатор
    def __str__(self):
        name_2name = self.last_name + ' ' + self.first_name
        return name_2name

    # Этот класс нужен для "человеческого отображения в админке"
    # Кое-что нужно поправить
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['first_name']  # Тут нужно переделать так чтобы отображалась Имя Фамилия


# Модель(таблица) Заказов
# Поле "список цен" заменено на price_good - Цена товара.
# В поле price_good, должна быть зафиксирована цена на товар когда произошла оплата заказа
class Orders(models.Model):
    order_numb = models.CharField(unique=True, max_length=50, verbose_name='Номер заказа')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status_order = models.CharField(max_length=50, verbose_name='Статус заказа')
    goods_order = models.ManyToManyField('Goods', verbose_name='Товары')
    orders_buy = models.ForeignKey('Buyers', null=True, verbose_name='покупатель', on_delete=models.PROTECT)
    price_good = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена товара')

    def __str__(self):
        return self.order_numb

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['order_date']


# Создаю функцию для того чтобы фото сохранядись в следующем порядке
# media/'pk_goods_name'
def get_path_save1(instance, filename):
    str1 = '{0}_{1}\\{2}'.format(instance.goods_name, instance.brend, filename)       # Незнаю правильно ли записано
    return str1


# Модель(таблица) Товаров
# Добавленно поле available - Доступен товар для продажи и поиска.
# Добавленно поле opisanie - Описание товара
# Добавлено 8штук полей для фото товаров
class Goods(models.Model):
    goods_name = models.CharField(max_length=150, verbose_name='Наименование товара')
    shop_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена товара')
    brend = models.ForeignKey('Makers', null=True, on_delete=models.PROTECT)  # производитель
    opisanie = models.TextField(null=True, verbose_name='Описание товара')
    count_goods = models.IntegerField(default=0, verbose_name='Количество товара')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    categor_goods = models.ForeignKey('Categories', null=True, on_delete=models.PROTECT)
    property_name = models.ManyToManyField('PropertyGoods', blank=True, verbose_name='Свойства товара')
    image1 = models.ImageField(upload_to=get_path_save1, verbose_name='Фото товара 1')
    image2 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 2')
    image3 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 3')
    image4 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 4')
    image5 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 5')
    image6 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 6')
    image7 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 7')
    image8 = models.ImageField(upload_to=get_path_save1, blank=True, verbose_name='Фото товара 8')

    def __str__(self):
        return '{0}_{1}'.format(self.goods_name, self.brend)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['goods_name']


# Модель(таблица) Свойства товара
class PropertyGoods(models.Model):
    nameProperty = models.CharField(max_length=150, verbose_name='Наименование свойства')   # Наименование свойства товара
    unitProperty = models.CharField(max_length=150, verbose_name='Еденица измерения')       # Еденица измерения свойства или название материала
    quantyProperty = models.IntegerField(default=0, verbose_name='Количество')              # Количественная часть
    boolProperty = models.BooleanField(default=False, verbose_name='Свойство Да/Нет')       # Указать назначение свойства да или нет
    boolValueProperty = models.BooleanField(default=False, verbose_name='Значение Да/Нет')       # Значение булевого свойства

    def __str__(self):
        return '{0} {1} {2}'.format(self.nameProperty, self.quantyProperty, self.unitProperty)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства товаров и их значения'
        ordering = ['nameProperty']


# Модель(таблица) Производители
class Makers(models.Model):
    nameMaker = models.CharField(max_length=150, verbose_name='Наименование производителя')
    countryMaker = models.CharField(max_length=150, verbose_name='Страна производителя')

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'Производители'
        ordering = ['nameMaker']

    def __str__(self):
        return self.nameMaker


class Categories(models.Model):
    categor_name = models.CharField(max_length=150, verbose_name='Наименование категории')

    def __str__(self):
        return self.categor_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['categor_name']




