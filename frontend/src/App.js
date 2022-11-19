import { Route, Routes, BrowserRouter as Router } from 'react-router-dom'
import React from "react";
import MainPage from "./components/mainPage/MainPage";
import MPPage from "./components/MPPage/MPPage";
import LawsPage from "./components/LawsPage/LawsPage";
const App = () => {
  return (

    <Router>
      <Routes>
        <Route exact path='/' element={<MainPage />} />
        <Route exact path='Laws' element={<LawsPage />} />
        <Route exact path='MembersOfParliament' element={<MPPage />} />
      </Routes>
    </Router>
  )
}

export default App;