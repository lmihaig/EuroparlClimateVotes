import React from "react";
import Navbar from "../navbar/navbar";
import { useState , useEffect} from 'react';

function MPPage() {


  const [meps, setData] = useState([{}])
  
  useEffect(() => {
    fetch("http://sima.zapto.org:8071/meps").then(
      res => res.json()
    ).then(
      meps => {
        setData(meps)
        console.log(meps)
      }
    )
  }, [])


  const [data, setdata] = useState(meps);
  const [order, setorder] = useState("ASC");
  const sorting = (col) => {
    if (order === "ASC") {
      const sorted = [...data].sort((a, b) =>
        a[col] > b[col] ? 1 : -1
      );
      setdata(sorted);
      setorder("DSC");
    }

    if (order === "DSC") {
      const sorted = [...data].sort((a, b) =>
        a[col] > b[col] ? 1 : -1
      );
      setdata(sorted);
      setorder("ASC");
    }
  };

//   let table = new DataTable('#example', {
    
// });

    return(
      <div>
      <Navbar />
      <div>
      <img src="images/obama.webp" width="70px" height="70px" />

      <table id="example" class="table w-75 mx-auto">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col" onClick={() => sorting("name")}>
              Name
            </th>
            <th scope="col" onClick={() => sorting("score")}>
              Score
            </th>
          </tr>
        </thead>
        <tbody>
          {data.map((d) => (
            <tr>
              <td>
                <img src="src\components\images\obama.webp" width="70px" height="70px" />
              </td>
              <td>{d.name}</td>
              <td>{d.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </div>
  );
}

export default MPPage;
