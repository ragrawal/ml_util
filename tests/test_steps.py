from baikal import Step
from catboost import CatBoostClassifier
from mlplumber.steps import CatBoostClassifierStep


def test_initialize_step():

    x = CatBoostClassifierStep(name='hello')
    assert isinstance(x, Step)
    assert isinstance(x, CatBoostClassifier)
