from ..core import Machine

from .nesting import HierarchicalMachine, NestedTransition, NestedEvent
from .locking import LockedMachine, LockedEvent
from .diagrams import MachineGraphSupport, TransitionGraphSupport

class MachineFactory(object):

    # get one of the predefined classes which fulfill the criteria
    @staticmethod
    def get_predefined(graph=False, nested=False, locked=False):
        if graph and nested and locked:
            return LockedHierarchicalGraphMachine
        elif locked and nested:
            return LockedHierarchicalMachine
        elif locked and graph:
            return LockedGraphMachine
        elif nested and graph:
            return HierarchicalGraphMachine
        elif graph:
            return MachineGraphSupport
        elif nested:
            return HierarchicalMachine
        elif locked:
            return LockedMachine
        else:
            return Machine


class NestedGraphTransition(TransitionGraphSupport, NestedTransition):
    pass


class LockedNestedEvent(LockedEvent, NestedEvent):
    pass


class HierarchicalGraphMachine(MachineGraphSupport, HierarchicalMachine):

    @staticmethod
    def _create_transition(*args, **kwargs):
        return NestedGraphTransition(*args, **kwargs)


class LockedHierarchicalGraphMachine(LockedMachine, HierarchicalGraphMachine):
    pass


class LockedHierarchicalMachine(LockedMachine, HierarchicalMachine):

    @staticmethod
    def _create_event(*args, **kwargs):
        return LockedNestedEvent(*args, **kwargs);


class LockedGraphMachine(MachineGraphSupport, LockedMachine):
    pass


