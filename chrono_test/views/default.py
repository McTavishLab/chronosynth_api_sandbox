from pyramid.view import view_config
from pyramid.response import Response
import json

def get_date(node):
    dates = json.load(open("/home/ejmctavish/projects/otapi/chronosynth/node_ages1.json"))
    if node in dates['node_ages']:
        return dates['node_ages'][node]
    else:
        return {
            "age": None,
            "source_id": None,
            "source_node": None,
            "time_unit": None
          },

@view_config(route_name='home', renderer='chrono_test:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'chrono_test', 'authors':'EJM + LLSR'}


@view_config(route_name='puppies')
def pup_view(request):
    return Response("Custard, Iris, Bailey\n")

@view_config(route_name='puppy_check')
def pup_check_view(request):
    puppies = ["Custard","Iris","Bailey"]
    guess = request.matchdict['dogname']
    if guess in puppies:
        answ = "YESSS!"
    else:
        answ = "Nope"
    return Response(answ)

@view_config(route_name='show_me')
def show_view(request):
    retstr = str(request.matchdict)
    return Response(retstr)

@view_config(route_name='trypost', renderer='json')
def trypost_view(request):
    try:
        payload = request.json_body
        print('payload is {p}'.format(p=payload))
    except:
        print("no payload")
        payload = {'dogname':'puppy'}
    retstr = "This doggie is named {}".format(payload['dogname'])
    return retstr

@view_config(route_name='node_dates', renderer='json')
def node_dates_view(request):
    payload = request.json_body
    node_id = payload['node']
    ret = get_date(node_id)
    return ret

@view_config(route_name='node_dates_get', renderer='json')
def node_dates_get_view(request):
    node_id = request.matchdict['node']
    ret = get_date(node_id)
    return ret

