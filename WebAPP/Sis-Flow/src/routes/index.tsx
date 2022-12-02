import React from "react";
import {BrowserRouter} from 'react-router-dom'

import {useAuth} from '../hooks/auth';

import AuthRoutes from "./auth.routes";
import App from "./app.routes";
import AppRoutesOp from "./app.routes_op";


const Routes: React.FC = () => {
    const {logged,permission} = useAuth();
    let permT = 0;
  
    switch(permission){
        case('Admin'):
            permT = 1
            break;
        case('Opera'):
            permT = 2
            break;
        default:
            permT = 0
            break;
    }
    const type = permT;
    if(type===2){
        return(
            <BrowserRouter>
               <AppRoutesOp/>     
            </BrowserRouter>
        )
    }
    if(type===1){
        return(
            <BrowserRouter>
                <App/>
            </BrowserRouter>
            
        )   
    }
    return(
        <BrowserRouter>
            <AuthRoutes/>
        </BrowserRouter>
        
    )
}

export default Routes;