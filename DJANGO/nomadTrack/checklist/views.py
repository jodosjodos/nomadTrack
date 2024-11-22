from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Checklist
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView


@login_required
def checklists_index(request):
    checklists_list = Checklist.objects.filter(user=request.user)
    return render(
        request, "checklist/checklist_list.html", {"checklists_list": checklists_list}
    )


class ChecklistDetail(LoginRequiredMixin, DetailView):
    model = Checklist


class ChecklistCreate(LoginRequiredMixin, CreateView):
    model = Checklist
    fields = ["name", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChecklistUpdate(LoginRequiredMixin, UpdateView):
    model = Checklist
    fields = ["name", "description"]


class ChecklistDelete(LoginRequiredMixin, DeleteView):
    model = Checklist
    success_url = "/checklist/checklists"