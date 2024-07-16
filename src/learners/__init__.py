from .q_learner import QLearner
from .q_learner_td import QLearner_TD
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["q_learner_td"] = QLearner_TD
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
