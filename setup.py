# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(
    name="q2-corncob",
    version="0.1.0",
    url="gith",
    license="BSD-3-Clause",
    packages=find_packages(),
    author="Bryan D Martin",
    author_email="bmartin6@uw.edu",
    description="Apply corncob for dysbiosis. ",
    scripts=['q2_corncob/assets/seq_depth.R'],
    package_data={
        'q2_corncob': ['citations.bib'],
        'q2_corncob.assets': ['seq_depth.R']
      # BRYAN TODO: WHAT
#        'q2_corncob.tests': ['data/*',
#                           'data/expected/*',
#                           'data/underscore_samples/*',
#                           'data/sample_seqs_single/*',
#                           'data/sample_seqs_paired/*']
    },
    ## where qiime learns about existance of a plugin
    entry_points={
        "qiime2.plugins":
        ["q2-corncob=q2_corncob.plugin_setup:plugin"]
    },
    zip_safe=False,
)
