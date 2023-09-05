from .operator import ACK_Operator, OpsReturn
from .modal import ACK_ModalOperator, ACK_ModalFlags


class OperatorTypes:
    ACTION = ACK_Operator
    MODAL = ACK_ModalOperator
    DRAW_MODAL = None # TODO: support draw modal operators.
