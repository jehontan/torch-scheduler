from abc import ABC
from typing import Any, Callable, Dict, Tuple, Optional, Union, Sequence

from .actions import SchedulerAction
from .triggers import SchedulerTrigger

class CustomScheduler:
    def __init__(self):
        self.triggers_actions:Dict[str, Tuple[SchedulerTrigger, SchedulerAction]] = dict()

    def register(self, name:str, trigger:SchedulerTrigger, action:SchedulerAction) -> None:
        '''Register an action to be perform on trigger condition.

        Parameters
        ----------
        name : str
            Name for the entry.
        trigger : SchedulerTrigger
            Trigger condition.
        action : SchedulerAction
            Action to be performed upon trigger.
        '''
        
        self.triggers_actions[name] = (trigger, action)

    def register_multiple(self, triggers_actions:Sequence[Tuple[str, SchedulerTrigger, SchedulerAction]]) -> None:
        '''Register multiple trigger-action pairs.

        Parameters
        ----------
        triggers_actions : Sequence[Tuple[str, SchedulerTrigger, SchedulerAction]]
            Named trigger-action pairs to register.
        '''
        self.triggers_actions.update((triggers_actions[0], triggers_actions[1:]))

    def remove(self, name:str):
        '''Remove registered trigger-action by name.

        Parameters
        ----------
        name : str
            Name of trigger-action pair to remove.
        '''
        del self.triggers_actions[name]

    def update(self):
        '''Check all triggers and perform all necessary actions.'''

        for name, trigger_action in self.triggers_actions.items():
            trigger, action  = trigger_action
            if trigger.check():
                action()