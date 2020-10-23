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
            <div>
                <select size="5" name="group">
                    <option disabled>Выберите группу</option>
                    <option value="ЭМ-111111">ЭМ-111111</option>
                    <option value="ЭМ-222222">ЭМ-222222</option>
                    <option value="ЭМ-333333">ЭМ-333333</option>
                </select>
            </div>
            <div>ФИО<br />
                <input type="text" size="100" maxlength="100" name="fio">
            </div>
            <div>
                <input type="submit" name="save" value="Я ТУТ!">
            </div>
        </form>
        <div><a href="/list">LIST</a></div>
    </body>
</html>
