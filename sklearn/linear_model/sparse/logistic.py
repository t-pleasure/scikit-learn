from ..logistic import LogisticRegression
from ...utils import deprecated


@deprecated("""to be removed in v0.12;
use sklearn.linear_model.LogisticRegression instead""")
class LogisticRegression(LogisticRegression):
    pass
