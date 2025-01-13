# URLS for Otodom.pl
# https://www.otodom.pl/pl/wyniki/sprzedaz/kawalerka/mazowieckie/warszawa/warszawa/warszawa/?ownerTypeSingleSelect=ALL&distanceRadius=5&priceMin=2&priceMax=68&areaMin=1&areaMax=36&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/haleimagazyny/cala-polska?ownerTypeSingleSelect=ALL&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/haleimagazyny,rynek-pierwotny/cala-polska?limit=36&ownerTypeSingleSelect=AGENCY&pricePerMeterMin=5&pricePerMeterMax=6&daysSinceCreated=1&heightMin=3&heightMax=4&advertId=12&description=123&heating=%5BYES%5D&extras=%5BIS_PRIVATE_OWNER%5D&useTypes=%5BSTOCK%5D&by=DEFAULT&direction=DESC&viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/podlaskie/bialystok/bialystok/bialystok/bacieczki?viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa/bielany?viewType=listing
# https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie,rynek-wtorny/mazowieckie/warszawa/warszawa/warszawa/bielany?limit=36&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing
# URL Structure:
# https://www.otodom.pl
# /pl/wyniki/sprzedaz
# /[kawalerka,haleimagazyny],[rynek-pierwotny]
# /[mazowieckie/warszawa/warszawa/warszawa/bielany, podlaskie/bialystok/bialystok/bialystok/bacieczki, cala-polska]
# ?ownerTypeSingleSelect=[ALL,AGENCY]
# &distanceRadius=5
# &priceMin=2
# &priceMax=68
# &areaMin=1
# &areaMax=36
# &viewType=listing
# &limit=36
# &pricePerMeterMin=5
# &pricePerMeterMax=6
# &daysSinceCreated=1
# &heightMin=3
# &heightMax=4
# &advertId=12
# &description=123
# &heating=[YES]
# &extras=[IS_PRIVATE_OWNER]
# &useTypes=[STOCK]
# &by=DEFAULT
# &direction=DESC
# &viewType=listing

searchUrl = 'https://www.otodom.pl/pl/wyniki/sprzedaz'
searchParameters = []
marketLocation = ''
realEstateMarketType = ''
propertyMarketType = ''

def parseArguments(args):
    __setPricePerRealEstate__(args.price_min,args.price_max)
    __setArea__(args.min_area,args.max_area)
    __setPlace__(args.place,0)
    __setAge__(args.time_filter)
    __setMarketType__(args.marketType)

def get_url_with_search_params():
    generate_url = searchUrl
    generate_url += __parseMarket__()
    generate_url += __parseLocation__()
    generate_url += __parseSearchParameters__()
    return generate_url

def __parseMarket__():
    return f'/${realEstateMarketType},${propertyMarketType}'

def __parseLocation__():
    return f'/${marketLocation}'

def __parseSearchParameters__():
    searchParametersString = ''
    for parameter in searchParameters:
        searchParametersString += f'&${parameter}'
    searchParametersString[0] = '?'
    return searchParametersString

def __setRealestateType__(realEstateTypeArgument):
    realEstateType = realEstateTypeArgument
    
def __setMarketType__(marketTypeArgument):
    if marketTypeArgument == 'primary':
        marketType = 'rynek-pierwotny'
    elif marketTypeArgument == 'secondary':
        marketType = 'rynek-wtorny'

def __setPricePerRealEstate__(min, max):
    addSearchParameters(formatMinMaxParameters(min,max,'price'))

def __setPricePreMeter__(min,max):
    addSearchParameters(formatMinMaxParameters(min,max,'pricePerMeter'))

def __setArea__(min,max):
    addSearchParameters(formatMinMaxParameters(min,max,'area'))

def __setPlace__(place, distanceRadius):
    addSearchParameters(f'distanceRadius=${distanceRadius}')
    if(place == 'ALL'):
        location = 'cala-polska'
    elif(place == 'Warszawa'):
        location = 'mazowieckie/warszawa/warszawa/warszawa/'
    elif(place == 'Bialystok'):
        location = 'podlaskie/bialystok/bialystok/bialystok/'
    
def __setAge__(age):
    if age == 'any':
        None
    elif age == 'last24h':
        addSearchParameters(f'daysSinceCreated=1')
    elif age == 'last3d':
        addSearchParameters(f'daysSinceCreated=3')
    elif age == 'last7d':
        addSearchParameters(f'daysSinceCreated=7')

def __formatMinMaxParameters__(min, max, name):
    return f'${name}Min=${min}',f'${name}Max=${max}'

def __addSearchParameters__(parameters):
    searchParameters.append(parameters)