from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello class! This is the project by Shilin, Joyce and Richard.")

from os.path import join
from django.conf import settings
import sqlite3, pandas as pd
from matplotlib import pyplot as plt

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from .forms import InputForm, IndicatorForm
from .models import COUNTRIES_DICT, VARIABLES_DICT

def location(request, country = None):
    country = request.GET.get('country', '')
    if not country: country = request.POST.get('country', 'china')

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data.csv')

    df = pd.read_csv(filename)
    df.set_index(["Country"], inplace = True)
    df.drop('Index', axis = 1, inplace = True)

    if country:
        df = df[df.index.str.lower() == country.lower()]

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:location'),
                'form_method' : 'get',
                'form' : InputForm({'country' : country}),
                'country' : COUNTRIES_DICT[country],
                'html_table': table,}
                # 'pic_source': reverse_lazy('dev:pic', kwargs = {'country': country})}

    return render(request, 'location.html', params)
    # return HttpResponse(table)

import matplotlib
matplotlib.style.use('ggplot')

def pic(request, country = None, variable = None):

    country = request.GET.getlist('country')
    if not country: country = [request.POST.get('country', 'albania')]
    variable = request.GET.get('variable', '')
    if not variable: variable = request.POST.get('variable', 'SE.SEC.ENRR.FE')

    indicator = VARIABLES_DICT[variable]

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data.csv')

    df = pd.read_csv(filename)

    if country and variable:
        df = df[['Country', 'Year', indicator]][df["Country"].str.lower().isin(country)]
        # df.set_index(['Country'], inplace = True)

    plt.figure() # needed, to avoid adding curves in plot
    ax = df.groupby('Country').plot(x = 'Year', y = indicator, title = indicator)
    # ax.legend(labels = country)
    # plt.ylim((-10.5,10.5))

    # write bytes instead of file.
    from io import BytesIO
    figfile = BytesIO()

    # this is where the color is used.
    try: plt.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such country")

    figfile.seek(0) # rewind to beginning of file
    return HttpResponse(figfile.read(), content_type="image/png")



def form(request, country = None):
    country = request.GET.get('country', '')
    if not country: country = request.POST.get('country', 'china')

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data.csv')

    df = pd.read_csv(filename)
    df.set_index(["Year"], inplace = True)
    df.drop("Index", axis = 1, inplace = True)

    if country:
        df = df[df["Country"].str.lower() == country.lower()]

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:form'),
                'form_method' : 'get',
                'form' : InputForm({'country' : country}),
                'country' : COUNTRIES_DICT[country],
                'html_table': table,
                'pic_source': reverse_lazy('dev:pic', kwargs = {'country': country})}

    return render(request, 'form.html', params)

# def compare(request, )

def indicator(request, country = None, variable = None):

    country = request.GET.getlist('country')
    if not country: country = [request.POST.get('country', 'albania')]
    variable = request.GET.get('variable', 'SE.SEC.ENRR.FE')
    # if not variable: variable = request.POST.get('variable', 'SE.SEC.ENRR.FE')

    indicator = VARIABLES_DICT[variable]

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data.csv')

    df = pd.read_csv(filename)

    if country and variable:
        df = df[['Country', 'Year', indicator]][df["Country"].str.lower().isin(country)]
        df.set_index(['Country'], inplace = True)

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:indicator'),
                'form_method' : 'get',
                'form' : IndicatorForm({'country' : country,
                                        'variable': variable}),
                'country' : COUNTRIES_DICT.get(country[i] for i in range(len(country))),
                'variable' : VARIABLES_DICT[variable],
                'html_table': table,}
                # 'pic_source': reverse_lazy('dev:pic', kwargs = {'country': country, 'variable': variable})}

    return render(request, 'indicator.html', params)
