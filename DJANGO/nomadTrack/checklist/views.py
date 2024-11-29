from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Checklist
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from django.http import JsonResponse
from django.views import View


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


class AllCheckList(View):
    def get(self, request):
        checklists = Checklist.objects.values(
            'id', 'name', 'description', 'user_id'
        )  # Fetch the required fields as dictionaries
        return JsonResponse(list(checklists), safe=False)