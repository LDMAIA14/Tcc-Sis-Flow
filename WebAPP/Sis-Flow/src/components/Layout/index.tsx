import React, { Children } from "react";
import { Grid } from "./styles";
import Aside from "../Aside";
import MainHeader from "../MainHeader";
import Content from "../Content";

interface ChildrenProps {
    children: React.ReactNode;
}

const Layout: React.FC<ChildrenProps> = ({ children })=>{
    return(
        <Grid>
            <MainHeader/>
            <Aside/>
            <Content>
                { children } 
            </Content>

        </Grid>
    );
}
export default Layout;


