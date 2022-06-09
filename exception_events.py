import sys

from connection.nivy.nivy import Nivy
from repository.models.task_model import TaskModel
from repository.repository.repository import Repository 
from .logger import Logger
from system.operation_system import OperationSystem

class ExceptionEvents(Logger):
    
    def __init__(self) -> None:
        super().__init__()
        self._database = Repository()
        self._os = OperationSystem()
        self._api = Nivy()
    
    def warning_to_try_again(self, message: str, task: TaskModel):
        self.warning(message=message)
        self._database.burnt_attempt(task=task)
        self._database.insert_error_message(message=message, task=task)
        self._os.close_chrome_instances()
        sys.exit(message)
    
    def error_eliminates_any_chances_try_again(self, message: str, task: TaskModel):
        self.error(message=message)
        self._database.eliminates_any_chance_of_trying_again(task=task)
        self._database.insert_error_message(message=message, task=task)
        self._database.insert_error_in_status(task)
        self._os.close_chrome_instances()
        self._database.delete_task(task)
        self._api.post_error(id=task.id, token=task.token, messages_error=message)
        sys.exit(message)
    
    def critical_when_impossible_to_try(self, message: str, task: TaskModel):
        self.critical(message=message)
        self._database.insert_error_message(message=message, task=task)
        self._database.insert_critical_in_status(task)
        self._os.close_chrome_instances()
        self._database.delete_task(task=task)
        self._api.post_error(id=task.id, token=task.token, messages_error=message)
        sys.exit(message)