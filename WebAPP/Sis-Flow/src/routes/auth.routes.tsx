import React from "react";
import { BrowserRouter,Route,Routes} from 'react-router-dom';

import Signin from "../pages/Signin";

const AuthRoutes: React.FC = () => (
    <Routes>
        <Route path="*" element={<Signin/>}/>
    </Routes>

)


export default AuthRoutes;