import csv
from io import StringIO
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from django.contrib import admin
from django.http import HttpResponse

from .models import *


class ListInvoice(admin.ModelAdmin):
    actions = ["download_csv", "export_xls"]
    list_filter = (
        ('start_date', DateRangeFilter), ('end_date', DateRangeFilter),
    )
    list_display = ["payment_address", "start_date", "end_date", "payment_status", "payment_mode", "tax_amount"]
    search_fields = ["payment_address", "start_date", "end_date", "payment_status", "payment_mode", "tax_amount"]

    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["payment_address", "start_date", "end_date", "payment_status", "payment_mode", "tax_amount"])
        for s in queryset:
            writer.writerow(
                [s.payment_address, s.start_date, s.end_date, s.payment_status, s.payment_mode, s.tax_amount])
        f.seek(0)
        response = HttpResponse(f, content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=invoice.csv"
        return response

    def export_xls(modeladmin, request, queryset):
        import xlwt
        wb = xlwt.Workbook()
        ws = wb.add_sheet("InvoiceList")
        columns = [
            ("payment_address", 15000), ("start_date",16000), ("end_date",17000),
            ("payment_status",18000), ("payment_mode",19000), ("tax_amount",20000)
        ]
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            ws.col(col_num).width = columns[col_num][1]
        for obj in queryset:
            row_num += 1
            row = [
                obj.payment_address, obj.start_date, obj.end_date,
                obj.payment_status, obj.payment_mode, obj.tax_amount]
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=invoice.xls'
        wb.save(response)
        return response   

    download_csv.short_description = "Export CSV"
    export_xls.short_description = "Export XLS"


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Invoice, ListInvoice)
