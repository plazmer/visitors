<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8" />
        <title></title>
        <!-- link rel="stylesheet" href="style.css" / -->
    </head>
    <body>
    %#template for the form for a new task
        <form action="/new" method="POST">
            <p>
                <select size="5" name="group">
                    <option disabled>Выберите группу</option>
                    <option value="Группа 8.30">Группа 8.30</option>
                    <option value="Группа 12.00">Группа 12.00</option>
                    <option value="-">-</option>
                </select>
            </p>

            <p>ФИО<br />
                <input type="text" size="100" maxlength="100" name="fio">
            </p>
            <p>
                <input type="submit" name="save" value="Я ТУТ!">
            </p>
        </form>
    </body>
</html>
