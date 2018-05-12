

import os
import tempfile
import hashlib
import subprocess
import pkg_resources

import biom
import skbio
import qiime2.util
import pandas as pd
import q2templates

TEMPLATES = pkg_resources.resource_filename('q2_corncob', 'assets')


# output directory as first thing
def seq_depth(output_dir: str,
              table: pd.DataFrame,
              metadata: qiime2.Metadata,
              mypar: float=4) -> None:
    
    table_path = os.path.join(output_dir, 'table.tsv')
    metadata_path = os.path.join(output_dir, 'metadata.tsv')
    
    table.to_csv(table_path)
    metadata.save(metadata_path)
    
    cmd_path = os.path.join(TEMPLATES, 'seq_depth.R')
    
    print(os.path.exists(table_path))
    print(os.path.exists(metadata_path))

    cmd = ['Rscript', cmd_path, '{0}'.format(output_dir), '{0}'.format(table_path),
           '{0}'.format(metadata_path)]
    #cmd = 'Rscript {0} arg1={1} arg2={2} arg3={3}'.format(cmd_path, output_dir, table_path, metadata_path)
    #cmd = 'Rscript assets/seq_depth.R arg1=$1 arg2=$2 arg3=$3'
    proc = subprocess.run(cmd, check=True)
    index = os.path.join(TEMPLATES, 'index.html')
    
    # Errors filepath, load in as list
    errors_fp = os.path.join(output_dir, 'warnings.txt')
    with open(errors_fp, 'r') as errors_f:
        errors = [e for e in errors_f]
    
    # Load in depths as a pandas data frame, then transfer to html
    depths = pd.read_csv(os.path.join(output_dir, 'mytable.tsv'), sep = "\t")
    depths = q2templates.df_to_html(depths)

    # Load in plot
    plot_fp = os.path.join(output_dir,'myplot.png')

    
    q2templates.render(index, output_dir, context={
                       'errors': errors,
                       'summary': None,
                       'model_summary': None,
                       'model_results': depths,
                       'multiple_group_test': None,
                       'pairwise_tests': None,
                       'paired_difference_tests': None,
                       'plot': True,
                       'plot_name': "My Plot",
                       'raw_data': None,
                       'pairwise_test_name': None,
    })
    


