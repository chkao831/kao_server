import React from "react";
import { Container} from "@material-ui/core";
import {BrowserRouter, Routes, Route} from 'react-router-dom';

import NewHome from './components/Home/NewHome'
import Navbar from "./components/Navbar/Navbar";

const App = () => {

    return(
        <BrowserRouter>
            <Navbar/>
            <Routes>
                <Route path='/' exact element={<NewHome />}></Route>
            </Routes>
        </BrowserRouter>

        
    );
}

export default App;