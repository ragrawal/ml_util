import pytest
import logging
import pandas as pd
from sklearn import preprocessing
from mlplumber import pandas_adapter


@pytest.fixture(scope='function')
def complex_dataframe():
    return pd.DataFrame({'target': ['a', 'a', 'b', 'b', 'c', 'c'],
                         'feat1': [1, 2, 3, 4, 5, 6],
                         'feat2': [1, 2, 3, 2, 3, 4]})


def test_module_adaptation(complex_dataframe):
    pandas_adapter.adapt_all_as_pandas_transformer(preprocessing)
    x = preprocessing.LabelBinarizerDF()
    outDF = x.fit_transform(complex_dataframe[['target']])
    assert all([c1 == c2 for (c1, c2) in zip(outDF.columns, ['a', 'b', 'c'])])


def test_logger(caplog, complex_dataframe):
    from sklearn import preprocessing
    logger = logging.getLogger('mlplumber')
    logger.setLevel(logging.INFO)
    pandas_adapter.adapt_all_as_pandas_transformer(preprocessing)
    assert 'Register' in caplog.text
