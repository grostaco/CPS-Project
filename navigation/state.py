from __future__ import annotations

from typing import Optional, Callable, Any, TypedDict
from .robot import Robot as _Robot

class Environment(TypedDict):
    Robot: _Robot
    TIME_STEP: int 


class State:
    def __init__(self, update_fn: Callable[[Environment], Any]): 
        self.update_fn = update_fn
        self.states: list[tuple[State, Callable[[Environment], bool]]] = []
    
    def connect(self, state: State, guard: Callable[[Environment], bool]): 
        self.states.append((state, guard))
    
    def update(self, env: Environment) -> Optional[State]: 
        for state, guard in self.states:
            if guard(env):
                return state
        self.update_fn(env)
