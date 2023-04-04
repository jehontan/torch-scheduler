from abc import ABC
from typing import Any, Callable, List, Tuple, Optional, Union

class SchedulerAction(ABC):
    def __call__(self) -> None:
        '''Perform action.'''
        raise NotImplementedError

class ObjectAttributeAction(SchedulerAction):
    def __init__(self,
                 target_obj:object,
                 target_attr:str,
                 action_fn:Callable[..., Any],
                 args:Optional[List[Tuple[object, str]]]=None
                ):
        '''
        Parameters
        ----------
        target_obj : object
            Target object to modify.
        target_attr : str
            Attribute name of target object to modify.
        action_fn : Callable[..., Any]
            Action to perform. Should accept argument in `args` and return
            new value for target object attribute.
        args : Optional[List[Tuple[object, str]]], optional
            Additional (object, attribute name) pairs whose value will be
            supplied as arguments to `action_fn`, by default None
        '''
        super().__init__()
        self.target_obj = target_obj
        self.target_attr = target_attr
        self.action_fn = action_fn
        self.args = args if args else list()

    def __call__(self) -> None:
        args = [o.__getattr__(a) for o, a in self.args]
        val = self.action_fn(*args)
        self.target_obj.__setattr__(self.target_attr, val)