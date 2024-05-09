from django.contrib import admin

from expenses.models import ExpenseCategory

# menasheh 12345678
# Register your models here.


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'amount', 'date']
    search_fields = ['id', 'title', 'amount', 'date']
    list_filter = ['title', 'amount', 'date']
    date_hierarchy = 'date'
