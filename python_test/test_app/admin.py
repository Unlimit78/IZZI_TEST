from django.contrib import admin
from django.http import HttpResponseRedirect

from django.urls import path

from .models import User,Order
from .forms import CsvUploadForm
from .parser import csv_parser

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_list_template = 'csv_upload.html'
    list_display = ['username','first_name','last_name','date_of_birth','date_of_registration','order']
    fields = ['username','first_name','last_name','date_of_birth','date_of_registration','order']

    def get_urls(self):
        urls = super().get_urls()
        add_urls = [
            path("csv_upload/", self.csv_upload),
        ]
        return add_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra = extra_context or {}
        extra["form"] = CsvUploadForm()
        return super(UserAdmin, self).changelist_view(request, extra_context=extra)

    def csv_upload(self, request):
        if request.method=='POST':
            form = CsvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES.get('file')
                data = csv_parser(file)
                for i in data:
                    i[2] = '-'.join(i[2].split('/'))
                    i[3] = '-'.join(i[3].split('/'))
                    user = User.objects.create(first_name=i[0],
                                        last_name=i[1],
                                        date_of_birth=i[2],
                                        date_of_registration=i[3],
                                               username=i[0]+i[1])


        else:
            form = CsvUploadForm()

        return HttpResponseRedirect('../')


admin.site.register(Order)

