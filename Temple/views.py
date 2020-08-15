from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Temple
from .forms import TempleForm


class TempleCreateView(CreateView):
    template_name = "temples/temple_create.html"
    form_class = TempleForm
    queryset = Temple.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class TempleUpdateView(UpdateView):
    template_name = "temples/temple_create.html"
    form_class = TempleForm
    queryset = Temple.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Temple, id=id_)


class TempleListView(ListView):
    template_name = "temples/temple_list.html"
    queryset = Temple.objects.all()
    # queryset = ShopName.objects.all()

    # def get_queryset(self):
    #     qs = super(TempleListView, self).get_queryset()
    #     user_id = InventoryUser.objects.filter(
    #         username=self.request.user).values_list('id', flat=True)
    #     return ShopName.objects.filter(created_by__in=user_id)

    # queryset = get_queryset


class TempleDetailView(DetailView):
    template_name = "temples/temple_detail.html"
    queryset = Temple.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Temple, id=id_)


class TempleDeleteView(DeleteView):
    template_name = "temples/temple_delete.html"
    queryset = Temple.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Temple, id=id_)

    def get_success_url(self):
        return reverse('temples:Temple-List')
