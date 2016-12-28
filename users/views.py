from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import User


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = ['last_name', 'first_name', 'phone']
    success_url = reverse_lazy('users:list')
    template_name_suffix = '_create'


class UserUpdateView(UpdateView):
    model = User
    fields = ['last_name', 'first_name', 'phone']
    success_url = reverse_lazy('users:list')
    template_name_suffix = '_update'

    def get_object(self, queryset=None):
        ret = super(UpdateView, self).get_object(queryset)
        print(ret)
        return ret


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
