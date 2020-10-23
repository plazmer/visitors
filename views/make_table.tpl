<table border="1">
  <tr>
    <th>id</th>
    <th>groups</th>
    <th>fio</th>
    <th>datetime</th>
  </tr>
%for row in rows:
  <tr>
    <td>{{ row['id'] }}</td>
    <td>{{ row['groups'] }}</td>
    <td>{{ row['fio'] }}</td>
    <td>{{ row['datetime'] }}</td>
  </tr>
  %end
</table>