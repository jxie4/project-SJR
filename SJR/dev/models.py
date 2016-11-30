from django.db import models

# Create your models here.
COUNTRIES = (
    ('afghanistan', 'Afghanistan') ,
    ('albania', 'Albania') ,
    ('algeria', 'Algeria') ,
    ('angola', 'Angola') ,
    ('argentina', 'Argentina') ,
    ('armenia', 'Armenia') ,
    ('australia', 'Australia') ,
    ('austria', 'Austria') ,
    ('azerbaijan', 'Azerbaijan') ,
    ('bahrain', 'Bahrain') ,
    ('bangladesh', 'Bangladesh') ,
    ('belarus', 'Belarus') ,
    ('belgium', 'Belgium') ,
    ('benin', 'Benin') ,
    ('bhutan', 'Bhutan') ,
    ('bolivia', 'Bolivia') ,
    ('bosnia', 'Bosnia') ,
    ('botswana', 'Botswana') ,
    ('brazil', 'Brazil') ,
    ('bulgaria', 'Bulgaria') ,
    ('burkina faso', 'Burkina Faso') ,
    ('burundi', 'Burundi') ,
    ('cambodia', 'Cambodia') ,
    ('cameroon', 'Cameroon') ,
    ('canada', 'Canada') ,
    ('cape verde', 'Cape Verde') ,
    ('central african republic', 'Central African Republic') ,
    ('chad', 'Chad') ,
    ('chile', 'Chile') ,
    ('china', 'China') ,
    ('colombia', 'Colombia') ,
    ('comoros', 'Comoros') ,
    ('congo brazzaville', 'Congo Brazzaville') ,
    ('congo kinshasa', 'Congo Kinshasa') ,
    ('costa rica', 'Costa Rica') ,
    ('croatia', 'Croatia') ,
    ('cuba', 'Cuba') ,
    ('cyprus', 'Cyprus') ,
    ('czech republic', 'Czech Republic') ,
    ('denmark', 'Denmark') ,
    ('djibouti', 'Djibouti') ,
    ('dominican republic', 'Dominican Republic') ,
    ('east timor', 'East Timor') ,
    ('ecuador', 'Ecuador') ,
    ('egypt', 'Egypt') ,
    ('el salvador', 'El Salvador') ,
    ('equatorial guinea', 'Equatorial Guinea') ,
    ('eritrea', 'Eritrea') ,
    ('estonia', 'Estonia') ,
    ('ethiopia', 'Ethiopia') ,
    ('fiji', 'Fiji') ,
    ('finland', 'Finland') ,
    ('france', 'France') ,
    ('gabon', 'Gabon') ,
    ('gambia', 'Gambia') ,
    ('georgia', 'Georgia') ,
    ('germany', 'Germany') ,
    ('ghana', 'Ghana') ,
    ('greece', 'Greece') ,
    ('guatemala', 'Guatemala') ,
    ('guinea', 'Guinea') ,
    ('guinea-bissau', 'Guinea-Bissau') ,
    ('guyana', 'Guyana') ,
    ('haiti', 'Haiti') ,
    ('honduras', 'Honduras') ,
    ('hungary', 'Hungary') ,
    ('india', 'India') ,
    ('indonesia', 'Indonesia') ,
    ('iran', 'Iran') ,
    ('iraq', 'Iraq') ,
    ('ireland', 'Ireland') ,
    ('israel', 'Israel') ,
    ('italy', 'Italy') ,
    ('ivory coast', 'Ivory Coast') ,
    ('jamaica', 'Jamaica') ,
    ('japan', 'Japan') ,
    ('jordan', 'Jordan') ,
    ('kazakhstan', 'Kazakhstan') ,
    ('kenya', 'Kenya') ,
    ('korea north', 'Korea North') ,
    ('korea south', 'Korea South') ,
    ('kosovo', 'Kosovo') ,
    ('kuwait', 'Kuwait') ,
    ('kyrgyzstan', 'Kyrgyzstan') ,
    ('laos', 'Laos') ,
    ('latvia', 'Latvia') ,
    ('lebanon', 'Lebanon') ,
    ('lesotho', 'Lesotho') ,
    ('liberia', 'Liberia') ,
    ('libya', 'Libya') ,
    ('lithuania', 'Lithuania') ,
    ('luxembourg', 'Luxembourg') ,
    ('macedonia', 'Macedonia') ,
    ('madagascar', 'Madagascar') ,
    ('malawi', 'Malawi') ,
    ('malaysia', 'Malaysia') ,
    ('mali', 'Mali') ,
    ('mauritania', 'Mauritania') ,
    ('mauritius', 'Mauritius') ,
    ('mexico', 'Mexico') ,
    ('moldova', 'Moldova') ,
    ('mongolia', 'Mongolia') ,
    ('montenegro', 'Montenegro') ,
    ('morocco', 'Morocco') ,
    ('mozambique', 'Mozambique') ,
    ('myanmar (burma)', 'Myanmar (Burma)') ,
    ('namibia', 'Namibia') ,
    ('nepal', 'Nepal') ,
    ('netherlands', 'Netherlands') ,
    ('new zealand', 'New Zealand') ,
    ('nicaragua', 'Nicaragua') ,
    ('niger', 'Niger') ,
    ('nigeria', 'Nigeria') ,
    ('norway', 'Norway') ,
    ('oman', 'Oman') ,
    ('pakistan', 'Pakistan') ,
    ('panama', 'Panama') ,
    ('papua new guinea', 'Papua New Guinea') ,
    ('paraguay', 'Paraguay') ,
    ('peru', 'Peru') ,
    ('philippines', 'Philippines') ,
    ('poland', 'Poland') ,
    ('portugal', 'Portugal') ,
    ('qatar', 'Qatar') ,
    ('romania', 'Romania') ,
    ('russia', 'Russia') ,
    ('rwanda', 'Rwanda') ,
    ('saudi arabia', 'Saudi Arabia') ,
    ('senegal', 'Senegal') ,
    ('serbia', 'Serbia') ,
    ('sierra leone', 'Sierra Leone') ,
    ('singapore', 'Singapore') ,
    ('slovak republic', 'Slovak Republic') ,
    ('slovenia', 'Slovenia') ,
    ('solomon islands', 'Solomon Islands') ,
    ('somalia', 'Somalia') ,
    ('south africa', 'South Africa') ,
    ('south sudan', 'South Sudan') ,
    ('spain', 'Spain') ,
    ('sri lanka', 'Sri Lanka') ,
    ('sudan', 'Sudan') ,
    ('sudan-north', 'Sudan-North') ,
    ('suriname', 'Suriname') ,
    ('swaziland', 'Swaziland') ,
    ('sweden', 'Sweden') ,
    ('switzerland', 'Switzerland') ,
    ('syria', 'Syria') ,
    ('tajikistan', 'Tajikistan') ,
    ('tanzania', 'Tanzania') ,
    ('thailand', 'Thailand') ,
    ('togo', 'Togo') ,
    ('trinidad and tobago', 'Trinidad and Tobago') ,
    ('tunisia', 'Tunisia') ,
    ('turkey', 'Turkey') ,
    ('turkmenistan', 'Turkmenistan') ,
    ('uae', 'UAE') ,
    ('uganda', 'Uganda') ,
    ('ukraine', 'Ukraine') ,
    ('united kingdom', 'United Kingdom') ,
    ('united states', 'United States') ,
    ('uruguay', 'Uruguay') ,
    ('uzbekistan', 'Uzbekistan') ,
    ('venezuela', 'Venezuela') ,
    ('vietnam', 'Vietnam') ,
    ('yemen', 'Yemen') ,
    ('zambia', 'Zambia') ,
    ('zimbabwe', 'Zimbabwe') ,
)

