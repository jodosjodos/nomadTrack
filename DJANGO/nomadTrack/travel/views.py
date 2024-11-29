from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Travel
from checklist.models import Checklist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import CheckingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.db.models import Count
from .models import Checking
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views import View

# Create your views here.


class TravelCreate(LoginRequiredMixin, CreateView):
    model = Travel
    fields = ["name", "country", "city", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TravelUpdate(LoginRequiredMixin, UpdateView):
    model = Travel
    fields = ["name", "country", "city", "description", "image"]


class TravelDelete(LoginRequiredMixin, DeleteView):
    model = Travel
    success_url = "/travel/"


# def home(request):
#     os.getenv("NAME")
#     return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def travels_index(request):
    travels = Travel.objects.filter(user=request.user)
    return render(request, "travel/index.html", {"travels": travels})


@login_required
def travels_detail(request, travel_id):
    checking_form = CheckingForm
    travel = Travel.objects.get(id=travel_id)
    checklists_travel_for_planning = Checklist.objects.filter(
        user=request.user
    ).exclude(id__in=travel.checklists.all().values_list("id"))
    return render(
        request,
        "travel/details.html",
        {
            "travel": travel,
            "title": "Travels Details Page",
            "checking_form": checking_form,
            "checklists": checklists_travel_for_planning,
        },
    )


@login_required
def add_checking(request, travel_id):
    form = CheckingForm(request.POST)

    if form.is_valid():
        new_checking = form.save(commit=False)
        new_checking.travel_id = travel_id
        new_checking.save()
        return redirect("detail", travel_id=travel_id)


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
    success_url = "/checklists/"


@login_required
def checklists_index(request):
    checklists_list = Checklist.objects.filter(user=request.user)
    return render(
        request, "main_app/checklist_list.html", {"checklists_list": checklists_list}
    )


@login_required
def assoc_checklist(request, travel_id, checklist_id):
    Travel.objects.filter(user=request.user)
    Travel.objects.get(id=travel_id).checklists.add(checklist_id)
    return redirect("detail", travel_id=travel_id)


@login_required
def unassoc_checklist(request, travel_id, checklist_id):
    Travel.objects.filter(user=request.user)
    Travel.objects.get(id=travel_id).checklists.remove(checklist_id)
    return redirect("detail", travel_id=travel_id)


def dashboard(request):
    # Fetch travel-related data
    travel_data = (
        Travel.objects.annotate(total_checkings=Count("checking"))
        .values("name", "country", "city", "total_checkings")
        .order_by("-total_checkings")
    )

    # Total counts
    total_travels = Travel.objects.count()
    total_checklists = Checklist.objects.count()
    checked_checklists = Checklist.objects.filter(name="checked").count()
    unchecked_checklists = total_checklists - checked_checklists

    # Checklist distribution for pie chart
    checklist_pie_data = {
        "Checked": checked_checklists,
        "Unchecked": unchecked_checklists,
    }

    # Most visited travels (top by checkings)
    top_travels = travel_data[:5]

    # Recent travel checkings
    recent_checkings = Checking.objects.order_by("-date")[:5]

    # Prepare context data
    context = {
        "total_travels": total_travels,
        "total_checklists": total_checklists,
        "checklist_pie_data": checklist_pie_data,
        "top_travels": top_travels,
        "recent_checkings": recent_checkings,
    }

    return render(request, "home.html", context)


class TravelList(View):
    def get(self, request):
        travels = Travel.objects.values(
            'id', 'name', 'country', 'city', 'description', 'user_id'
        )  # Fetch only the required fields as dictionaries
        return JsonResponse(list(travels), safe=False)