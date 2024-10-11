from django.http import JsonResponse, HttpResponse

class AjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():

            errors = []
            for field in form:
                for error in field.errors:
                    errors.append(error)
            return JsonResponse({'errors':errors}, status=400)
        else:
            return response

    def form_valid(self, form, json_data=None):

        response = super().form_valid(form)
        if self.request.is_ajax():

            return JsonResponse(json_data)
        else:
            return response