COUNTRIES_DICT = dict(COUNTRIES)

class Input(models.Model):

    country = models.CharField(max_length=50, choices=COUNTRIES)

VARIABLES = (
    ('POLITY', 'Polity Score'),
    ('SE.SEC.ENRR.FE', 'School enrollment, secondary, female % (gross)') ,
    ('SE.SEC.ENRR.MA', 'School enrollment, secondary, male % (gross)') ,
    ('SL.AGR.EMPL.ZS', 'Employment in agriculture (% of total employment)') ,
    ('SL.SRV.EMPL.ZS', 'Employment in services (% of total employment)') ,
    ('SL.TLF.ACTI.1524.ZS', 'Labor force participation rate for ages 15-24, total (%) (modeled ILO estimate)') ,
    ('SL.UEM.1524.ZS', 'Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)') ,
    ('SH.DYN.MORT', 'Mortality rate, under-5 (per 1,000 live births)') ,
    ('SP.DYN.AMRT.FE', 'Mortality rate, adult, female (per 1,000 female adults)') ,
    ('SP.DYN.AMRT.MA', 'Mortality rate, adult, male (per 1,000 male adults)') ,
    ('SP.DYN.LE00.IN', 'Life expectancy at birth, total (years)') ,
    ('SP.DYN.TFRT.IN', 'Fertility rate, total (births per woman)') ,

)

VARIABLES_DICT = dict(VARIABLES)

SOCIAL_INDICATORS = (
    ('SE.SEC.ENRR.FE', 'School enrollment, secondary, female % (gross)') ,
    ('SE.SEC.ENRR.MA', 'School enrollment, secondary, male % (gross)') ,
    ('SL.AGR.EMPL.ZS', 'Employment in agriculture (% of total employment)') ,
    ('SL.SRV.EMPL.ZS', 'Employment in services (% of total employment)') ,
    ('SL.TLF.ACTI.1524.ZS', 'Labor force participation rate for ages 15-24, total (%) (modeled ILO estimate)') ,
    ('SL.UEM.1524.ZS', 'Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)') ,
    ('SH.DYN.MORT', 'Mortality rate, under-5 (per 1,000 live births)') ,
    ('SP.DYN.AMRT.FE', 'Mortality rate, adult, female (per 1,000 female adults)') ,
    ('SP.DYN.AMRT.MA', 'Mortality rate, adult, male (per 1,000 male adults)') ,
    ('SP.DYN.LE00.IN', 'Life expectancy at birth, total (years)') ,
    ('SP.DYN.TFRT.IN', 'Fertility rate, total (births per woman)') ,

)

SOCIAL_INDICATORS_DICT = dict(SOCIAL_INDICATORS)

class Indicator(models.Model):

    variable = models.CharField(max_length = 200, choices = VARIABLES)
    country = models.CharField(max_length=30, choices=COUNTRIES)

class Correlate(models.Model):

    variable = models.CharField(max_length = 200, choices = SOCIAL_INDICATORS)
