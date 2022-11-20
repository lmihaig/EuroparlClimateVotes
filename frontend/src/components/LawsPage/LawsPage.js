import React from "react";
import Navbar from "../navbar/navbar";
import { useState , useEffect} from 'react';
import $ from 'jquery'; 
import SortTable from "../SortTable";
import obama from '../images/politician-pic.webp'


function LawsPage() {


  const [meps, setData] = useState({laws:[{}]})
  
  useEffect(() => {
    fetch("http://sima.zapto.org:8071/laws").then(
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


    return(
      <div>
      <Navbar />
      <div>

      <table id="example" class="table w-75 mx-auto">
        <thead>
          <tr>
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
          {meps.laws.map((d) => (
            <tr>
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


export default LawsPage;