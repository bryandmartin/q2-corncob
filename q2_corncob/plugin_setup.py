# ----------------------------------------------------------------------------
# Copyright (c) 2017-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import importlib


import qiime2.plugin
from q2_types.sample_data import SampleData
from q2_types.feature_table import FeatureTable, Frequency

import q2_corncob

citations = qiime2.plugin.Citations.load('citations.bib', package='q2_corncob')

plugin = qiime2.plugin.Plugin(
    name='corncob',
    version='0.1.0',
    website='http://bryandmartin.github.io/corncob/',
    package='q2_corncob',
    description=('This QIIME 2 plugin wraps corncob and supports '
                 'single-taxon regression using the corncob R library.'),
    short_description='Plugin for single-taxon regression with corncob.',
    citations=[citations['martin2018']]
)

# has to match _seq_depth.py
# parameters arent artifacts
plugin.visualizers.register_function(
    function=q2_corncob.seq_depth,
    inputs={'table': FeatureTable[Frequency]
    },
    parameters={'metadata': qiime2.plugin.Metadata,
                'mypar': qiime2.plugin.Float},
    input_descriptions={
        'table': ('A feature table.')
    },
    parameter_descriptions={
         'mypar': ('A parameter description.'),
         'metadata': ('Metadata')
    },
    name='Get sequencing depth',
    description=('This method gets sequencing depth.')
)

