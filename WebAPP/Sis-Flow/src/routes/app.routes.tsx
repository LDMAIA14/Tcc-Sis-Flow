import React from "react";
import { 
    Route,
    Routes
} from 'react-router-dom'

import Layout from "../components/Layout";
import Dashboard from "../pages/Dashboard";
import List from "../pages/List";
import Zps from "../pages/Zps";

const AppRoutes: React.FC = () => (
    <Layout>
        <Routes>
            <Route path="/" element={<Dashboard/>}/>
            <Route path="/dashboard" element={<Dashboard />}/>
            <Route path="/list/:type" element={<List/>}/>
            <Route path="/zonaspressao" element={<Zps/>}/>
        </Routes>
    
    </Layout>
);

export default AppRoutes;