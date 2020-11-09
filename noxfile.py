import nox


@nox.session
def lint(session):
    session.install('pytest==5.3.5', 'setuptools==45.2',
                    'wheel==0.34.2', 'flake8==3.7.9',
                    'numpy==1.18.1', 'pandas==1.0.5')
    session.install('.')
    session.run('flake8', 'mlplumber/')


@nox.session
@nox.parametrize('pandas', ['1.0.5', '1.1.0'])
@nox.parametrize('sklearn_pandas', ['2.0.0', '2.0.3'])
def tests(session, pandas, sklearn_pandas):
    session.install('pytest==5.3.5', 'setuptools==45.2',
                    'wheel==0.34.2', 'flake8==3.7.9',
                    'numpy==1.18.1', f'pandas=={pandas}',
                    f'sklearn_pandas=={sklearn_pandas}')
    session.install('.')
    session.run('py.test', 'README.rst', 'tests')
