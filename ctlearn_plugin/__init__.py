from astropy.table import Table
from ctapipe.reco import Reconstructor, ReconstructionProperty
import numpy as np
from ctapipe.reco.stereo_combination import StereoMeanCombiner
from ctapipe.core.traits import Unicode
import astropy.units as u

rng = np.random.default_rng(0)


class CTLearnReconstructor(Reconstructor):

    prefix = Unicode("ctlearn").tag(config=True)


    def __init__(self, subarray, **kwargs):
        super().__init__(subarray=subarray, **kwargs)
        self.stereo_combiner = StereoMeanCombiner(prefix=self.prefix)

    def __call__(self, event):
        pass

    def predict_table(self, tel, table):

        n_events = len(table)
        energy = 10**rng.uniform(2, 6, n_events)
        valid = np.ones(n_events, dtype=bool)
        result = Table({
            f"{self.prefix}_tel_energy": energy * u.TeV,
            f"{self.prefix}_tel_is_valid": valid,
        })

        return {
            ReconstructionProperty.ENERGY: result,
        }
