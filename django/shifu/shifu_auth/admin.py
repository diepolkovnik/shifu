from django.contrib import admin
# Register your models here.


def get_queryset(self, request):
        queryset = super(User.email, self).get_queryset(request)
        queryset = queryset.order_by('email', 'user')
        return queryset