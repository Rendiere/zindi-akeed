from pathlib import Path
from invoke import task


@task(help={
    'ip': 'IP to listen on, defaults to *',
    'extra': 'Port to listen on, defaults to 8888',
})
def lab(ctx, ip='*', port=8888):
    """
    Launch Jupyter lab
    """
    cmd = ['jupyter lab', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))


@task(help={
    'ip': 'IP to listen on, defaults to *',
    'extra': 'Port to listen on, defaults to 8888',
})
def notebook(ctx, ip='*', port=8888):
    """
    Launch Jupyter notebook
    """
    cmd = ['jupyter notebook', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))



@task()
def check_data(ctx):
    """
    Check that all the data is downloaded
    into the correct directory
    """
    pth = Path('data/raw')

    files = [str(f) for f in sorted(list(pth.glob('*')))]

    correct_list = [
    'data/raw/.gitkeep',
    'data/raw/SampleSubmission.csv',
    'data/raw/Variable Definitions.txt',
    'data/raw/orders.csv',
    'data/raw/test_customers.csv',
    'data/raw/test_locations.csv',
    'data/raw/train_customers.csv',
    'data/raw/train_locations.csv',
    'data/raw/vendors.csv'
    ]

    assert len(files) == len(correct_list), '''
    The follwoing files files were missing: \n{}
    '''.format(set(correct_list) - set(files))

    for f1, f2 in zip(correct_list, files):
        if f1 != f2:
            raise FileNotFoundError('File {} missing!'.format(f1))
