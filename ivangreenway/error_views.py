from django.shortcuts import render
from django.views.generic import TemplateView


class Error404(TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=404)

class Error403(TemplateView):
    template_name = '403.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=403)

