from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Avg
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction, Budget
from .forms import CategoryForm, TransactionForm, BudgetForm

# BUDGET
@method_decorator(login_required, name='dispatch')
class BudgetListView(ListView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user).order_by('-start_date')


# @method_decorator(login_required, name='dispatch')
class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget created successfully!')
        return reverse_lazy('budget_section:budget_list')


@method_decorator(login_required, name='dispatch')
class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_list.html'
    extra_context = {'header': 'Update Budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget updated successfully!')
        return reverse_lazy('budget_section:budget_update')

@method_decorator(login_required, name='dispatch')
class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user).order_by('-id')

@method_decorator(login_required, name='dispatch')
class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Budget deleted successfully!')
        return reverse_lazy('budget_section:budget_list')

# CATEGORY
@method_decorator(login_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'budget_section/category_transaction_budget_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user).order_by('-id')

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Category'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Category created successfully!')
        return reverse_lazy('budget_section:category_list')


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Update Category'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Category created successfully!')
        return reverse_lazy('budget_section:category_list')

@method_decorator(login_required, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user).order_by('-date')

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Category deleted successfully!')
        return reverse_lazy('budget_section:category_list')


@method_decorator(login_required, name='dispatch')
class TransactionListView(ListView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_list.html'
    extra_context = {'list_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-date')


@method_decorator(login_required, name='dispatch')
class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Transaction'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Transaction created successfully!')
        return reverse_lazy('budget_section:transaction_list')


@method_decorator(login_required, name='dispatch')
class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Transaction'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Transaction created successfully!')
        return reverse_lazy('budget_section:transaction_list')


@method_decorator(login_required, name='dispatch')
class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Transaction'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-date')


@method_decorator(login_required, name='dispatch')
class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Transaction'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Transaction deleted successfully!')
        return reverse_lazy('budget_section:transaction_list')
