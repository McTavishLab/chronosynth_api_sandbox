def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('puppies', '/pup')
    config.add_route('puppy_check', '/pup/{dogname}')
    config.add_route('show_me', '/show/{val1}/{val2}')
    config.add_route('trypost', '/posted')
    config.add_route('node_dates', '/node_dates')
    config.add_route('node_dates_get', '/node_dates/{node}')