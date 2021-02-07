from enum import Enum
from django.db import connection

def exec_sql(sql_query, values):
    try:
        cursor = connection.cursor()
        
        cursor.execute(sql_query, values)

    except expression as identifier:
        pass

def exec_sql_get_data(sql_query, values):
    try:
        cursor = connection.cursor()

        cursor.execute(sql_query, values)
        
        return dictfetchall(cursor)

    except expression as identifier:
        pass

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class Sql_Queries(Enum):
    GET_ALL_SOME_TEXTS = """
    select concat("Some_Text_", (@r := @r + 1)) Some_Text_Label,
    t.Id
    from tbl_some_text t,
    (select @r := 0) r
    WHERE t.Is_Deleted = 0
    """
    DELETE_SOME_TEXT = """
    UPDATE tbl_some_text
    SET Is_Deleted = 1
    WHERE Id = %s
    """
    ADD_SOME_TEXT = """
    INSERT INTO tbl_some_text
    (Is_Deleted)
    VALUES
    (0);
    """
    ADD_SOME_TEXT_BOX = """
    INSERT INTO tbl_some_text_box
    (Some_Text_Id,
    Box_Content)
    VALUES
    (%s, %s);
    """
    GET_ALL_SOME_TEXT_BOXES  = """
    SELECT
        t.Id,
        t.Some_Text_Id,
        t.Box_Content,
        concat("Box_", (
        CASE WHEN t.Some_Text_Id = @last_text_id
            THEN @r := @r + 1
            ELSE @r := 1
        END
        )) Box_Label,
        @last_text_id := t.Some_Text_Id
    FROM 
        bmkct.tbl_some_text_box t,
    (select @r := 0, @last_text_id := 0) r
    WHERE t.Is_Deleted = 0 AND t.Some_Text_Id = %s
    """
    UPDATE_SOME_TEXT_BOX = """
    UPDATE tbl_some_text_box
    SET Box_Content = %s
    WHERE Id = %s
    """