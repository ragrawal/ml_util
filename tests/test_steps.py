import pytest
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelBinarizer

from baikal import Input, Model
import pickle

from mlplumber.steps import DataFrameMapperStep


@pytest.fixture
def complex_dataframe():
    return pd.DataFrame({'target': ['a', 'a', 'b', 'b', 'c', 'c'],
                         'feat1': [1, 2, 3, 4, 5, 6],
                         'feat2': [1, 2, 3, 2, 3, 4]})


def test_data_frame_mapper_step_serialization(complex_dataframe):
    """
    Get transformed names of features in `transformed_names` attribute
    for a transformation that multiplies the number of columns
    """
    inDF = complex_dataframe
    x = Input(name='X')
    y = Input(name='target')
    transformer = DataFrameMapperStep(
        [('target', LabelBinarizer())],
        name='transformer',
        df_out=True
    )(x, y)
    model = Model(x, transformer, y)
    model.fit(inDF, inDF[['feat1']])
    mapper_pickled = pickle.dumps(model)

    loaded_mapper = pickle.loads(mapper_pickled)
    assert np.array_equal(
        model.predict(inDF).values,
        loaded_mapper.predict(inDF).values
    )
