import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";

const columns = [
  { field: "id", headerName: "emp_no", width: 100 },
  { field: "firstName", headerName: "First name", width: 130 },
  { field: "lastName", headerName: "Last name", width: 130 },
  {
    field: "gender",
    headerName: "Gender",
    type: "character",
    width: 90,
  },
  {
    field: "birth_date",
    headerName: "Birth Date",
    type: "date",
    width: 130,
  },
  {
    field: "hire_date",
    headerName: "Hire Date",
    type: "date",
    width: 130,
  },
];

const row = [
  { id: 1, lastName: "Snow", firstName: "Jon", age: 35 },
  { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
  { id: 3, lastName: "Lannister", firstName: "Jaime", age: 45 },
  { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
  { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
  { id: 6, lastName: "Melisandre", firstName: null, age: 150 },
  { id: 7, lastName: "Clifford", firstName: "Ferrara", age: 44 },
  { id: 8, lastName: "Frances", firstName: "Rossini", age: 36 },
  { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65 },
];

export default function DataTable() {
    const [rows, setRows] = React.useState([]);
  React.useEffect(() => {
    axios
      .get("http://localhost:5000/admin/Get_all_users")
      .then((res) => {
        console.log(res.data);
        setRows(res.data);
        for (let i = 0; i < res.data.length; i++) {
          res.data[i].id = i;
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <div style={{ height: 800, width: "80%" }}>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 5 },
          },
        }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
    </div>
  );
}
