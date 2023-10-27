# coding: utf-8
from astropy.table import Table
from ctapipe.io import EventSource
from ctlearn_plugin import CTLearnReconstructor
from pickle import dump


source = EventSource("dataset://gamma_prod5.simtel.zst")
reco = CTLearnReconstructor(source.subarray)
t = Table({"obs_id": [1, 1, 1], "event_id": [1, 2, 3], "tel_id": [1, 1, 1]})
reco.predict_table(1, t)
with open("test.pkl", "wb") as f:
    dump(reco, f)
