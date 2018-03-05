import logging

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy_utils import UUIDType

from walkoff.executiondb import Device_Base
from walkoff.executiondb.representable import Representable

logger = logging.getLogger(__name__)


class Position(Representable, Device_Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    _action_id = Column(UUIDType(binary=False), ForeignKey('action.id'))
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)

    def __init__(self, x, y):
        """Initializes a new Position object. An Action has a Position object.

        Args:
            x (float): The X coordinate of the Action.
            y (float): The Y coordinate of the Action.
        """
        self.x = x
        self.y = y
