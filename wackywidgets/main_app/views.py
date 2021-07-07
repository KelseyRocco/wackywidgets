from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm


# Define the home view
def index(request):
    return render(request, 'index.html')

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'

# def widgets_index(request, widget_id):
#     widget = Widget.objects.get(id=widget_id)
#     widget_form = WidgetForm()
#     return render(request, 'index.html', {
#         'widget': widget, 'widget_form' : widget_form
#     })


def widgets_index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets' : widgets})

def add_widget(request, widget_id):
    form=WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('', widget_id=widget_id)