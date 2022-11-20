import React from "react";
import Navbar from "../navbar/navbar";
import { useState , useEffect} from 'react';
import obama from '../images/politician-pic.webp'

function MPPage() {


  const [meps, setData] = useState({meps:[{}]})
  
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

      <table id="example" class="table w-75 mx-auto">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col" onClick={() => sorting("name")}>
              Name
            </th>
            <th scope="col" onClick={() => sorting("pro")}>
              Pro
            </th>
            <th scope="col" onClick={() => sorting("contra")}>
              Contra
            </th>
            <th scope="col" onClick={() => sorting("abstain")}>
              Abstain
            </th>
          </tr>
        </thead>
        <tbody>
          {meps.meps.map((d) => (
            <tr>
              <td>
                <img src={obama} width="70px" height="70px" />
              </td>
              <td>{d.name}</td>
              <td>{d.pro}</td>
              <td>{d.contra}</td>
              <td>{d.abstain}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </div>
  );
}

export default MPPage;
