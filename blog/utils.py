from time import time

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s)
    return f'{new_slug}-{str(int(time()))}'


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model
        return render(request, self.template, {'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        context = {
            self.model.__name__.lower(): obj,
            'form': bound_form
        }
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        context = {
            self.model.__name__.lower(): obj,
            'form': bound_form
        }

        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)
        return render(request, self.template, context)

class ObjectDeleteMixin:
    model = None
    template = None
    success_url = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.success_url))
