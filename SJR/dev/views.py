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
from .forms import InputForm, IndicatorForm, CorrelateForm
from .models import COUNTRIES_DICT, VARIABLES_DICT, YEARS_DICT

def team(request):
    return render(request,'OurTeam.html')

def datasetSource(request):
    return render(request,'Dataset_Sources.html')

def question(request):
    return render(request,'question.html')

def location(request, country = None):

    country = request.GET.get('country', 'china')
    # if not country: country = request.POST.get('country', 'china')

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data_new.csv')

    df = pd.read_csv(filename)

    df.set_index(["Country"], inplace = True)
    df.drop('Index', axis = 1, inplace = True)

    if country:
        df = df[df.index.str.lower() == country.lower()]

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    # table = table.replace('border="1"','border="0"')
    # table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:location'),
                'form_method' : 'get',
                'form' : InputForm({'country' : country}),
                'country' : COUNTRIES_DICT[country],
                'html_table': table,}

    return render(request, 'location.html', params)

import matplotlib
matplotlib.style.use('ggplot')

def pic(request, country, variable):

    country_list = country.split(",")

    indicator = VARIABLES_DICT[variable]

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data_new.csv')

    df = pd.read_csv(filename)

    if country and variable:
        df = df[['Country', 'Year', indicator]][df["Country"].str.lower().isin(country_list)]
        # df.set_index(['Country'], inplace = True)

    plt.figure() # needed, to avoid adding curves in plot
    fig, ax = plt.subplots(figsize = (8,6))
    for label, df_group in df.groupby("Country"):
        df_group.plot(x = 'Year', y = indicator, title = indicator, ax = ax, label = label)
    plt.legend(loc = 0)
    # ax.legend(labels = country)
    plt.ylim((min(df[indicator])-1,max(df[indicator])+1))

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
    table = table.replace('style="text-align: left;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:form'),
                'form_method' : 'get',
                'form' : InputForm({'country' : country}),
                'country' : COUNTRIES_DICT[country],
                'html_table': table,
                'pic_source': reverse_lazy('dev:pic', kwargs = {'country': country})}

    return render(request, 'form.html', params)


def indicator(request, country = None, variable = None):

    country = request.GET.getlist('country')
    if not country: country = [request.POST.get('country', 'albania')]
    variable = request.GET.get('variable', 'SE.SEC.ENRR.FE')
    # if not variable: variable = request.POST.get('variable', 'SE.SEC.ENRR.FE')

    indicator = VARIABLES_DICT[variable]

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data_new.csv')

    df = pd.read_csv(filename)

    if country and variable:
        df = df[['Country', 'Year', indicator]][df["Country"].str.lower().isin(country)]
        df.set_index(['Country'], inplace = True)

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    # table = table.replace('border="1"','border="0"')
    # table = table.replace('style="text-align: left;"', "") # control this in css, not pandas.

    countries = ",".join(country)

    params = {'form_action' : reverse_lazy('dev:indicator'),
                'form_method' : 'get',
                'form' : IndicatorForm({'country' : country,
                                        'variable': variable}),
                'country' : COUNTRIES_DICT.get(country[i] for i in range(len(country))),
                'variable' : VARIABLES_DICT[variable],
                'html_table': table,
                'pic_source': reverse_lazy('dev:pic', kwargs = {'country' : countries, 'variable' : variable})}

    return render(request, 'indicator.html', params)

import seaborn as sns
sns.set(font_scale = 1.3)

def scatter(request, variable):

    indicator1 = 'Polity Score'
    indicator2 = VARIABLES_DICT.get(variable)

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data_new.csv')

    df = pd.read_csv(filename)

    if variable:
        df = df[['Country', 'Year', indicator1, indicator2]]
        # df.set_index(['Country'], inplace = True)

    plt.figure() # needed, to avoid adding curves in plot
    # fig, ax = plt.subplots(figsize = (8,6))
    # for label, df_group in df.groupby("Country"):
    #     df_group.plot(x = 'Year', y = indicator, title = indicator, ax = ax, label = label)
    # plt.legend(loc = 0)
    # ax.legend(labels = country)
    # df.boxplot(by = indicator1, column = indicator2)

    sns.regplot(data = df, x = indicator1, y = indicator2)
    # plt.ylim((min(df[indicator])-1,max(df[indicator])+1))

    # write bytes instead of file.
    from io import BytesIO
    figfile = BytesIO()

    # this is where the color is used.
    try: plt.savefig(figfile, format = 'png')
    except ValueError: raise Http404("No such country")

    figfile.seek(0) # rewind to beginning of file
    return HttpResponse(figfile.read(), content_type="image/png")

from scipy import stats
# import statsmodels.formula.api as sm
import numpy as np

def correlate(request, variable = None):

    variable = request.GET.get('variable', 'SE.SEC.ENRR.FE')
    if not variable: variable = request.POST.get('variable', 'SE.SEC.ENRR.FE')

    indicator1 = 'Polity Score'
    indicator2 = VARIABLES_DICT.get(variable)

    filename = join(settings.STATIC_ROOT, 'dev/project_merge_data_new.csv')

    df = pd.read_csv(filename)

    # if variable:
    #     df = df[['Country', 'Year', indicator1, indicator2]]
    #     df.set_index(['Country'], inplace = True)

    X = df[indicator1]
    Y = df[indicator2]
    mask = ~np.isnan(X) & ~np.isnan(Y)

    slope, intercept, r_value, p_value, std_err = stats.linregress(X[mask], Y[mask])
    r_squared = r_value ** 2
    # table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    # table = table.replace('border="1"','border="0"')
    # table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:compare'),
                'form_method' : 'get',
                'form' : CorrelateForm({'variable': variable}),
                'variable' : VARIABLES_DICT[variable],
                # 'slope': slope,
                # 'intercept' : intercept,
                # 'r_squared': r_squared,
                # 'p_value': p_value,
                # 'std_err': std_err,
                # 'html_table': table,
                'pic_source': reverse_lazy('dev:scatter', kwargs = {'variable' : variable})}

    return render(request, 'correlate.html', params)
