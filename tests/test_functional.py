def test_root(testapp):
    res = testapp.get('/', status=200)
    assert b'Pyramid' in res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404

def test_dates(testapp):
    res = testapp.get('/node_dates/mrcaott1000311ott3643727', status=200)
    assert res.body == b'[{"age": 9.325001, "source_id": "ot_1592@tree1", "source_node": "node22956", "time_unit": "Myr"}]'


def test_dates_post(testapp):
    post_params = '{"node":"mrcaott1002674ott1038063"}'
    res = testapp.post('/node_dates', params=post_params, status=200)
    assert res.body == b'[{"age": 16.949003, "source_id": "ot_307@tree2", "source_node": "node13291", "time_unit": "Myr"}, {"age": 7.18052, "source_id": "ot_409@tree2", "source_node": "node78398", "time_unit": "Myr"}, {"age": 12.818414, "source_id": "ot_1177@tree1", "source_node": "node4207", "time_unit": "Myr"}, {"age": 12.800342, "source_id": "ot_1041@tree1", "source_node": "node4215", "time_unit": "Myr"}]'


def test_no__dates_post(testapp):
    #Note to self, do not currently differentiate between bad ID vs no date info
    post_params = '{"node":"asdf"}'
    res = testapp.post('/node_dates', params=post_params, status=200)
    assert res.body == b'[{"age": null, "source_id": null, "source_node": null, "time_unit": null}]'
