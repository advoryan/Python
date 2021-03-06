from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import *
from books.views import *
from books.models import *
from .forms import *

from django.db.models import Q
from django.urls import reverse_lazy

# class Searching(ListView):
    #     def get_queryset(self):
    #         qs = super().get_queryset()
    #         search = self.request.GET.get("search", 0)
    #         if search != 0:
    #             return qs.filter(pk__gte=search)
    #         return qs
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         f = SearchForm()
    #         context["form"] = f       
    #         # context["form"] = f
    #         return context

class SeriesDetail(DetailView):
    model = Series
    # template_name = - изменить тип шаблона
    abc = 2 * 2
    # переопределение методов родителя get_context_data
    def get_context_data(self, **kwargs): # переопределяем функцию папашки
        context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
        print(self, kwargs) # - 
        # context["ffff"] = self.abc
        return context

class SeriesView(ListView):
    model = Series

    def get_queryset(self):
        qs = super().get_queryset()
        # active = self.request.GET.get("on", False)
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(name__icontains=search)
        return qs
    # if active:
        #     qs = qs.filter(is_active=True) #- если есть поле активный
        # #     if search != 0:
        # #         return qs.filter(Q(name__icontains=search) | Q(description__icontains=search)) # - это аналог "И" ( | - или, & - и, ~ - NOT + работаюь скобки)
        # #     return qs
        # # if search:
        # return qs.filter(Q(name__icontains=search) | Q(description__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

# РАБОЧЕЕ - СОХРАНЕНО --------------------------------
    # class SeriesView(ListView):
    #     model = Series
    #     def get_queryset(self):
    #         qs = super().get_queryset()
    #         search = self.request.GET.get("search", 0)
    #         if search != 0:
    #             return qs.filter(name__icontains=search)
    #         return qs
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         f = SearchForm()
    #         context["form"] = f       
    #         return context
    # -----------------------------------------------------

class SeriesCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = SeriesCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("series-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("series-list-view")
        return reverse_lazy("series-create-view")

class SeriesUpdateView(UpdateView):
    model = Series
    # template_name = 'data/Creation_form.html'
    form_class = SeriesCreateForm

class SeriesDeleteView(DeleteView):
    success_url = reverse_lazy("series-detail-view")
    model = Series
    # template_name = 'data/Creation_form.html'
    # form_class = SeriesCreateForm
    template_name = "data/Delete_form.html"


# template_name = "data/series_list.html"
        # def get_queryset(self):
        #     queryset = ["fgsdg", "sdfgsdfg", "gfdgs"]
        
        #    model = Series
        # def get_queryset(self):
        #     return ["2"]

        # def get_queryset(self):
        #     a = self.model
        #     return a.objects.filter(pk__gt=25)

        # def get_queryset(self):
        #     return Series.objects.filter(pk__gt=25)
    
    # class SeriesView(ListView):
    #     model = Series
    #     queryset = Series.objects.filter(pk__gt=20)   # работает
    
        # def get_context_data(self, **kwargs): # переопределяем функцию папашки
        #         context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
        #         print(context) # - 
        #         a = context["object_list"]# context["ffff"] = self.abc
        #         b = a.filter(pk__gt=50) # фильтр пк > 50
        #         context["object_list"] = b
        #         return context


        # def get_queryset(self):
        #     return Series.objects.filter(description__icontains='desk')[:5] # - it's work!!!
        # model = Series
        # # template_name = - изменить тип шаблона
        # abc = 2 * 2
        # # переопределение методов родителя get_context_data
        # def get_context_data(self, **kwargs): # переопределяем функцию папашки
        #     context = super().get_context_data(**kwargs) # проим отработать отцовский метод с помощью super
        #     print(self, kwargs) # - 
        #     # context["ffff"] = self.abc
        #     return context

# class BooksView(ListView):
#     model = Book
#     def get_queryset(self):
#         qs = super().get_queryset()
#         search = self.request.GET.get("search", 0)
#         if search != 0:
#             return qs.filter(name__icontains=search)
#         return qs
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         f = SearchForm()
#         context["form"] = f       
#         return context

# class BooksDetail(DetailView):
#     model = Book

class AuthorDetail(DetailView):
    model = Author

class AuthorView(ListView):
    model = Author
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0) # СЛОВАРЬ - self.request.GET
        if search != 0:
            return qs.filter(last_name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

# return qs.filter(first_name=form1)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     f = SearchForm()
    #     context["form"] = f
    #     return context

class AuthorCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = AuthorCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("author-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("author-list-view")
        return reverse_lazy("author-create-view")

class GenreDetail(DetailView):
    model = Genre

class GenreView(ListView):
    model = Genre
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f
        return context

class GenreCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = GenreCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("genre-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("genre-list-view")
        return reverse_lazy("genre-create-view")

class PublishDetail(DetailView):
    model = Publish

class PublishView(ListView):
    model = Publish
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(name__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class PublishCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = PublishCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("publish-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("publish-list-view")
        return reverse_lazy("publish-create-view")

class BindingDetail(DetailView):
    model = Binding

class BindingView(ListView):
    model = Binding
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(binding_type__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class BindingCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = BindingCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("binding-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("binding-list-view")
        return reverse_lazy("binding-create-view")
 
class BookFormatDetail(DetailView):
    model = BookFormat

class BookFormatView(ListView):
    model = BookFormat
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", 0)
        if search != 0:
            return qs.filter(size__icontains=search)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f       
        return context

class BookFormatCreateView(CreateView):
    model = Series
    template_name = 'data/Creation_form.html'
    form_class = BookFormatCreateForm
    def get_success_url(self):
        # new_url = super().get_success_url() - не обязательно надо, пользуемся родителем
        detail1 = self.request.POST.get("detail")
        list1 = self.request.POST.get("list")
        view1 = self.request.POST.get("view")
        if detail1:
            return reverse_lazy("bookformat-detail-view", kwargs={"pk": self.object.pk})
        elif list1:
            return reverse_lazy("bookformat-list-view")
        return reverse_lazy("bookformat-create-view")

class DictView(TemplateView):
    template_name = "data/Dict_List.html"

