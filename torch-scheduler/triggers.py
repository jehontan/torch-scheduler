from abc import ABC
from typing import Any, Callable

class SchedulerTrigger(ABC):
    def check(self) -> bool:
        '''Check if trigger condition is met.
        
        Returns
        -------
        is_triggered
            True if tigger condition is met, False otherwise.
        '''
        return NotImplementedError

class ObjectAttributeTrigger(SchedulerTrigger):
    '''Trigger on condition of object attribute.

    This trigger is activated by checking a named attribute of a target object
    using a specified condition callable.
    '''

    def __init__(self, target_obj:object, attr_name:str, cond_fn:Callable[[Any], bool]):
        '''
        Parameters
        ----------
        target_obj : object
            Target object to check.
        attr_name : str
            Name of attribute of target to check.
        cond_fn : Callable[[Any], bool]
            Callable to check condition. Should have signature `(attr_val) -> bool`
            and return `True` if trigger condition is met.
        '''
        super().__init__()

        self.target_obj = target_obj
        self.attr_name = attr_name
        self.cond_fn = cond_fn

    def check(self) -> bool:
        return self.cond_fn(self.target_obj.__getattr__(self.attr_name))