from enum import Enum
import datetime


class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"



class ETLActionType(Enum):
    FULL_REFRESH = "full_refresh"
    IncrementalField = "incremental"
    
class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    
class PreHookSteps(Enum):
    EXECUTE_SQL_QUERY = "execute_sql_folder"
    CREATE_SQL_STAGING = "create_sql_staging_tables"

class DestinationName(Enum):
    Datawarehouse = "dw_reporting"
    
class SourceName(Enum):
    DVD_RENTAL = "dvd_rental"
    COLLEGE = "college"

class SQLTablesToReplicate(Enum):
    RENTAL = "dvd_rental.rental"
    FILM = "dvd_rental.film"
    ACTOR = "dvd_rental.actor"
    STUDENTS = "college.student"

class IncrementalField(Enum):
    RENTAL = "rental_last_update"
    FILM = "film_last_update"
    ACTOR = "actor_last_update"

class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"
    POST_HOOK = "post-hook"
class Date(Enum):
    FIRST_DATE=datetime.datetime(1992,6,19)
class  hook_steps(Enum):
    FULL_REFRESH="full_refresh"
    INCREMENTAL="incremental"
    INTIALIZE="initialize"

    