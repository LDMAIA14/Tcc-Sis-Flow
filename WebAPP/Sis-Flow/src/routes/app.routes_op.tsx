import React from "react";
import { 
    Route,
    Routes
} from 'react-router-dom'

import Layout from "../components/Layout";
import Dashboard from "../pages/Dashboard";
import List from "../pages/List";


const AppRoutesOp: React.FC = () => (
    <Layout>
        <Routes>
            <Route path="/" element={<Dashboard/>}/>
            <Route path="/dashboard" element={<Dashboard />}/>
            <Route path="/list/:type" element={<List/>}/>
        </Routes>
    
    </Layout>
);

export default AppRoutesOp;