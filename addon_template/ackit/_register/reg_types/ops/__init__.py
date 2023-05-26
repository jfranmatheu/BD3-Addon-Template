from .operator import Operator, OpsReturn
from .modal import ModalOperator, ModalFlags


class OperatorTypes:
    ACTION = Operator
    MODAL = ModalOperator
    DRAW_MODAL = None # TODO: support draw modal operators.
